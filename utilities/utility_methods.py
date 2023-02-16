import base64
import time

from appium.webdriver.extensions.android.gsm import GsmCallActions
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.appiumby import AppiumBy


def wait_element_visibility(driver, timeout, locator):
    wait = WebDriverWait(driver, timeout)
    wait.until(ec.visibility_of_element_located(locator))

def el_is_visible(element):
    return element.is_displayed()



def find_element(driver, locator):
    return driver.find_element(*locator)


def click_element(element):
    element.click()


def input_text(element, text):
    element.send_keys(text)


def get_text(element):
    return element.text


# appium special methods
def swipe_down_pixels(driver):
    driver.swipe(500, 1200, 500, 500, 1000)


def swipe_up_pixels(driver):
    driver.swipe(500, 1000, 500, 500, 1200)


def swipe_left_pixels(driver):
    driver.swipe(500, 1000, 500, 250, 1000)


def swipe_right_pixels(driver):
    driver.swipe(500, 1000, 750, 500, 1200)


def tap_element(driver, element):
    action = TouchAction(driver)
    action.tap(element).perform()


def long_press(driver, element):
    action = TouchAction(driver)
    action.long_press(element)


def drag_drop(driver, element1, element2, wait_ms):
    action = TouchAction(driver)
    action.press(element1).wait(wait_ms).move_to(element2).perform().release()


def switch_to_activity(driver, pacakge, activity):
    driver.start_activity(pacakge,activity)



# Ui Selector Class methods
def scroll_to_element(driver, ui_sel_short_locator):
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                        f'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView({ui_sel_short_locator}.instance(0))')

def scroll_long_to_element(driver, ui_sel_short_locator, max_swipes):
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                        f'new UiScrollable(new UiSelector().scrollable(true).instance(0)).setMaxSearchSwipes({max_swipes})scrollIntoView({ui_sel_short_locator}.instance(0))')


def scroll_to_element_horizontal(driver, ui_sel_short_locator):
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                        f'new UiScrollable(new UiSelector().scrollable(true).instance(0)).setAsHorizontalList().scrollIntoView({ui_sel_short_locator}.instance(0))')


def scroll_to_element_vertical(driver, ui_sel_short_locator):
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                        f'new UiScrollable(new UiSelector().scrollable(true).instance(0)).setAsVerticalList().scrollIntoView({ui_sel_short_locator}.instance(0))')


# check if needed
def swipe_to_element(driver, ui_sel_short_locator):
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                        f'new UiScrollable(new UiSelector().scrollable(true).setAsVerticalList().scrollIntoView({ui_sel_short_locator}.instance(0))')


# Native Keyboard Events
def hide(driver):
    driver.hide_keyboard()


def enter(driver):
    driver.press_keycode(66)


def back(driver):
    driver.press_key_code(4)

# Sending pictures to device
# Not tested
def push_file(content, file_name, driver):
    dest_path = f'/data/local/tmp/{file_name}'
    data = bytes(content, 'utf-8')
    driver.push_file(dest_path, base64.b64encode(data).decode('utf-8'))


# Interruptions

def get_incoming_call(driver):
    driver.make_gsm_call('3233336832', GsmCallActions.CALL)
    time.sleep(2)


def accept_incoming_call(driver):
    driver.make_gsm_call('3233336832', GsmCallActions.ACCEPT)
    time.sleep(2)

def cancel_incoming_call(driver):
    driver.make_gsm_call('3233336832', GsmCallActions.CANCEL)
    time.sleep(2)


    # dest_path = '/data/local/tmp/test_push_file.txt'
    # data = bytes('This is the contents of the file to push to the device.', 'utf-8')
    # self.driver.push_file(dest_path, base64.b64encode(data).decode('utf-8'))