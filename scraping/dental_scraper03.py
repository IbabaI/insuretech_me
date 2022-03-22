from operator import ge
from selenium import webdriver
import re

driver = webdriver.Chrome('./chromedriver')


def rePlaceData(value):
    numbers = re.findall("\d+", value)
    result = ""
    for i in numbers:
        decodedNumber = i
        result += decodedNumber
    return result

# 실습2 - lina 내가 실습
# AIA 생명 치아보험 견적 페이지에서 보장 내역과 보험료을 가져와서 출력을한다

birthInput = driver.find_element_by_xpath('//*[@id="birthday"]')
birthInput.send_keys(birth)

def getAIAData(name, birth, gender):
    driver.get('https://direct.lina.co.kr/product/ess/dtc01/easy')

    if gender == 0:
        # 남자를 클릭하라
        maleButton = driver.find_element_by_xpath(
            '//*[@id="main_btn_male"]')
        maleButton.click()
    else:
        # 여자 버튼을 클릭하라
        femaleButton = driver.find_element_by_xpath(
            '//*[@id="main_btn_female"]')
        femaleButton.click()
        

# 여기에 작성


    confirmButton = driver.find_element_by_xpath('//*[@id="btn_direct_dental_cal"]')
    confirmButton.click()


getAIAData("이름", "700101", 0)