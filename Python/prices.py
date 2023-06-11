import streamlit as st
from datetime import date
from openpyxl import Workbook
from scraper import compare_prices  # Assuming the scraping function is in a separate file "scraper.py"

def save_to_excel(prices, search_word):
    filename = 'prices.xlsx'
    file_exists = os.path.exists(filename)

    wb = Workbook()

    # First sheet
    sheet1 = wb.active
    sheet1.title = 'Item Prices'
    if not file_exists:
        sheet1.append(['Website', 'Item', 'Name', 'Price', 'Date Added'])
    current_date = date.today().strftime('%m/%d/%Y')
    for item in prices:
        sheet1.append([item['website'], search_word, item['name'], item['price'], current_date])

    # Second sheet
    sheet2 = wb.create_sheet(title='Compared')
    if not file_exists:
        sheet2.append(['Item', 'Avg Price 1', 'Avg Price 2', 'Price Difference', 'Date Added'])
    current_date = date.today().strftime('%m/%d/%Y')
    sheet2.append([search_word, prices[0]['avg_price'], prices[1]['avg_price'], prices[0]['price_diff'], current_date])

    wb.save(filename)

def main():
    st.title("Price Comparison App")

    search_word = st.text_input("Enter word to search:")
    if st.button("Compare Prices"):
        prices = compare_prices(search_word)
        save_to_excel(prices, search_word)
        st.subheader(f"Search Results for '{search_word}':")
        for item in prices:
            st.write(f"Name: {item['name']}")
            st.write(f"Price: {item['price']}")
            st.write(f"Website: {item['website']}")
            st.write("---")
        st.success("Data saved to Excel file.")

if __name__ == '__main__':
    main()
