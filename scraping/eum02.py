from selenium import webdriver
from selenium.webdriver.support.ui import Select
# 내가 작성한 코드
# SELECT 엘리먼트를 위한 라이브러리 로드
driver = webdriver.Chrome('./chromedriver')
driver.get("http://www.eum.go.kr/web/am/amMain.jsp")

sidoSelect = Select(driver.find_element_by_xpath('//*[@id="selSido"]'))
sidoSelect.select_by_visible_text('전라남도')
driver.implicitly_wait(1)

sggSelect = Select(driver.find_element_by_xpath('//*[@id="selSgg"]'))
sggSelect.select_by_visible_text('고흥군')
driver.implicitly_wait(1)

umdSelect = Select(driver.find_element_by_xpath('//*[@id="selUmd"]'))
umdSelect.select_by_visible_text('고흥읍')
driver.implicitly_wait(1)

gbnSelect = Select(driver.find_element_by_xpath('//*[@id="selRi"]'))
gbnSelect.select_by_visible_text('남계리')
driver.implicitly_wait(1)

bobn = driver.find_element_by_name('bobn')
bubn = driver.find_element_by_name('bubn')
bobn.send_keys('45')
bubn.send_keys('1')

Button = driver.find_element_by_xpath(
    '//*[@id="frm"]/fieldset/div[3]/p/span/a')
Button.click()

price = driver.find_element_by_xpath('//*[@id="appoint"]/div[2]/table/tbody/tr[3]/td')
print(price.text)



# work1 : 전라남도 고흥군 고흥읍 남계리 본번 45 부번 1 지역에 공시지가를 출력하세요

driver.implicitly_wait(1)
# 상기코드는 드라이버가 1초동안 대기