from binance.client import Client
from config import API_KEY, API_SECRET, BASE_URL

# Initialize Binance client
client = Client(API_KEY, API_SECRET)
client.FUTURES_URL = BASE_URL  # Testnet URL

try:
    # Test server time to verify connection
    server_time = client.futures_time()
    print("Connection successful! Server time:", server_time)
except Exception as e:
    print("Connection failed:", e)
