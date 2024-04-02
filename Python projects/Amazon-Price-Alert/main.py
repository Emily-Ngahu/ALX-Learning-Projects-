import requests
from bs4 import BeautifulSoup as bs
URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}

response = requests.get(url=URL, headers=headers)

if response.status_code == 200:
    html_data = response.content

    print(html_data)
    soup = bs(html_data, "html.parser")

    span_tags = soup.find(name="span" ,class_="a-offscreen")
    print(span_tags)
else:
    print("Error:", response.status_code)