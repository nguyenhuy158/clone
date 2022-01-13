page_course = "http://bmktdt.cscvn.com:8080/moodle/course/view.php?id=43"
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("http://bmktdt.cscvn.com:8080/moodle/")

user = "quãng đại ngân"
passs = "ngandeptrai123"
driver.find_element_by_id("login_username").send_keys(user)
driver.find_element_by_id("login_password").send_keys(passs)
time.sleep(2)
driver.find_element_by_id("login_password").send_keys(Keys.RETURN)

driver.get(page_course)

allTagA = driver.find_elements_by_css_selector(".activityinstance")
links = []
for tagA in allTagA:
    # tagA.text = ""
    if tagA.text.startswith("Prac"):
        a = tagA.find_element_by_tag_name("a")
        print(tagA.text, a.get_attribute("href"))
        links.append(a.get_attribute("href"))
        # driver.get(tagA.)
        # tagA.click()

linkSections = [[] for i in range(len(links) + 1)]
index = 1
for link in links:
    driver.get(link)
    linkSection = driver.find_elements_by_css_selector(".cell.c4.lastcol")
    for ls in linkSection:
        href = ls.find_element_by_tag_name("a").get_attribute("href")
        print(index, href)
        linkSections[index].append(href)
    index += 1
    time.sleep(3)

time.sleep(2)
driver.close()
# output to file
with open(f"input.txt", "w", encoding="utf-8") as file:
    for i in range(len(linkSections)):
        for j in range(len(linkSections[i])):
            file.write(f"{i}.{j}\n{linkSections[i][j]}\n")
