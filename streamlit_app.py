import streamlit as st 
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

st.set_page_config(layout="wide")

st.sidebar.title('Montgomery County, MD')
input_sites = st.sidebar.text_input('"geographic id list" here:')
lista = input_sites.split(' ')

def main():

    
    st.write('You entered:', lista)

    # Initialize empty lists
    url_lista = []
    owner_name_list = [] 
    secondary_owner_name_list = []
    property_address_list = []
    owner_id_list = []
    ownership_percentage_list = []
    exemptions_list = []
    account_number_list = [] 
    state_code_list = []

    property_id_list = []
    geographic_id_list = []
    tax_office_list = []
    type_list = []
    legal_list = [] 
    property_use_list = []

    land_homesite_list = []
    land_non_homesite_list = []
    special_use_list = []
    total_land_list = []
    improvement_list = []
    improvement_non_live_list = []
    total_improvement_list = []
    market_value_list = []
    special_use2_list = []
    appraised_value_list = []
    value_limitation_list = []
    net_appraised_list = [] 

    driver = webdriver.Chrome() 

    for i in lista:
        url = 'https://mcad-tx.org/property-search'
        driver.get(url)
        time.sleep(2)
        driver.find_element('xpath','//*[@id="searchInput"]').send_keys(i)
        time.sleep(2)
        driver.find_element('xpath','//*[@id="searchInput"]').send_keys(Keys.ENTER)
        time.sleep(2)
        driver.find_element(By.CLASS_NAME, 'sc-hEsumM').click()
        time.sleep(5)
        # driver.find_element('xpath','//*[@id="root"]/div/div/div/div[1]/div[3]/div/div[2]/div[3]/div[2]/div[1]/div/div[2]/div[2]/div[4]/div[1]/div[2]/div/div/div[3]/a').click()

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        # Extract data from soup using class names
        url_lista.append(driver.current_url)
        first_group = soup.find_all(class_="sc-eopZyb gcOyaR")
        owner_name_list.append(first_group[0].text if first_group and first_group[0].text.strip() else 'Not found')
        secondary_owner_name_list.append(first_group[1].text if len(first_group) > 1 and first_group[1].text.strip() else 'Not found')
        property_address_list.append(first_group[2].text if len(first_group) > 2 and first_group[2].text.strip() else 'Not found')
        owner_id_list.append(first_group[3].text if len(first_group) > 3 and first_group[3].text.strip() else 'Not found')
        ownership_percentage_list.append(first_group[4].text if len(first_group) > 4 and first_group[4].text.strip() else 'Not found')
        exemptions_list.append(first_group[5].text if len(first_group) > 5 and first_group[5].text.strip() else 'Not found')
        account_number_list.append(first_group[6].text if len(first_group) > 6 and first_group[6].text.strip() else 'Not found')
        state_code_list.append(first_group[7].text if len(first_group) > 7 and first_group[7].text.strip() else 'Not found')

        second_group = soup.find_all(class_="sc-bYwvMP gBhcoQ")
        property_id_list.append(second_group[0].text if second_group and second_group[0].text.strip() else 'Not found')
        geographic_id_list.append(second_group[1].text if len(second_group) > 1 and second_group[1].text.strip() else 'Not found')
        tax_office_list.append(second_group[2].text if len(second_group) > 2 and second_group[2].text.strip() else 'Not found')
        type_list.append(second_group[3].text if len(second_group) > 3 and second_group[3].text.strip() else 'Not found')
        legal_list.append(second_group[4].text if len(second_group) > 4 and second_group[4].text.strip() else 'Not found')
        property_use_list.append(second_group[5].text if len(second_group) > 5 and second_group[5].text.strip() else 'Not found')

        third_group = soup.find_all(class_="sc-kqlzXE friqHl")
        land_homesite_list.append(third_group[0].text if third_group and third_group[0].text.strip() else 'Not found')
        land_non_homesite_list.append(third_group[1].text if len(third_group) > 1 and third_group[1].text.strip() else 'Not found')
        special_use_list.append(third_group[2].text if len(third_group) > 2 and third_group[2].text.strip() else 'Not found')
        total_land_list.append(third_group[3].text if len(third_group) > 3 and third_group[3].text.strip() else 'Not found')
        improvement_list.append(third_group[4].text if len(third_group) > 4 and third_group[4].text.strip() else 'Not found')
        improvement_non_live_list.append(third_group[5].text if len(third_group) > 5 and third_group[5].text.strip() else 'Not found')
        total_improvement_list.append(third_group[6].text if len(third_group) > 6 and third_group[6].text.strip() else 'Not found')
        market_value_list.append(third_group[7].text if len(third_group) > 7 and third_group[7].text.strip() else 'Not found')
        special_use2_list.append(third_group[8].text if len(third_group) > 8 and third_group[8].text.strip() else 'Not found')
        appraised_value_list.append(third_group[9].text if len(third_group) > 9 and third_group[9].text.strip() else 'Not found')
        value_limitation_list.append(third_group[10].text if len(third_group) > 10 and third_group[10].text.strip() else 'Not found')
        net_appraised_list.append(third_group[11].text if len(third_group) > 11 and third_group[11].text.strip() else 'Not found')








    driver.quit()

    data_dict = {
        # First group
        'link': url_lista,
        'owner_name_list': owner_name_list,
        'secondary_owner_name_list': secondary_owner_name_list,
        'property_address_list': property_address_list,
        'owner_id_list': owner_id_list,
        'ownership_percentage_list': ownership_percentage_list,
        'exemptions_list': exemptions_list,
        'account_number_list': account_number_list,
        'state_code_list': state_code_list,

        # Second group
        'property_id_list': property_id_list,
        'geographic_id_list': geographic_id_list,
        'tax_office_list': tax_office_list,
        'type_list': type_list,
        'legal_list': legal_list,
        'property_use_list': property_use_list,

        # Third group
        'land_homesite_list': land_homesite_list,
        'land_non_homesite_list': land_non_homesite_list,
        'special_use_list': special_use_list,
        'total_land_list': total_land_list,
        'improvement_list': improvement_list,
        'improvement_non_live_list': improvement_non_live_list,
        'total_improvement_list': total_improvement_list,
        'market_value_list': market_value_list,
        'special_use2_list': special_use2_list,
        'appraised_value_list': appraised_value_list,
        'value_limitation_list': value_limitation_list,
        'net_appraised_list': net_appraised_list
    }




    df = pd.DataFrame(data_dict)
    st.write(df)

if len(lista) >= 2:
    st.write(len(lista))
    main()

