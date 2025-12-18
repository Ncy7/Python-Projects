import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import EMAIL_SENDER, EMAIL_PASSWORD, EMAIL_RECEIVER, SMTP_SERVER, SMTP_PORT  # Add this import

def send_email_alert(product_title, current_price, product_url, target_price):
    subject = f"PRICE DROP ALERT: {product_title}"
    body = f"""
    Good news! The price dropped to ${current_price:.2f} (your target: ${target_price:.2f})
    
    Product: {product_title}
    Link: {product_url}
    
    Time to buy! 🚀
    """
    
    msg = MIMEMultipart()
    msg["From"] = EMAIL_SENDER
    msg["To"] = EMAIL_RECEIVER
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))
    
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())
        server.quit()
        print("📧 Price alert email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

URL = "https://www.amazon.com/Poop-Learn-Useless-Perfect-Curious/dp/3982670632/ref=sr_1_6?_encoding=UTF8&content-id=amzn1.sym.1de72386-12c8-42a9-ba27-a781e38af974&dib=eyJ2IjoiMSJ9.nr-hUe_Q5btjJ1mkR1polw3HxEHkEdNtsrW2xUCKU09Clv5O8UEP-ZOPTPIuHQmmWyA7tmVfBWyYWkdPxxdWLV8lm5qygwNyQnMP1PpWkyy6So28A8W4QeZtBsjcfjrKUxcJ_jYbFSBXpqC5JccbAr-yiyyLoI5340ZSConESnfqJxrDVATCZBaVdJAGVZNpJQlYSf6QH1HhDJKnABMlBm3pE9KJkc0Y9_9BzEIiH_5BOoC66mlhWbDWQ1AGB9rH1xznWCXQQoBlmdG4N9ZUetTyJg9A-2KqE6GOV1Bl1R4.7ncZJmfHAo5UA-UkOGHlOm1wgYzGjb_KQ6A7aFwiKNU&dib_tag=se&keywords=gifts&pd_rd_r=04adbac5-24b9-4b44-9c8f-b3512f0f12c2&pd_rd_w=2kgC8&pd_rd_wg=LDIA4&qid=1766073555&refinements=p_36%3A-5000&sr=8-6"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

# Make the request
response = requests.get(URL, headers=HEADERS)   #requests.get() with headers: Amazon blocks automated scripts without a proper "User-Agent" (it thinks you're a bot). This header tricks it into thinking you're a real Chrome browser.

# Check if we got the page successfully
if response.status_code != 200:
    print(f"Error: Got status code {response.status_code}")
    print("Amazon might be blocking the request. Try again later.")
else:
    # Parse the HTML
    soup = BeautifulSoup(response.content, "html.parser")   #BeautifulSoup: Parses the messy HTML and lets us search by tag, id, or class.

    
    # Title extraction
    title_element = soup.find("span", id="productTitle")    #id="productTitle": Reliable for the title (Amazon uses this consistently).
    title = title_element.get_text(strip=True) if title_element else "Title not found"
    
    # Extract price - try multiple common selectors
    price_str = "Price not found"
    price_element = soup.find("span", class_="a-offscreen")
    if price_element:
        price_str = price_element.get_text(strip=True)
    else:
        # Fallback attempt
        whole = soup.find("span", class_="a-price-whole")
        fraction = soup.find("span", class_="a-price-fraction")
        if whole and fraction:
            price_str = "$" + whole.get_text(strip=True) + fraction.get_text(strip=True)
    
    price_str = price_str.replace("\n", "").strip()
    
    print("\n" + "="*60)
    print(f"Product: {title}")
    print(f"Current Price: {price_str}")
    print("="*60)

        # Price comparison logic - safer version
    print(f"Current Price: {price_str}")
    
    if price_str and price_str != "Price not found":
        # Extract numbers (handle $29.99 or $29,99 etc.)
        import re
        numbers = re.findall(r'\d+\.?\d*', price_str)
        if numbers:
            current_price = float(numbers[0])
            if current_price <= target_price:
                print(f"🎉 PRICE DROP ALERT! Current price (${current_price:.2f}) is at or below your target (${target_price:.2f})")
                print("Time to buy!")
                send_email_alert(title, current_price, url, target_price)  # ← Added this line
            else:
                print(f"😔 Still too high. Current: ${current_price:.2f} > Target: ${target_price:.2f}")
        else:
            print("Could not parse the price number — check manually.")
    else:
        print("Could not retrieve a valid price this time — try again later or check the page manually.")
    print("="*60)