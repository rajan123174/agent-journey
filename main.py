import os
from dotenv import load_dotenv

load_dotenv()  # finds .env next to this file or in a parent folder

key = os.getenv("MY_API_KEY")

if key is None:
    print("No key found. Check your .env file name and the variable name.")
else:
    print(f"Key loaded. It starts with: {key[:5]}...")