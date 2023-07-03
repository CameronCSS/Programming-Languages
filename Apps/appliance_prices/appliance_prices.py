# Added concurrent.futures parallel processing to take run time from 50 seconds down to 16 seconds.

import concurrent.futures

from flask import Flask, render_template, request
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

app = Flask(__name__, template_folder='.')

def scrape_website(url, word):
    options = uc.ChromeOptions()
    options.add_argument('--headless')
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
        model_number_element = soup.find('div', class_='product-identifier--bd1f5')
        if not model_number_element:
            price_element = soup.find('div', class_='price')
            if price_element:
                price_text = price_element.text.strip()
                price_text = re.sub(r'\D', '', price_text)
                price_text = price_text[:-2] + '.' + price_text[-2:]
                price = float(price_text)
                model_number = word.upper()
                items.append({'price': price, 'model_number': model_number})
        else:
            price_element = soup.find('div', class_='price')
            if price_element:
                price_text = price_element.text.strip()
                price_text = re.sub(r'\D', '', price_text)
                price_text = price_text[:-2] + '.' + price_text[-2:]
                price = float(price_text)
                model_number = model_number_element.text.strip().replace('Model# ', '')
                if model_number.upper() == word.upper():
                    items.append({'price': price, 'model_number': model_number})


    elif "rcwilley.com" in url:
        product_items = soup.find_all('div', class_='productContent')
        for item in product_items:
            price_element = item.find('span', class_='price')
            if price_element:
                product_link_element = item.find_parent('a')
                if product_link_element:
                    product_link = product_link_element.get('href')
                    print(product_link)
                    model_match = re.search(r'/([^/]+)/\d+/', product_link)
                    if model_match:
                        model_number = model_match.group(1)
                        price = price_element.text.strip()
                        if model_number.replace('-', '').upper() == word.upper():
                            items.append({'price': float(price.replace('$', '').replace(',', '')), 'model_number': model_number})


    elif "lowes.com" in url:
        product_items = soup.find_all('div', class_=lambda value: value and value.endswith('tile_group'))
        if not product_items:
            price_element = soup.find('span', class_='item-price-dollar')
            if price_element:
                price_text = price_element.text.strip().replace('$', '')
                price_match = re.search(r'\d+(?:,\d+)*(?:\.\d+)?', price_text)
                if price_match:
                    price = float(price_match.group().replace(',', ''))
                    model_number = word.upper()
                    image_url = ''
                    items.append({'price': price, 'model_number': word, 'image_url': image_url})
        else:
            item = product_items[0]
            model_element = item.find('div', class_='reglr-dv expand-specs-mdl-id')
            if model_element:
                model_number = model_element.find('span', class_='tooltip-custom').text.strip().replace('Model #', '')
                price_element = item.find('div', attrs={'data-selector': 'splp-prd-act-$'})
                if price_element:
                    price_text = price_element.get('aria-label')
                    price_match = re.search(r'\d+(?:,\d+)*(?:\.\d+)?', price_text)
                    if price_match:
                        price = float(price_match.group().replace(',', ''))
                        if model_number.upper() == word.upper():
                            image_url = ''
                            items.append({'price': price, 'model_number': model_number, 'image_url': image_url})


    elif "bestbuy.com" in url:
        product_items = soup.find_all('div', class_='pricing-price')
        for item in product_items:
            price_element = item.find('span', attrs={'aria-hidden': 'true'})
            if price_element:
                price = price_element.text.strip()
                model_number_element = item.find_previous('span', class_='attribute-title', string='Model:')
                if model_number_element:
                    model_number = model_number_element.find_next('span', class_='sku-value').text.strip()
                    
                    # Remove "/AA" suffix from model number if present
                    if model_number.upper().endswith('/AA'):
                        model_number = model_number[:-3]
                    
                    if model_number.upper() == word.upper():
                        image_url = ''
                        items.append({'price': float(price.replace('$', '').replace(',', '')), 'model_number': model_number})
                        break


    driver.quit()

    if not items:
        return None
    else:
        return items
    
def get_image_url_rcwilley(url, word):
    options = uc.ChromeOptions()
    options.add_argument('--headless')
    driver = uc.Chrome(options=options)
    driver.get(url)

    if "rcwilley.com" in url:
        input_field = driver.find_element(By.ID, 'searchBox')
        input_field.send_keys(word)
        submit_button = driver.find_element(By.ID, 'searchSubmit')
        submit_button.click()
        wait = WebDriverWait(driver, 10)
        try:
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'product-pod--s5vy1')))
        except TimeoutException:
            pass

    results = []

    if "rcwilley.com" in url:
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')
        product_items = soup.find_all('div', class_='productContent')
        
        if product_items:
            for item in product_items:
                price_element = item.find('span', class_='price')
                if price_element:
                    product_link_element = item.find_parent('a')
                    if product_link_element:
                        product_link = product_link_element.get('href')
                        model_match = re.search(r'/([^/]+)/\d+/', product_link)
                        if model_match:
                            model_number = model_match.group(1)
                            if model_number.replace('-', '').upper() == word.upper():
                                image_element = item.find_previous_sibling('div', class_=re.compile(r'^productImage'))
                                if image_element:
                                    image_url = image_element.find('img')['src']
                                    results.append({'image_url': image_url})
                                else:
                                    results.append({'image_url': 'No Product Image'})


    driver.quit()
    return results



def compare_prices(word):
    website_urls = [
        'https://www.homedepot.com/',
        'https://www.lowes.com/',
        'https://www.bestbuy.com/',
        'https://www.rcwilley.com/'
    ]

    website_names = {
        'https://www.homedepot.com/': 'Home Depot',
        'https://www.lowes.com/': 'Lowes',
        'https://www.bestbuy.com/': 'Best Buy',
        'https://www.rcwilley.com/': 'RC Willey'
    }

    results = []

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        image_url_futures = {}
        price_futures = {}

        for url in website_urls:
            if "rcwilley.com" in url:
                image_url_futures[url] = executor.submit(get_image_url_rcwilley, url, word)
                price_futures[url] = executor.submit(scrape_website, url, word)
            else:
                future = executor.submit(scrape_website, url, word)
                futures.append((future, url))

        for future, website_url in futures:
            items_list = future.result()
            print(f"Scraped items from {website_url}: {items_list}")
            if items_list:
                for item in items_list:
                    item['website'] = website_names[website_url]
                    price = item.get('price')
                    if price is not None:
                        price = "${:.2f}".format(price)
                    else:
                        price = 'N/A'
                    results.append({
                        'model_number': word,
                        'price': price,
                        'website': item['website'],
                    })
            else:
                results.append({
                    'model_number': word,
                    'price': 'N/A',
                    'website': website_names[website_url],
                })

        for website_url, price_future in price_futures.items():
            price_data = price_future.result()
            print(f"Price data from {website_url}: {price_data}")
            if price_data:
                for item in price_data:
                    item['website'] = website_names[website_url]
                    price = item.get('price')
                    if price is not None:
                        price = "${:.2f}".format(price)
                    else:
                        price = 'N/A'
                    results.append({
                        'model_number': item['model_number'],
                        'price': price,
                        'website': item['website'],
                    })
            else:
                results.append({
                    'model_number': word,
                    'price': 'N/A',
                    'website': website_names[website_url],
                })

        for website_url, image_url_future in image_url_futures.items():
            image_url = image_url_future.result()
            print(f"Image URL from {website_url}: {image_url}")
            if image_url:
                matching_results = [item for item in results if item['website'] == website_names[website_url] and item['model_number'] == word]
                if matching_results:
                    for item in matching_results:
                        item['image_url'] = image_url
            else:
                matching_results = [item for item in results if item['website'] == website_names[website_url] and item['model_number'] == word]
                if matching_results:
                    for item in matching_results:
                        item['image_url'] = 'No Product Image'


    return results


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compare', methods=['POST'])
def compare():
    search_word = request.form['search_word']
    search_word = re.sub(r'\W+', '', search_word)
    results_data = compare_prices(search_word)

    results = []
    image_url = None

    for item in results_data:
        model_number = item['model_number']
        price = item.get('price', 'N/A')
        website = item['website']
        if 'image_url' in item:
            image_url = item['image_url']
        results.append({'model_number': model_number, 'price': price, 'website': website})

    return render_template('results.html', results=results, image_url=image_url)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)