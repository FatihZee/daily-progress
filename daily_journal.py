import requests
import datetime

# API untuk mendapatkan quote
api_url = "https://api.api-ninjas.com/v1/quotes"
headers = {'X-Api-Key': 'dbvRtRS2xqO4pe72YUsrRw==1FpgIQpTJrWZFo1B'}

response = requests.get(api_url, headers=headers)

if response.status_code == 200:
    quote_data = response.json()[0]
    quote_text = f'"{quote_data["quote"]}" - {quote_data["author"]}'
else:
    quote_text = "Failed to retrieve quote."

timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
new_entry = f"{timestamp} - {quote_text}\n"

# Menyimpan ke progress.txt
with open("progress.txt", "a") as file:
    file.write(new_entry)

# Menyimpan ke PROGRESS.md dengan format Markdown
with open("PROGRESS.md", "a") as md_file:
    md_file.write(f"| {timestamp} | {quote_text} |\n")

print("Progress updated in both progress.txt and PROGRESS.md.")
