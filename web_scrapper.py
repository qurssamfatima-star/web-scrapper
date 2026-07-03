from bs4 import BeautifulSoup
import pandas as pd

# List of input HTML files
html_files = [r"D:\areebas project\PycharmProjects\PythonProject\Web scrapper\Alibaba.html", r"D:\areebas project\PycharmProjects\PythonProject\Web scrapper\Alibaba2.html", r"D:\areebas project\PycharmProjects\PythonProject\Web scrapper\Alibaba3.html"]

data = []
seen = set()

for filename in html_files:
    with open(filename, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")

    containers = soup.find_all("div", class_="organic-list app-organic-search-mb-20 viewtype-gallery")

    for container in containers:
        product_cards = container.find_all("div", recursive=False)

        for card in product_cards:
            try:
                product_name = card.find("h2", class_="search-card-e-title").get_text(strip=True)
            except:
                product_name = " "

            try:
                product_price = card.find("div", class_="search-card-e-price-main").get_text(strip=True)
            except:
                product_price = " "

            try:
                product_review = card.find("span", class_="search-card-e-review").get_text(strip=True)
            except:
                product_review = " "

            try:
                seller_name = card.find("a", class_="search-card-e-company").get_text(strip=True)
            except:
                seller_name = " "

            try:
                product_description = card.find("div", class_="search-card-m-sale-features").get_text(strip=True)
            except:
                product_description = " "

            try:
                img_div = card.find("div", class_="search-card-m-imgarea search-card-m-imgarea-overlap gallery-card-layout__img")
                img_tag = img_div.find("img") if img_div else None
                product_image = img_tag['src'] if img_tag and img_tag.has_attr('src') else " "
            except:
                product_image = " "

            # De-duplication key
            key = (product_name, product_price, product_review, seller_name, product_description, product_image)
            if key not in seen:
                seen.add(key)
                data.append({
                    "Product_Name": product_name,
                    "Product_Price": product_price,
                    "Product_Review": product_review,
                    "Seller_Name": seller_name,
                    "Product_Description": product_description,
                    "Product_Image": product_image
                })

            if len(data) >= 100:
                break
        if len(data) >= 100:
            break
    if len(data) >= 100:
        break

# Export to Excel
df = pd.DataFrame(data)
df.to_excel("Alibaba_Products.xlsx", index=False)
print(f"{len(df)} unique products saved to Alibaba_Products.xlsx")
