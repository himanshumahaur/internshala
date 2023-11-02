
import requests

url = "https://api.airtable.com/v0/appQsEV94eQuwURPi/tblgkvDKVKpNbWV2L"

headers = {
    "Authorization": "Bearer patijTY4ITapmTa9W.8ca91c85013328f160b793d0ab2be245c1777f628b1450009345ab0f0fc2d2a6"
}

res = requests.get(url, headers=headers).json()

for record in res['records']:
    print(f"Details: {record['fields']['FirstName']} {record['fields']['LastName']} {record['fields']['Status'].title()}")