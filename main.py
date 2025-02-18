import requests
from bs4 import BeautifulSoup

# Making a GET request
r = requests.get('https://www.scrapingcourse.com/ecommerce/')

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

# Extracting all image URLs
products = soup.find_all("li", class_="product")

for index, product in enumerate(products, 1):
    print(f"Product {index}:")

    title_tag = product.find("h2", class_="woocommerce-loop-product__title")
    title = title_tag.text.strip() if title_tag else "No title found"

    product_link = product.find("a", class_="woocommerce-LoopProduct-link woocommerce-loop-product__link")
    product_link_href = product_link["href"] if product_link else "No Link found"

    img_tag = product.find("img")
    img_url = img_tag["src"] if img_tag and img_tag.has_attr("src") else "No image found"

    price_tag = product.find("span", class_="woocommerce-Price-amount")
    price = price_tag.text.strip() if price_tag else "No price found"

    r_prod = requests.get(product_link_href)

    # Parsing the HTML
    soup_prod = BeautifulSoup(r_prod.content, 'html.parser')

    # Extracting all image URLs
    description_div = soup_prod.find("div", id="tab-description")  # Use find(), not find_all()

    # Extract text from only <p> tags
    if description_div:
        paragraphs = description_div.find_all("p")  # Get all <p> tags
        product_description = "\n".join(p.get_text(strip=True) for p in paragraphs)  # Join all paragraphs
    else:
        product_description = "No description found"




    print(f"Name: {title}")
    print(f"Image URL: {img_url}")
    print(f"Price: {price}")
    print(f"URL: {product_link_href}")
    print(f"Description: {product_description}")
    print("=" * 80)
