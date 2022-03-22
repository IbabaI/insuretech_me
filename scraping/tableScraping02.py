from selenium import webdriver
driver = webdriver.Chrome('./chromedriver')
# 크롬을 통해서 스크래핑을 진행 크롬 드라이버 로딩

driver.get('https://www.alimi.or.kr/dataview/a/selectDsFacilities.do')
tablebody = driver.find_element_by_xpath('//*[@id="list"]/tbody/tr[3]/td/table/tbody')
rowInTable = tablebody.find_elements_by_xpath('tr')
for index, row in enumerate(rowInTable):
    print(index + 1)
    titleAndSinger = row.find_elements_by_tag_name('th')[5]
    print(titleAndSinger.text)