from appium import webdriver
from behave import *
from pom.home_screen import HomeScreen
from logger import get_logger

log = get_logger()

@step('I tap button English')
def tap_button_english(context):
    context.home_screen = HomeScreen(context.driver)
    log.debug('taping on English button')
    context.home_screen.tap_button_english()


@step('I tap continue button')
def tap_continue_button(context):
    log.debug('taping on continue button')
    context.home_screen.tap_button_continue()

@step('then I scroll down to text "{header}"')
def scroll_down_to_text(context, header):
    pass


@step('I skip signin')
def skip_signin(context):
    log.debug('skipping signin')
    context.home_screen.tap_button_skip_signin()