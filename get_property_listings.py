import requests
from requests_oauthlib import OAuth1
from config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

# Trademe API endpoint (Sandbox environment)
url = 'https://api.tmsandbox.co.nz/v1/Search/Property/Residential.json'

# OAuth1 object
auth = OAuth1(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# API call to fetch property listings
params = {
    'region': 'Auckland',
    'listingType': 'PropertyForSale'
}

response = requests.get(url, params=params, auth=auth)

# Check response status
if response.status_code == 200:
    data = response.json()
    print("✅ Property Listings:")
    for listing in data.get('List', []):
        print(f"- {listing.get('Title', 'Unknown')} ({listing.get('PriceDisplay', 'N/A')})")
else:
    print(f"❌ Failed: {response.status_code}")
    print("Error Message:", response.text)
