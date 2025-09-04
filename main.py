import requests
import smtplib
from bs4 import BeautifulSoup
import os

# Load environment variables from .env
MY_EMAIL = os.getenv("EMAIL")
MY_PASSWORD = os.getenv("PASSWORD")
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"

}

# Step 1: Scrape product price
URL = "https://www.amazon.in/Not-Quite-Dead-Holly-Jackson/dp/059397705X/ref=tmm_hrd_swatch_0?_encoding=UTF8&dib_tag=se&dib=eyJ2IjoiMSJ9.T5kSAGXt4DgkbMWbj8nxNV4w9_-hHtueePmZouyeKmW1N5d7EQ3PBWk0FClMM9qzz-HkOFWIbhYlAH7JuZPQqW5eOKkVPxEfX3A5kBxhO-ldFndj2NJgYEDxXA9tvO-_.eEJlk8ATizbQIxcuREh1UIS2TsB0_dMu0d8FoduSpQQ&qid=1756977351&sr=8-1"
response = requests.get(URL,headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

price_whole = soup.select_one("span.a-price-whole")
price_fraction = soup.select_one("span.a-price-fraction")

if price_whole:
    whole = price_whole.getText().replace(",", "").strip()
    fraction = price_fraction.getText().strip() if price_fraction else "00"
    price = float(f"{whole}.{fraction}")
else:
    raise ValueError("Could not find price on the page")

print("Parsed price:", price)

title="Not Quite Dead Yet Hardcover – 22 July 2025 by Holly Jackson (Author)"

# Step 2: Check price and send email
if price < 800:
    subject = "Price Alert: Instant Pot Price Dropped!"
    body = f"{title} is now {price}Rupees!\nCheck it here: {URL}"
    msg = f"Subject:{subject}\n\n{body}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=msg.encode("utf-8"))

    print("📧 Email sent!")
else:
    print("No alert, price still above target.")
