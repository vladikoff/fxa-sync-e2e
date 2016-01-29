import helpers
from locators import FxaPageLocators

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class FxaPage(BasePage):
    def fill_out_signup(self, email, password='password'):
        """
        Fill out FxA Sign up

        :param email:
        :param password:
        :return:
        """
        element = self.driver.find_element(*FxaPageLocators.INPUT_EMAIL)
        element.send_keys(email)

        el_pass = self.driver.find_element(*FxaPageLocators.INPUT_PASSWORD)
        el_pass.send_keys(password)

        el_age = self.driver.find_element(*FxaPageLocators.INPUT_AGE)
        el_age.send_keys("2")
        el_age.send_keys("4")

        el_submit = self.driver.find_element(*FxaPageLocators.BUTTON_SUBMIT)
        el_submit.click()

        self.driver.find_element(*FxaPageLocators.HEADER_CONFIRM_EMAIL)

    def verify_account(self, email):
        """
        Verify account by opening the verification link

        :param email:
        :return:
        """
        link = helpers.get_verification_link(email)

        # At this time we cannot open a new Selenium window
        # because Marionette cannot run `execute_script`
        # https://bugzilla.mozilla.org/show_bug.cgi?id=1123506
        # We just paste the link on top of the existing tab
        self.driver.get(link)
        self.driver.find_element(*FxaPageLocators.HEADER_VERIFIED_EMAIL)