from utilities import utility_methods
from appium.webdriver.common.appiumby import AppiumBy
from appium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By


class HomeScreen:
    button_english = (AppiumBy.ACCESSIBILITY_ID, "Select English")
    button_continue = (By.ID, "in.amazon.mShop.android.shopping:id/continue_button")
    # button_skip_sigin = (By.ID, "in.amazon.mShop.android.shopping: id / skip_sign_in_button")
    button_skip_signin = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().textContains("Skip sign in")')

    logo_home_screen = (By.ID, "in.amazon.mShop.android.shopping:id/chrome_action_bar_home_logo")
    header_pocket_friendly_stores = ('new UiSelector().text("Pocket friendly stores")')

    def __init__(self, driver):
        self.driver = driver

    def tap_button_english(self):
        utility_methods.wait_element_visibility(self.driver, 2, HomeScreen.button_english)
        utility_methods.tap_element(self.driver, utility_methods.find_element(self.driver, HomeScreen.button_english))

    def tap_button_continue(self):
        utility_methods.tap_element(self.driver, utility_methods.find_element(self.driver, HomeScreen.button_continue))

    def tap_button_skip_signin(self):
        utility_methods.wait_element_visibility(self.driver,2,HomeScreen.button_skip_signin)
        utility_methods.tap_element(self.driver,
                                    utility_methods.find_element(self.driver, HomeScreen.button_skip_signin))

    def home_logo_visible(self):
        utility_methods.wait_element_visibility(self.driver, 2, HomeScreen.logo_home_screen)
        visibility = utility_methods.el_is_visible(
            utility_methods.find_element(self.driver, HomeScreen.logo_home_screen))
        return visibility

    def scroll_to_down_to_text(self, header):
        pass

# try using
# class UI Selector: Resource ID, Text, Partial Text
# https://developer.android.com/reference/androidx/test/uiautomator/UiSelector

# driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("abc")')
# driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("abc")')
# driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("abc")')
