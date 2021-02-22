from BaseApp import BasePage
from selenium.webdriver.common.by import By


class AppFollowLocators:
    LOCATOR_TRY_NOW_BUTTON = (By.XPATH, "/html/body/header/div/div/div/form/button[1]")
    LOCATOR_EMAIL_FIELD = (By.ID, "signup-payed-full_name")
    LOCATOR_FULLNAME_FIELD = (By.ID, "signup-payed-full_name")
    LOCATOR_COMPANY_FIELD = (By.ID, "signup-payed-company")
    LOCATOR_POSITION_DROPDOWN = (By.ID, "signup-payed-position")
    LOCATOR_SIGNUP_BUTTON = (By.ID, "payed-signup-button")
    LOCATOR_PRICING_TAB = (By.CLASS_NAME, "pricing-offers__tab pricing-offers__tab--inactive")


class UseElements(BasePage):

    def enter_email(self, word):
        enter_email = self.find_element(AppFollowLocators.LOCATOR_EMAIL_FIELD)
        enter_email.click()
        enter_email.send_keys(word)
        return enter_email

    def enter_fullname(self, word):
        enter_fullname = self.find_element(AppFollowLocators.LOCATOR_FULLNAME_FIELD)
        enter_fullname.click()
        enter_fullname.send_keys(word)
        return enter_fullname

    def enter_company(self, word):
        enter_company = self.find_element(AppFollowLocators.LOCATOR_COMPANY_FIELD)
        enter_company.click()
        enter_company.send_keys(word)
        return enter_company

    def choose_position(self):
        choose_position = self.find_element(AppFollowLocators.LOCATOR_POSITION_DROPDOWN)
        choose_position.click()
        choose_position.selectByValue("QA Engineer")
        return choose_position

    def click_on_create_account_button(self):
        return self.find_element(AppFollowLocators.LOCATOR_TRY_NOW_BUTTON, time=2).click()

    def click_on_submit_button(self):
        return self.find_element(AppFollowLocators.LOCATOR_SIGNUP_BUTTON, time=2).click()

    def click_assert_tab(self):
        return self.find_element(AppFollowLocators.LOCATOR_PRICING_TAB, time=2).click()
