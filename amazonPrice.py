import requests
import smtplib
from bs4 import BeautifulSoup

# The URL of the Amazon page for the item you want to track
URL = "https://www.amazon.com/dp/B07DJHV6VZ"

# Your email address and password (insert your corresponding email and pass)
EMAIL_ADDRESS = "your-email@example.com"
EMAIL_PASSWORD = "your-email-password"

# Send a GET request to the Amazon page
page = requests.get(URL)

# Parse the HTML content of the page
soup = BeautifulSoup(page.content, "html.parser")

# Find the price of the item
price = soup.find(id="priceblock_ourprice").get_text()
price = float(price[1:])  # Convert the price to a float and remove the dollar sign

# Set the threshold price at which you want to be notified
threshold_price = 50.00

# If the price is below the threshold, send an email notification
if price < threshold_price:
    # Create the email message
    subject = "Price drop alert for Amazon item"
    body = f"The price of the item on Amazon has dropped to ${price:.2f}. Check it out at {URL}"
    msg = f"Subject: {subject}\n\n{body}"

    # Send the email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg)

print(f"The current price is ${price:.2f}")

