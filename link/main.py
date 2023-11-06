# cid
# // CYF8KNA2ADWG539NO0631BFAE8UVTHTB

# Client Secret
# // K5EWLPV98YV96Q17ZREKWVC4MZNEQTL96BBYUQIYAVKDRM8LVT0U54JYKH4URO6T

import requests

url = "https://api.clickup.com/api/v2/oauth/token"

query = {
  "client_id": "CYF8KNA2ADWG539NO0631BFAE8UVTHTB",
  "client_secret": "K5EWLPV98YV96Q17ZREKWVC4MZNEQTL96BBYUQIYAVKDRM8LVT0U54JYKH4URO6T",
  "code": "38A9L35O6KZZUXAW20CL2F6NXZ1RH0ZQ"
}

response = requests.post(url, params=query)

data = response.json()
print(data)