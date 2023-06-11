import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from datetime import date

def scrape_website(url, word):
    driver = webdriver.Chrome()
    driver.get(url)

    if "livingspaces.com" in url:
        input_field = driver.find_element(By.ID, 'search')
        input_field.send_keys(word)
        form = input_field.find_element(By.XPATH, './ancestor::form')
        form.submit()
    elif "rcwilley.com" in url:
        input_field = driver.find_element(By.ID, 'searchBox')
        input_field.send_keys(word)
        submit_button = driver.find_element(By.ID, 'searchSubmit')
        submit_button.click()

    time.sleep(5)  
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')
    prices = []

    if "livingspaces.com" in url:
        product_items = soup.find_all('div', class_='product-item-container')
        for item in product_items:
            name_element = item.find('span', class_='name')
            price_element = item.find('span', class_='price')
            if name_element and price_element:
                name = name_element.text.strip()
                price = price_element.text.strip()
                prices.append({'name': name, 'price': float(price.replace('$', '').replace(',', ''))})

    elif "rcwilley.com" in url:
        product_items = soup.find_all('div', class_='productContent')
        for item in product_items:
            name_element = item.find('div', class_='productName')
            price_element = item.find('span', class_='price')
            if name_element and price_element:
                name = name_element.text.strip()
                price = price_element.text.strip()
                prices.append({'name': name, 'price': float(price.replace('$', '').replace(',', ''))})

    driver.quit()

    return prices

def calculate_average(prices):
    prices_float = [price['price'] for price in prices]
    average = sum(prices_float) / len(prices_float) if prices_float else 0
    rounded_average = round(average, 2)
    return rounded_average

def get_min_max(prices):
    if not prices:
        return None, None
    min_price = min(prices, key=lambda x: x['price'])
    max_price = max(prices, key=lambda x: x['price'])
    return min_price, max_price

def compare_prices(word):
    website1_url = 'https://www.livingspaces.com/'
    website2_url = 'https://www.rcwilley.com/'

    prices_website1 = scrape_website(website1_url, word)
    prices_website2 = scrape_website(website2_url, word)

    average_website1 = calculate_average(prices_website1)
    average_website2 = calculate_average(prices_website2)

    rounded_average_website1 = round(average_website1, 2)
    rounded_average_website2 = round(average_website2, 2)

    website1_name = website1_url.replace('https://www.', '').replace('.com/', '').capitalize()
    website2_name = website2_url.replace('https://www.', '').replace('.com/', '').capitalize()

    print(f"Item: {search_word}")
    print()

    # To print a list of all items on the first page.

    # print(f"Average price on {website1_name}: ${average_website1:.2f}")
    # for item in prices_website1:
    #     print(f"Name: {item['name']}, Price: {item['price']}")

    # print(f"\nAverage price on {website2_name}: ${average_website2:.2f}")
    # for item in prices_website2:
    #     print(f"Name: {item['name']}, Price: {item['price']}")

    print(f"Number of {word}s on {website1_name} front page: {len(prices_website1)}")
    print(f"Average price on {website1_name}: ${average_website1:.2f}")
    min_price, max_price = get_min_max(prices_website1)
    if min_price and max_price:
        print(f"Lowest price on {website1_name}: {min_price['name']} at ${min_price['price']:.2f}")
        print(f"Highest price on {website1_name}: {max_price['name']} at ${max_price['price']:.2f}")

    print(f"\nNumber of {word}s on {website2_name} front page: {len(prices_website2)}")
    print(f"Average price on {website2_name}: ${average_website2:.2f}")
    min_price, max_price = get_min_max(prices_website2)
    if min_price and max_price:
        print(f"Lowest price on {website2_name}: {min_price['name']} at ${min_price['price']:.2f}")
        print(f"Highest price on {website2_name}: {max_price['name']} at ${max_price['price']:.2f}")

    price_diff = abs(average_website1 - average_website2)
    print(f"\nPrice Comparison: {website1_name} is {'cheaper' if average_website1 < average_website2 else 'more expensive' if average_website1 > average_website2 else 'equally priced'} than {website2_name} by ${price_diff:.2f}")



search_word = input("Enter word to search: ")
compare_prices(search_word)
