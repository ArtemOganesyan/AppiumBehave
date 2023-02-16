import subprocess
import time

from appium.webdriver.common.appiumby import AppiumBy
from behave import *

import utilities.utility_methods
from pom.home_screen import HomeScreen
from logger import get_logger

log = get_logger()


@step('I tap button English')
def tap_button_english(context):
    context.home_screen = HomeScreen(context.driver)
    log.debug(f'{context.scenario} taping on English button')
    context.home_screen.tap_button_english()


@step('I tap continue button')
def tap_continue_button(context):
    log.debug(f'{context.scenario} taping on continue button')
    context.home_screen.tap_button_continue()


@step('I skip signin')
def skip_signin(context):
    log.debug(f'{context.scenario} skipping signin')
    context.home_screen.tap_button_skip_signin()


@step('I see amazon logo')
def check_amazon_logo_visibility(context):
    log.debug(f'{context.scenario}asserting amazon logo visibility')
    assert context.home_screen.home_logo_visible()


@step('I scroll down to Pocket friendly stores on Home Screen')
def scroll_down_to_header_home_screen(context):
    log.debug(f'{context.scenario}scrolling to Pocket friendly stores')
    context.home_screen.scroll_to_down_to_header_pocket_friendly_stores()


@step('I see top picks under 199 image')
def assert_top_picks_under_199_image_visible(context):
    log.debug(f'{context.scenario} asserting top picks under 199 image visibility')
    visibility = context.home_screen.top_pics_image_199_is_visible()
    if visibility:
        assert True
    else:
        log.debug(f'{context.scenario} taking error screenshot')
        context.driver.save_screenshot(f'./screenshots/{context.scenario}.png')
        assert False


@step('I receive incoming call')
def get_incoming_call(context):
    log.debug('simulating incoming call')
    utilities.utility_methods.get_incoming_call(context.driver)


@step('I accept incoming call')
def accept_incoming_call(context):
    log.debug('accepting incoming call')
    utilities.utility_methods.accept_incoming_call(context.driver)


@step('I cancel incoming call')
def cancel_incoming_call(context):
    log.debug('canceling incoming call')
    utilities.utility_methods.cancel_incoming_call(context.driver)
    time.sleep(5)


@step('I input "{query}" into search field on Home Screen')
def input_text_into_search_field(context, query):
    log.debug('inputting query into search field')
    context.home_screen.input_text_into_search_field(query)


@step('I hit enter key')
def hit_enter_key(context):
    log.debug('hitting enter key')
    utilities.utility_methods.enter(context.driver)


@step('I tap navi burger')
def tap_burger(context):
    log.debug('tapping burger')
    context.home_screen.tap_navi_burger()


@step('I see "{expected_text}" in side menu header')
def assert_side_menu_header_text(context, expected_text):
    log.debug('asserting text in side menu header')
    actual_text = context.home_screen.get_side_menu_header_text()
    if actual_text == expected_text:
        assert True
    else:
        log.debug(f'{context.scenario} taking error screenshot')
        context.driver.save_screenshot(f'./screenshots/{context.scenario}.png')
        assert False
