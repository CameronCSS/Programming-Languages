# Added concurrent.futures parallel processing to take run time from 50 seconds down to 16 seconds.

import concurrent.futures
import time
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc


def scrape_website(url, word):
    options = uc.ChromeOptions()
    driver = uc.Chrome(options=options)
    driver.get(url)

    if "homedepot.com" in url:
        try:
            input_field = driver.find_element(By.ID, 'headerSearch')
        except NoSuchElementException:
            input_field = driver.find_element(By.CSS_SELECTOR, 'input[name="keyword"]')
            
        time.sleep(1)
        input_field.send_keys(word)
        input_field.send_keys(Keys.ENTER)

    elif "rcwilley.com" in url:
        input_field = driver.find_element(By.ID, 'searchBox')
        input_field.send_keys(word)
        submit_button = driver.find_element(By.ID, 'searchSubmit')
        submit_button.click()
        wait = WebDriverWait(driver, 10)
        try:
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'product-pod--s5vy1')))
        except TimeoutException:
            pass

    elif "lowes.com" in url:
        input_field = driver.find_element(By.ID, 'search-query')
        input_field.send_keys(word)
        submit_button = driver.find_element(By.CSS_SELECTOR, 'button.sb-search-icon')
        submit_button.click()

    elif "bestbuy.com" in url:
        input_field = driver.find_element(By.ID, 'gh-search-input')
        input_field.send_keys(word)
        submit_button = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="submit search"][class="header-search-button"]')
        time.sleep(1)
        submit_button.click()

    time.sleep(1)
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')
    items = []

    if "homedepot.com" in url:
        product_items = soup.find_all('div', attrs={'data-testid': 'product-pod', 'class': 'product-pod--s5vy1'})
        if not product_items:
            price_element = soup.find('div', class_='price')
            if price_element:
                price_text = price_element.text.strip()
                price_match = re.search(r'\d{1,3}(?:,\d{3})*(?:\.\d{2})?', price_text)
                if price_match:
                    price = float(price_match.group().replace(',', ''))
                    model_number = word
                    items.append({'price': price, 'model_number': model_number})
        else:
            item = product_items[0]
            price_element = item.find('div', class_='price')
            model_number_element = item.find('div', class_='product-identifier--bd1f5')
            if price_element and model_number_element:
                price_text = price_element.text.strip()
                price_match = re.search(r'\d{1,3}(?:,\d{3})*(?:\.\d{2})?', price_text)
                if price_match:
                    price = float(price_match.group().replace(',', ''))
                    model_number = model_number_element.text.strip().replace('Model# ', '')
                    if model_number.upper() == word:
                        items.append({'price': price, 'model_number': model_number})

    elif "rcwilley.com" in url:
        product_items = soup.find_all('div', class_='productContent')
        for item in product_items:
            price_element = item.find('span', class_='price')
            if price_element:
                product_link_element = item.find_parent('a')
                if product_link_element:
                    product_link = "https://www.rcwilley.com" + product_link_element.get('href')
                    model_match = re.search(r'(?<=/)\w+(?=/\d+)', product_link)
                    if model_match:
                        model_number = model_match.group()
                        price = price_element.text.strip()
                        if model_number.upper() == word:
                            items.append({'price': float(price.replace('$', '').replace(',', '')), 'model_number': model_number})

    elif "lowes.com" in url:
        product_items = soup.find_all('div', class_=lambda value: value and value.endswith('tile_group'))
        if not product_items:
            price_element = soup.find('span', class_='item-price-dollar')
            if price_element:
                price_text = price_element.text.strip().replace('$', '')
                price_match = re.search(r'\d+(?:\.\d+)?', price_text)
                if price_match:
                    price = float(price_match.group())
                    model_number = word
                    items.append({'price': price, 'model_number': word})
        else:
            item = product_items[0]
            model_element = item.find('div', class_='reglr-dv expand-specs-mdl-id')
            if model_element:
                model_number = model_element.find('span', class_='tooltip-custom').text.strip().replace('Model #', '')
                price_element = item.find('div', attrs={'data-selector': 'splp-prd-act-$'})
                if price_element:
                    price_text = price_element.get('aria-label')
                    price_match = re.search(r'\d+(?:\.\d+)?', price_text)
                    if price_match:
                        price = float(price_match.group())
                        if model_number.upper() == word:
                            items.append({'price': price, 'model_number': model_number})

    elif "bestbuy.com" in url:
        product_items = soup.find_all('div', class_='pricing-price')
        for item in product_items:
            price_element = item.find('span', attrs={'aria-hidden': 'true'})
            if price_element:
                price = price_element.text.strip()
                model_number_element = item.find_previous('span', class_='attribute-title', string='Model:')
                if model_number_element:
                    model_number = model_number_element.find_next('span', class_='sku-value').text.strip()
                    # Check if the model number matches the input word exactly
                    if model_number.upper() == word:
                        items.append({'price': float(price.replace('$', '').replace(',', '')), 'model_number': model_number})
                        break  # Exit the loop after finding the first price

    driver.quit()

    if not items:
        return None  # Return None if no items found
    else:
        return items


def compare_prices(word):
    website_urls = [
        'https://www.homedepot.com/',
        'https://www.rcwilley.com/',
        'https://www.lowes.com/',
        'https://www.bestbuy.com/'
    ]

    items_website1 = []
    items_website2 = []
    items_website3 = []
    items_website4 = []

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for url in website_urls:
            futures.append(executor.submit(scrape_website, url, word))

        for idx, future in enumerate(concurrent.futures.as_completed(futures)):
            items = future.result()
            if idx == 0:
                items_website1 = items
            elif idx == 1:
                items_website2 = items
            elif idx == 2:
                items_website3 = items
            elif idx == 3:
                items_website4 = items

    if not items_website1:
        print(f"Model #{word} not found on Home Depot.")
    else:
        if items_website1[0]['model_number'] == word:
            for item in items_website1:
                print(f"Model #: {item['model_number']}, Home Depot Price: ${item['price']:.2f}")

    if not items_website2:
        print(f"Model #{word} not found on RC Willey.")
    else:
        for item in items_website2:
            print(f"Model #: {item['model_number']}, RC Willey Price: ${item['price']:.2f}")

    if not items_website3:
        print(f"Model #{word} not found on Lowes.")
    else:
        for item in items_website3:
            print(f"Model #: {item['model_number']}, Lowes Price: ${item['price']:.2f}")

    if not items_website4:
        print(f"Model #{word} not found on Best Buy.")
    else:
        if items_website4[0]['model_number'] == word:
            for item in items_website4:
                print(f"Model #: {item['model_number']}, Best Buy Price: {item['price']}")


search_word = input("Enter Model #: ")
search_word = re.sub(r'\W+', '', search_word)  # Removes spaces and symbols from the input
compare_prices(search_word)

# Test model # WM3400CW
