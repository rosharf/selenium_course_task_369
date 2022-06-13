from selenium.webdriver.common.by import By
#import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_customer_should_see_add_to_cart_button_on_the_item_page(browser):
    browser.get(link)
    #time.sleep(30)
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn-add-to-basket')
    assert button, print("\n'Add to basket' button is not presented at the item page")

