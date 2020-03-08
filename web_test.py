from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager



def test_my_first_chrome_selenium_test():
    # Opening Chrome browser. The path to chromedriver
    # set automatically by the webdriver-manager library
    browser = Chrome(executable_path=ChromeDriverManager().install())
    browser.maximize_window() 


    #Opening testarena website - the first use of Selenium API
    browser.get('http://demo.testarena.pl/zaloguj')

    # Verification that the title of the open page contains 'TestArena'
    assert 'TestArena' in browser.title

    # Closing the browser
    browser.quit()



def test_my_first_firefox_selenium_test():
    # Opening Firefox browser. The path to geckodriver (driver for Firefox)
    # set automatically by the webdriver-manager library  
    browser = Firefox(executable_path=GeckoDriverManager().install()) 
    browser.fullscreen_window()

    # Opening www.google.pl
    browser.get('https://www.google.pl')

    # Title verification
    assert 'Google' in browser.title
  

    # Closing the browser
    browser.quit()
