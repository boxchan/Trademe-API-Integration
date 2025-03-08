import requests
from requests_oauthlib import OAuth1

# 🔑 받은 Consumer Key와 Secret
CONSUMER_KEY = '4CE47C16279CC989B20BA8AA5783D05A'
CONSUMER_SECRET = '4394597F3F06F1DF17EF3E2FF15ACFB2'

# OAuth1 객체 생성
auth = OAuth1(CONSUMER_KEY, CONSUMER_SECRET)

# Request Token 받기
url = 'https://api.tmsandbox.co.nz/v1/Oauth/RequestToken'
response = requests.post(url, auth=auth)

# 결과 확인
if response.status_code == 200:
    print("✅ Request Token 받기 성공!")
    print("Response:", response.text)
else:
    print(f"❌ 실패: {response.status_code}")
    print("Error Message:", response.text)
