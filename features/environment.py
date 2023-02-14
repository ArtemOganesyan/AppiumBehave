import subprocess

from appium import webdriver
from appium.webdriver import appium_service
from appium.webdriver.appium_service import AppiumService
from selenium.webdriver.common.by import By

from config import get
from logger import get_logger

log = get_logger()


def before_all(context):
    # starting server, code is not working
    # default_port = get()['Server']['port']
    # default_host = get()['Server']['host']
    # service = AppiumService()
    # service.start(args=['--address', str(default_host), '-p', str(default_port)])


    # invoking driver
    dc = get()['Amazon_Pixel4']
    log.debug('invoking driver')
    context.driver = webdriver.Remote(get()['Resources']['Url'], desired_capabilities=dc)
    context.driver.implicitly_wait(3)


def after_all(context):
    log.debug('killing driver')
    context.driver.quit()
    # context.appium_service.stop()

