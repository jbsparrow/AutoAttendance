from selenium import webdriver
import time

option = webdriver.ChromeOptions()
option.add_argument("user-data-dir=selenium") 
# this is to prevent from having to log in each time.

browser = webdriver.Chrome(executable_path='~/home/chromedriver', options=option)

browser.get("google form link")


textboxes = browser.find_elements_by_class_name("quantumWizTextinputPaperinputInput")
submitbutton = browser.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div/div/span/span") 
# if switching to a new google form you have to find the xpath of the submit button again.


textboxes[0].send_keys("248892742") # Student No.

textboxes[1].send_keys("John") # First name

textboxes[2].send_keys("Doe") # Last name

textboxes[3].send_keys("FOI091") # Class code

textboxes[4].send_keys("Jane Doe") # Teacher name

browser.find_element_by_class_name("quantumWizMenuPaperselectOptionList").click()

# the downtime allows you to check if everything has been selected correctly because I don't trust my code
time.sleep(7)


submitbutton.click()

browser.close()
