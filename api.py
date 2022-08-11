import requests
root_url="http://192.168.50.62:8080/vtb-retail/api/v1/app/"
data = {"grant_type": "password", "username": "sseleznev", "password": "test"}

def authorization():
    url = f'{root_url}oauth/token?grant_type={data["grant_type"]}&username={data["username"]}' \
          f'&password={data["password"]}'
    headers = {"Authorization": "Basic YnJvd3NlcjpzZWNyZXQ="}
    response = requests.post(url, headers=headers)
    return response.json()["access_token"]

def send_SMS():
    access_token=authorization()
    url =f'{root_url}sms/send'
    json_data = {"phoneNumber": "994222222222"}
    headers = {'accept': '*/*',
        "Authorization": "Bearer "+str(access_token)}
    response = requests.post(url, headers=headers, json=json_data)
    return response.json()["smsCode"]

def get_use():
    access_token = authorization()
    url = f'{root_url}users/current'
    headers = {'accept': '*/*',
        "Authorization": "Bearer " + str(access_token)}
    response = requests.get(url, headers=headers)
    return response.json()["authorities"][0]["nameRu"]
