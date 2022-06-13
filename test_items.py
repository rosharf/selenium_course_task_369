from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_customer_should_see_add_to_basket_button_on_the_item_page(browser):
    browser.get(link)
    button = browser.find_elements(By.CSS_SELECTOR,'button.btn-add-to-basket')
    assert button, "'Add to basket' button is not presented at the item page"

