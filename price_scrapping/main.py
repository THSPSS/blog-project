import requests #for sending request to amazon
from bs4 import BeautifulSoup #for getting the value from response..
import lxml
import smtplib


my_email = "contentc082@gmail.com"
password = "bokmqyvrtuxuicnj"

URL = "https://www.amazon.com/RK-ROYAL-KLUDGE-Ultra-Compact-Switch-White/dp/B0832CZNS5/ref=sr_1_1_sspa?keywords=gaming+keyboard&pd_rd_r=0e2a97dc-f6fb-462f-91e0-762f734a3504&pd_rd_w=cB4XK&pd_rd_wg=jnYGz&pf_rd_p=12129333-2117-4490-9c17-6d31baf0582a&pf_rd_r=B0S631E6NW321ZV2NJG2&qid=1666293764&qu=eyJxc2MiOiI3LjE1IiwicXNhIjoiNi44MCIsInFzcCI6IjYuMjEifQ%3D%3D&sr=8-1-spons&psc=1"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
} #for not getting CAPTCHA

response = requests.get(URL,headers=headers)
soup = BeautifulSoup(response.content,"lxml")


product_price = soup.find(class_="a-offscreen").get_text()
product_name = soup.find(id="productTitle").get_text().strip()

only_price = product_price.split("$")[1]

price_float = float(only_price)

if price_float <= 60:
    message = f"{product_name}is now {product_price}"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email,
                            msg= f"Subject:Amazon Price Alert!!\n\n"
                                f"{message}\n{URL}")

