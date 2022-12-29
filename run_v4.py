from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
 
options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.maximize_window() 

driver.get("https://speedsums.com/")
print(driver.title)


ques_xpath  = '//*[@id="question"]'  
ans_xpath = '//*[@id="answer"]'

while True:
    elem = driver.find_element("xpath",ques_xpath)
    data = eval(elem.text.replace("x","*").replace("÷","//").replace("=",""))
    driver.find_element("xpath", ans_xpath).send_keys(data)