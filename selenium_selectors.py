from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

driver.get("http://automationpractice.com/index.php")

## locate the elements
# logo
driver.find_elements_by_id("header_logo")
# cart
driver.find_elements_by_class_name("shopping_cart")
# email newsletter
driver.find_elements_by_id('newsletter-input')
# twitter
driver.find_elements_by_class_name('twitter')
# 'POPULAR'
driver.find_elements_by_class_name('homefeatured')
# Contact us
driver.find_elements_by_id('contact-link')

# CSS selectors
driver.find_elements_by_css_selector("#header_logo")
driver.find_elements_by_css_selector(".shopping_cart")
driver.find_elements_by_css_selector("#newsletter-input")
driver.find_elements_by_css_selector(".twitter")
driver.find_elements_by_css_selector(".homefeatured")
driver.find_elements_by_css_selector("#contact-link")

# Xpath selectors
driver.find_elements_by_xpath("//div[@id='header_logo']")
driver.find_elements_by_xpath("//div[@class='shopping_cart']")
driver.find_elements_by_xpath("//input[@id='newsletter-input']")
driver.find_elements_by_xpath("//li[@class='twitter']")
driver.find_elements_by_xpath("//a[@class='homefeatured']")
driver.find_elements_by_xpath("//div[@id='contact-link']")

driver.close()
driver.quit()




