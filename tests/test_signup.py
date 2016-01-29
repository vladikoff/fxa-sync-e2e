import unittest
import page
import random

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

firefox_capabilities = DesiredCapabilities.FIREFOX
# Disable for now, https://github.com/jgraham/wires/issues/46
#firefox_capabilities['marionette'] = True
#firefox_capabilities['binary'] = '/Users/vladikoff/mozilla/mercurial/fx-team/objdir-frontend/dist/Nightly.app/Contents/MacOS/firefox'


from selenium import webdriver

fp = webdriver.FirefoxProfile()

fp.set_preference("browser.download.folderList",2)


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(capabilities=firefox_capabilities)
        self.driver.implicitly_wait(20)  # seconds

    def test_search_in_python_org(self):
        email = "fxatester" + str(random.random()) + "@restmail.net"

        self.driver.get("about:preferences#sync")
        elem = self.driver.find_element_by_css_selector("#noFxaSignUp")

        elem.click()

        self.driver.find_element_by_css_selector("#remote")
        self.driver.switch_to.frame("remote")

        fxa_page = page.FxaPage(self.driver)
        fxa_page.fill_out_signup(email)
        fxa_page.verify_account(email)

        self.driver.get("about:preferences#sync")

        el_pref_email = self.driver.find_element_by_css_selector("#fxaEmailAddress1")
        self.assertEqual(el_pref_email.text, email)

        # Find the 'Disconnect', that means we connected.
        self.driver.find_element_by_css_selector("#fxaUnlinkButton")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
