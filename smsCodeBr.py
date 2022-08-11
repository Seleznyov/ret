from seleniumrequests import Chrome
webdriver = Chrome()
root_url = "http://192.168.50.62:8080/vtb-retail/api/v1/app/"
data = {"grant_type": "password", "username": "sseleznev", "password": ""}
url = f'{root_url}oauth/token?grant_type={data["grant_type"]}&username={data["username"]}' \
      f'&password={data["password"]}'
headers = {
    "Authorization": "Basic YnJvd3NlcjpzZWNyZXQ="
}
response = webdriver.request('POST', url, headers=headers)
print(response.json())

url1 = f'{root_url}sms/send'
json_data = {"phoneNumber": "994222222222"}
headers = {
    'accept': '*/*',
    "Authorization": "Bearer " + str(response.json()["access_token"])
}

response2 = webdriver.request("POST",url1, headers=headers, json=json_data)
print(response2.json()["smsCode"])
