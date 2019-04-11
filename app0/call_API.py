import requests

url = "http://127.0.0.1:8000/api/tasksmtd/"

payload = "{\"service_type\":\"mimic-web\",\"username\":\"lwy1\",\"mima\":\"123456\"}"
headers = {
    'Content-Type': "application/json",
    'cache-control': "no-cache",
    'Postman-Token': "4b44cbb1-7cc8-41a2-82f2-ea37c3338fb6"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
