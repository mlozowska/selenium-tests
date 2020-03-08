from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager




# Verifying that the number of subtitles presented on Wikipedia is equal 10
def test_titles_count():
    browser = Chrome(executable_path=ChromeDriverManager().install())

    browser.get('https://en.wikipedia.org/wiki/Shiba_Inu')
    list_of_titles = browser.find_elements_by_css_selector('.mw-headline')

    assert len(list_of_titles) == 10

    browser.quit()

    
    
# Verifying that after searching for the word 'Hokkaido'
# the list of presented subtitles is equal 31
def test_titles_count_after_search():
    browser = Chrome(executable_path=ChromeDriverManager().install())
    browser.get('https://en.wikipedia.org/wiki/Shiba_Inu')

    search_bar = browser.find_element_by_id('searchInput')
    search_button = browser.find_element_by_id('searchButton')

    assert search_bar.is_displayed() is True
    assert search_button.is_displayed() is True

    search_bar.send_keys('Hokkaido')
    search_button.click()

    list_of_Hokkaido_titles = browser.find_elements_by_css_selector('.mw-headline')

    assert len(list_of_Hokkaido_titles) == 31

    browser.quit()

# Verifying that there is only one post when you click
# in References subtitle on the label "Dog Owners Guide: Shiba Inu'

def test_post_count_on_the_label():
    browser = Chrome(executable_path=ChromeDriverManager().install())
    browser.get('https://en.wikipedia.org/wiki/Shiba_Inu')

    label = browser.find_element_by_class_name("external.text")
    label.click()

    title = browser.find_elements_by_css_selector('h1')

    assert len(title) == 1

    browser.quit()
