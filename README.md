How to Integrate with Trademe API

🚀 Project Overview

This project demonstrates how to integrate with the Trademe API to fetch real estate listings in New Zealand using OAuth 1.0a authentication.Currently, only the Property category is implemented, but it can be extended to other categories like Motor, Jobs, and Services. 🔥

🛠️ Features

🌟 OAuth 1.0a Authentication: Securely connect to the Trademe API.

🌟 Real Estate Data Fetching: Retrieve property listings by region and type.

🌟 Scalable Integration: Can be extended to fetch data for Motor, Jobs, and other categories.

📦 Tech Stack

Language: Python 🐍

API: Trademe API

Libraries:

requests - For HTTP requests.

requests-oauthlib - For OAuth 1.0a authentication.

python-dotenv - For managing environment variables.

🚀 Getting Started

1️⃣ Clone the Repository

git clone https://github.com/boxchan/Trademe-API-Integration.git
cd Trademe-API-Integration

2️⃣ Create a Virtual Environment

python3 -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Create a .env File

Add your API keys and secrets in a .env file:

CONSUMER_KEY=your_consumer_key
CONSUMER_SECRET=your_consumer_secret
ACCESS_TOKEN=your_access_token
ACCESS_TOKEN_SECRET=your_access_token_secret

5️⃣ Run the Script

python get_property_listings.py

🔄 Planned Improvements

🏎️ Additional Categories: Fetch data for Motor, Jobs, and other categories.

📊 Data Visualization: Regional price distribution and trend analysis.

🔒 Security Considerations

DO NOT share your .env file or API keys publicly.

.gitignore is configured to exclude sensitive files.

🛠️ Contributing

Feel free to submit issues and pull requests. For major changes, open an issue first to discuss what you would like to change.

👉 Ready to explore Trademe's data? Let's get started! 🚀🔥
