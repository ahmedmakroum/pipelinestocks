import requests
import csv

# API call
url = "https://twelve-data1.p.rapidapi.com/stocks"
querystring = {"exchange":"NASDAQ","format":"json"}
headers = {
    "x-rapidapi-key": "0bf7e2aba0msh2655a5a5baba619p1a4d51jsn050cd154d2c6",
    "x-rapidapi-host": "twelve-data1.p.rapidapi.com"
}
response = requests.get(url, headers=headers, params=querystring)
data = response.json().get("data", [])

# Extract field names dynamically from the first item in data
if data:
    fieldnames = data[0].keys()
else:
    fieldnames = []

# CSV file path
csv_file_path = 'stocks.csv'

# Writing to CSV
with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

print(f"Data has been written to {csv_file_path}")

