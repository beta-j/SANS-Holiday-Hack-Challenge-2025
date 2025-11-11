# Call URL https://its-idorable.holidayhackchallenge.com/api/receipt?id={id}
import requests
def call_receipt_api(receipt_id):
    url = f"https://its-idorable.holidayhackchallenge.com/api/receipt?id={receipt_id}"
    response = requests.get(url)
    return response.json()
if __name__ == "__main__":
    filename = "receipt_results.txt"
    for i in range(100, 155):
      test_id = i
      result = call_receipt_api(test_id)
      print(f"Receipt No.{test_id}: ")
      print(result)
