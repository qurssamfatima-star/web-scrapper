# Alibaba Product Scraper 🕷️

A Python web scraper that extracts product data (name, price, rating, seller, description, and image) from saved **Alibaba.com search result pages** for "smart watch" and compiles them into a clean, de-duplicated Excel spreadsheet.

## 📋 Overview

This project parses locally saved HTML copies of Alibaba search results using **BeautifulSoup** and exports the extracted data into a structured `.xlsx` file using **pandas**. It scrapes across multiple saved pages, removes duplicate listings, and caps the output at 100 unique products.

## ✨ Features

- Extracts key product details from each listing card:
  - Product Name
  - Price
  - Review Rating & Count
  - Seller / Company Name
  - Description (min. order & delivery estimate)
  - Product Image URL
- Parses **multiple HTML files** in a single run
- **De-duplicates** listings using a composite key so the same product isn't counted twice
- Gracefully handles missing fields (falls back to blank instead of crashing)
- Exports results directly to a formatted Excel file (`Alibaba_Products.xlsx`)

## 🛠️ Tech Stack

- **Python 3**
- [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/) – HTML parsing
- [pandas](https://pypi.org/project/pandas/) – data handling & Excel export
- [openpyxl](https://pypi.org/project/openpyxl/) – Excel file writing engine (used by pandas)

## 📁 Project Structure

```
├── web_scrapper.py          # Main scraping script
├── Alibaba.html             # Saved search results page 1
├── Alibaba2.html             # Saved search results page 2
├── Alibaba3.html             # Saved search results page 3
└── Alibaba_Products.xlsx    # Output: cleaned product data
```

## ⚙️ How It Works

1. Loads each saved HTML file with BeautifulSoup.
2. Locates the product grid container (`organic-list app-organic-search-mb-20 viewtype-gallery`).
3. Loops through each product card inside the container and pulls out the relevant fields using their respective CSS classes.
4. Builds a de-duplication key from all extracted fields to skip repeat listings.
5. Stops once 100 unique products have been collected (across all files).
6. Saves everything into `Alibaba_Products.xlsx` using pandas.

## 🚀 Usage

1. Save the Alibaba search results pages you want to scrape as `.html` files (right-click → *Save Page As* → *Webpage, Complete*).
2. Update the `html_files` list in `web_scrapper.py` with the paths to your saved HTML files.
3. Install the required dependencies:
   ```bash
   pip install beautifulsoup4 pandas openpyxl
   ```
4. Run the script:
   ```bash
   python web_scrapper.py
   ```
5. Find your results in `Alibaba_Products.xlsx` in the same directory.

## 📊 Sample Output

| Product_Name | Product_Price | Product_Review | Seller_Name | Product_Description | Product_Image |
|---|---|---|---|---|---|
| Equantu Fashion Muslim Islamic Electronic Zikir Counter Smart Ring Watch... | PKR 5,624.74 | 4.4/5.0 (50 reviews) | Shenzhen Huagepeng Technology Co., Ltd. | Min. order: 10 pieces, Est. delivery by Jun 13 | ./Alibaba_files/... |
| Popular 2025 WiFi GPS Android Smart Watch 4G Global Net HD Big Screen... | PKR 12,880.64 | 4.7/5.0 (65) | Shenzhen Byco Tech Co., Ltd. | Min. order: 1 piece, Est. delivery by Jun 4 | ./Alibaba_files/... |

*(100 unique products in total, generated from real scraped data)*

## ⚠️ Notes & Limitations

- This scraper works on **locally saved HTML pages**, not live URLs — it does not send requests directly to Alibaba.com.
- CSS class names are specific to Alibaba's current page layout and may break if their site structure changes.
- Image paths point to local asset folders generated when saving the page (e.g., `Alibaba_files/`), not hosted URLs.
- Intended for educational and personal data-analysis purposes only. Please review [Alibaba's Terms of Service](https://rule.alibaba.com/rule/detail/2044.htm) before scraping or reusing site content, and always respect a website's `robots.txt` and usage policies.

## 👤 Author

**Qurssam Fatima**
GitHub: [@qurssamfatima-star](https://github.com/qurssamfatima-star)

## 📄 License

This project is open source and available for personal and educational use.
