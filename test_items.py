link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_customer_should_see_add_to_basket_button_on_the_item_page(browser):
    browser.get(link)
    button = browser.find_elements_by_css_selector('button.btn-add-to-basket')
    assert button, "\n'Add to basket' button is not presented at the item page"

