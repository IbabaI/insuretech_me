from selenium import webdriver
driver = webdriver.Chrome('./chromedriver')
# 크롬을 통해서 스크래핑을 진행 크롬 드라이버 로딩

driver.get('https://www.jobplanet.co.kr/companies/144007/interviews/%ED%81%90%EB%B9%85%EC%95%84%EC%9D%B4%EC%97%94%EC%94%A8')
tablebody = driver.find_element_by_xpath('//*[@id="viewInterviewsList"]/div/div/section[1]/div/div[2]/div/div[2]')
rowInTable = tablebody.find_elements_by_xpath('div')
for index, row in enumerate(rowInTable):
    print(index + 1)
    titleAndSinger = row.find_elements_by_tag_name('td')[5]
    print(titleAndSinger.text)