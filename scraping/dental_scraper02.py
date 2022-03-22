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

# 실습2 - 내가 한 코드
# AIA 생명 치아보험 견적 페이지에서 보장 내역과 보험료을 가져와서 출력을한다


def getAIAData(name, birth, gender):
    driver.get(
        'https://www.aia.co.kr/ko/our-products/medical-protection/non-par-denteal-health-plan.html#')
    if gender == 0:
        # 남자를 클릭하라
        maleButton = driver.find_element_by_xpath('//*[@id="calculator-container-form"]/div[1]/div[2]/div/div[1]/div/div[3]/div[1]/div[2]')
        maleButton.click()
    else:
        # 여자 버튼을 클릭하라
        felmaleButton = driver.find_element_by_xpath('//*[@id="calculator-container-form"]/div[1]/div[2]/div/div[1]/div/div[3]/div[1]/div[1]')
        felmaleButton.click()

    brthDt = driver.find_element_by_name('brthDt')
    brthDt.send_keys("19"+bityh)

    Button = driver.find_element_by_xpath('//*[@id="btn806817556"]')
    Button.click()

    
getAIAData("이름", "700101", 0)