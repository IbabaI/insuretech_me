from selenium import webdriver
from selenium.webdriver.support.ui import Select
# 내가 작성한 코드
# SELECT 엘리먼트를 위한 라이브러리 로드
driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.choongang.co.kr/html/sub06_06_n.php")

titleButton = driver.find_element_by_xpath(
    '//*[@id="hpt_body_conti"]/div/div[2]/div/div[2]/div/div/div/table[1]/tbody/tr[1]/td[2]/a')
titleButton.click()

tableBody = driver.find_element_by_xpath('//*[@id="hpt_body_conti"]/div/div[2]/div/div/div/div/div[1]/table')
rowInTable = tableBody.find_elements_by_xpath('tbody')
for index, row in enumerate(rowInTable):
    print(index + 1)
    titleAndSinger = row.find_elements_by_tag_name('tr')
    print(titleAndSinger.text)