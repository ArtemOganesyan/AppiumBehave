import subprocess
import time

from appium.webdriver.common.appiumby import AppiumBy
from behave import *
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
def check_top_picks_under_199_image_visible(context):
    log.debug(f'{context.scenario} asserting top picks under 199 image visibility')
    visibility = context.home_screen.top_pics_image_199_is_visible()
    if visibility:
        assert True
    else:
        log.debug(f'{context.scenario} taking error screenshot')
        context.driver.save_screenshot(f'./screenshots/{context.scenario}.png')
        assert False
