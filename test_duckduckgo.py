from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def test_searching_in_duckduckgo():
    # Opening Chrome browser. The path to chromedriver
    # set automatically by the webdriver-manager library
    browser = Chrome(executable_path=ChromeDriverManager().install())

    # Opening duckduckgo website
    browser.get('https://duckduckgo.com/')

    # Finding the search bar 
    search_bar = browser.find_element_by_id('search_form_input_homepage')

    # Finding the search button (icon finder)
     search_button = browser.find_element_by_id('search_button_homepage')

     # Assertions that items are visible to the user
     assert search_bar.is_displayed() is True
     assert search_button.is_displayed() is True

     # Searching for Shiba Inu breed
     search_bar.send_keys('Shiba Inu')
     search_button.click()

     #Checking that any search result has a title "Shiba Inu"
      list = browser.find_elements_by_css_selector('.result__title')
      list_of_titles = []
      for i in list:
          list_of_titles.append(i.text)
     assert 'Shiba Inu - Wikipedia' in list_of_titles

     browser.quit()
