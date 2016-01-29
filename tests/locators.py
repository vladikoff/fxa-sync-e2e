from selenium.webdriver.common.by import By

class FxaPageLocators(object):
    """
    A class for main page locators. All main page locators should come here
    """
    INPUT_EMAIL = (By.CSS_SELECTOR, '.email')
    INPUT_PASSWORD = (By.CSS_SELECTOR, '.password')
    INPUT_AGE = (By.CSS_SELECTOR, '#age')
    BUTTON_SUBMIT = (By.CSS_SELECTOR, '#submit-btn')
    HEADER_CONFIRM_EMAIL = (By.CSS_SELECTOR, '#fxa-confirm-header')
    HEADER_VERIFIED_EMAIL = (By.CSS_SELECTOR, '#fxa-sign-up-complete-header')

    # Firefox about:prefs items
    BUTTON_UNLINK = (By.CSS_SELECTOR, '#fxaUnlinkButton')
    BUTTON_MANAGE = (By.CSS_SELECTOR, '#verifiedManage')
