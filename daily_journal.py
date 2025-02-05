import requests
import datetime
import pytz  # Import library timezone

# API untuk mendapatkan quote
api_url = "https://api.api-ninjas.com/v1/quotes"
headers = {'X-Api-Key': 'dbvRtRS2xqO4pe72YUsrRw==1FpgIQpTJrWZFo1B'}

response = requests.get(api_url, headers=headers)

if response.status_code == 200:
    quote_data = response.json()[0]
    quote = quote_data["quote"]
    author = quote_data["author"]
else:
    quote = "Failed to retrieve quote."
    author = "Unknown"

# Konversi timestamp ke zona waktu Jakarta (GMT+7)
jakarta_tz = pytz.timezone('Asia/Jakarta')
timestamp = datetime.datetime.now(pytz.utc).astimezone(jakarta_tz).strftime('%Y-%m-%d %H:%M:%S')

new_entry = f"{timestamp} - \"{quote}\" - {author}\n"

# Menyimpan ke progress.txt (format tetap)
with open("progress.txt", "a") as file:
    file.write(new_entry)

# Menyimpan ke PROGRESS.md dengan format Markdown yang sudah dipisah kolomnya
with open("PROGRESS.md", "a") as md_file:
    md_file.write(f"| {timestamp} | \"{quote}\" | {author} |\n")

print("Progress updated in both progress.txt and PROGRESS.md.")
