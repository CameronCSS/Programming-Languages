import streamlit as st
from datetime import date
from scraper import compare_prices
import subprocess

def main():
    st.title("Price Comparison App")

    search_word = st.text_input("Enter word to search:")
    if st.button("Compare Prices"):
        subprocess.run(['pip', 'install', 'openpyxl'])  # Install openpyxl package
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
