import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# WebDriverWait는 Selenium 2.4.0 이후 부터 사용 가능합니다.
from selenium.webdriver.support.ui import WebDriverWait
# expected_conditions는 Selenium 2.26.0 이후 부터 사용 가능합니다.
from selenium.webdriver.support import expected_conditions as EC

from time import sleep
import click

webdriver_path = os.environ['CHROME_DRIVER_PATH'] or '/Users/hanyoungjeong/Documents/workspace_example/inflearn_crawling/chromedriver'


def create_and_cli(name, cli):
    return 'mkdir {} && cd {} && {}'.format(name, name, cli)


def github_init_project(name):

    if os.environ['GITHUB_USERNAME'] and os.environ['GITHUB_PASSWORD']:
        username = os.environ['GITHUB_USERNAME']
        password = os.environ['GITHUB_PASSWORD']

        url = automation_with_selenium(name, username, password)

        os.system('cd {} && git init'.format(name))
        sleep(0.5)
        os.system('cd {} && git add .'.format(name))
        sleep(0.5)
        os.system('cd {} && git commit -m initialize project'.format(name))
        sleep(0.5)
        os.system('cd {} && git remote add origin {}'.format(name, url))
        sleep(0.5)
        os.system('cd {} && git push origin master'.format(name))

        return True
    else:
        click.echo('No credential exists..')
        return False


def automation_with_selenium(name, username, password):

    urlInput = ''
    driver = webdriver.Chrome(webdriver_path)

    # 웹 자원을 로드하기 위해 3초까지 기다린다.
    driver.implicitly_wait(3)

    driver.get('https://github.com/login')

    # Description
    # driver.find_element_by_name('repository[description]').send_keys('Hello~ Description')

    # print(driver.find_element_by_css_selector('button[type="submit"]'))
    # print(driver.find_element_by_selector('button[type="submit"]'))
    # print(driver.find_element_by_xpath(
    #     '//*[@id="new_repository"]/div[3]/button'))
    # print(driver.find_element_by_xpath(
    #     '//*[@id="new_repository"]/div[3]/button').text)

    try:
        driver.find_element_by_name('login').send_keys(username)
        driver.find_element_by_name('password').send_keys(password)

        driver.find_element_by_xpath(
            '//*[@id="login"]/form/div[3]/input[4]').click()

        driver.find_element_by_xpath(
            '/html/body/div[4]/div/aside[1]/div[2]/div[2]/div/h2/a').click()

        driver.find_element_by_name('repository[name]').send_keys(name)
        # WebDriverWait와 .until 옵션을 통해 우리가 찾고자 하는 HTML 요소를
        # 기다려 줄 수 있습니다.
        WebDriverWait(driver, 10) \
            .until(EC.presence_of_element_located((By.CSS_SELECTOR, "input.is-autocheck-successful")))

        driver.find_element_by_xpath(
            '//*[@id="new_repository"]/div[3]/button').send_keys(Keys.ENTER)

        # //*[@id="new_repository"]/div[3]/button
        urlInput = driver.find_element_by_xpath(
            '//*[@id="empty-setup-clone-url"]').get_attribute('value')
    finally:
        driver.quit()

    return urlInput
