import requests
from requests_oauthlib import OAuth1

# 🔑 받은 Consumer Key와 Secret
CONSUMER_KEY = '4CE47C16279CC989B20BA8AA5783D05A'
CONSUMER_SECRET = '4394597F3F06F1DF17EF3E2FF15ACFB2'

# 🔑 Request Token 단계에서 받은 것
OAUTH_TOKEN = '96152D844FE7BB83093576CCB03A3A6B'
OAUTH_TOKEN_SECRET = '70701EB4B0B12F270857EA4DA8D8DBB8'
VERIFIER = 'A3610F3BD3819CB441FB82837FA9ED2A'

# OAuth1 객체 생성
auth = OAuth1(CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET, verifier=VERIFIER)

# Access Token 받기
url = 'https://api.tmsandbox.co.nz/v1/Oauth/AccessToken'
response = requests.post(url, auth=auth)

# 결과 확인
if response.status_code == 200:
    print("✅ Access Token 받기 성공!")
    print("Response:", response.text)
else:
    print(f"❌ 실패: {response.status_code}")
    print("Error Message:", response.text)
