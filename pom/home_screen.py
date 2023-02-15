import time

from utilities import utility_methods
from appium.webdriver.common.appiumby import AppiumBy
from appium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By


class HomeScreen:
    button_english = (AppiumBy.ACCESSIBILITY_ID, "Select English")
    button_continue = (By.ID, "in.amazon.mShop.android.shopping:id/continue_button")
    button_skip_signin = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Skip sign in")')
    logo_home_screen = (By.ID, "in.amazon.mShop.android.shopping:id/chrome_action_bar_home_logo")
    header_pocket_friendly_stores = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Pocket friendly stores")')

    text_top_picks_199 = (AppiumBy.ANDROID_UIAUTOMATOR, 'new Ui Selector().text("Top picks under ₹199")')
    text_top_picks_299 = (AppiumBy.ANDROID_UIAUTOMATOR, 'new Ui Selector().text("Top picks under ₹299")')
    text_top_picks_399 = (AppiumBy.ANDROID_UIAUTOMATOR, 'new Ui Selector().text("Top picks under ₹399")')
    text_top_picks_499 = (AppiumBy.ANDROID_UIAUTOMATOR, 'new Ui Selector().text("Top picks under ₹499")')

    image_top_pics_199 = (By.XPATH, '//android.view.View[@content-desc="Top picks under ₹199 Top picks under ₹199"]/android.widget.Image')



    def __init__(self, driver):
        self.driver = driver

    def tap_button_english(self):
        utility_methods.wait_element_visibility(self.driver, 5, HomeScreen.button_english)
        utility_methods.tap_element(self.driver, utility_methods.find_element(self.driver, HomeScreen.button_english))

    def tap_button_continue(self):
        utility_methods.tap_element(self.driver, utility_methods.find_element(self.driver, HomeScreen.button_continue))

    def tap_button_skip_signin(self):
        utility_methods.wait_element_visibility(self.driver, 2, HomeScreen.button_skip_signin)
        utility_methods.tap_element(self.driver,
                                    utility_methods.find_element(self.driver, HomeScreen.button_skip_signin))

    def home_logo_visible(self):
        utility_methods.wait_element_visibility(self.driver, 2, HomeScreen.logo_home_screen)
        visibility = utility_methods.el_is_visible(
            utility_methods.find_element(self.driver, HomeScreen.logo_home_screen))
        return visibility

    def scroll_to_down_to_header_pocket_friendly_stores(self):
        # passing locator w/o location strategy
        utility_methods.scroll_to_element(self.driver, HomeScreen.header_pocket_friendly_stores[1])

    def top_pics_image_199_is_visible(self):
        visibility = utility_methods.el_is_visible(utility_methods.find_element(self.driver, HomeScreen.image_top_pics_199))
        return visibility

# try using
# class UI Selector: Resource ID, Text, Partial Text
# https://developer.android.com/reference/androidx/test/uiautomator/UiSelector

# driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("abc")')
# driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("abc")')
# driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("abc")')
