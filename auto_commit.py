import requests
import os
import datetime

# Konfigurasi API Quotes
API_URL = "https://api.api-ninjas.com/v1/quotes"
HEADERS = {"X-Api-Key": "dbvRtRS2xqO4pe72YUsrRw==1FpgIQpTJrWZFo1B"}

# Ambil Quote dari API
response = requests.get(API_URL, headers=HEADERS)
if response.status_code == 200:
    quote_data = response.json()[0]
    quote_text = f'"{quote_data["quote"]}" - {quote_data["author"]}'
else:
    quote_text = "Failed to fetch quote."

# Tulis ke file progress.txt
filename = "progress.txt"
with open(filename, "a") as file:
    file.write(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {quote_text}\n")

# Git Commit dan Push
os.system("git add progress.txt")
os.system(f'git commit -m "Daily progress update: {datetime.datetime.now().strftime("%Y-%m-%d")}"')
os.system("git push origin main")
