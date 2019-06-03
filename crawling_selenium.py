from selenium import webdriver

driver = webdriver.Chrome(
    '/Users/hanyoungjeong/Documents/workspace_example/inflearn_crawling/chromedriver')

# 웹 자원을 로드하기 위해 3초까지 기다린다.
driver.implicitly_wait(3)

driver.get('https://github.com/login')

driver.find_element_by_name('login').send_keys('8735132@naver.com')
driver.find_element_by_name('password').send_keys('Jhy5968!@#')

driver.find_element_by_xpath('//*[@id="login"]/form/div[3]/input[4]').click()

driver.find_element_by_xpath(
    '/html/body/div[4]/div/aside[1]/div[2]/div[2]/div/h2/a').click()

driver.find_element_by_name('repository[name]').send_keys('hello_world~')
driver.find_element_by_name(
    'repository[description]').send_keys('Hello~ Description')

# print(driver.find_element_by_css_selector('button[type="submit"]'))
# print(driver.find_element_by_selector('button[type="submit"]'))
driver.find_element_by_xpath('//*[@id="new_repository"]/div[3]/button').click()

urlInput = driver.find_element_by_xpath(
    '//*[@id="empty-setup-clone-url"]').get_attribute('value')
