import re
import sys
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import requests



q = requests.get("http://www.baidu.com",timeout=5)
m = re.search(r'STATUS OK',q.text)
if m:
    sys.exit()
else:
    driver = webdriver.Chrome()

    driver.get('http://210.29.79.141/')

    cmcc = driver.find_element_by_xpath('//*[@id="edit_body"]/div[2]/div[5]/span[3]/input')
    driver.execute_script("arguments[0].click();", cmcc)
    driver.find_element_by_xpath('//*[@id="edit_body"]/div[2]/div[2]/div/div[2]/div[1]/div/form/input[3]').send_keys('xxx')  # 在xxx处输入账号
    driver.find_element_by_xpath('//*[@id="edit_body"]/div[2]/div[2]/div/div[2]/div[1]/div/form/input[4]').send_keys('xxx')  # 在xxx处输入密码
    driver.find_element_by_xpath('//*[@id="edit_body"]/div[2]/div[2]/div/div[2]/div[1]/div/form/input[2]').send_keys(Keys.ENTER)
    time.sleep(2)
    driver.close()

# driver.find_element_by_xpath('//*[@id="edit_body"]/div/div[2]/form/input')
#
# inf = driver.find_element_by_xpath('//*[@id="edit_body"]/div/div[2]/form/input')
# content = inf.get_attribute('value')
# # print(content == '注  销')
# if content == '注  销':
#     driver.close()
# else:

