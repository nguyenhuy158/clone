from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# import urllib.request


# chromeDriverPath = "./chromedriver.exe"
# userdatadir = "/users"
# chromeOptions = webdriver.ChromeOptions()
# # chromeOptions.add_argument(
# #     f"--user-data-dir={userdatadir}"
# # )  # Path to your chrome profile
# driver = webdriver.Chrome(chromeDriverPath, options=chromeOptions)

driver = webdriver.Chrome()
driver.get("http://bmktdt.cscvn.com:8080/moodle/")

user = "quãng đại ngân"
passs = "ngandeptrai123"
driver.find_element_by_id("login_username").send_keys(user)
driver.find_element_by_id("login_password").send_keys(passs)
time.sleep(2)
driver.find_element_by_id("login_password").send_keys(Keys.RETURN)
# driver.find_element_by_id("#login > div:nth-child(4) > input").click()

parent = "./4.12"
driver.get(
    "http://bmktdt.cscvn.com:8080/moodle/mod/quiz/review.php?attempt=144549&cmid=678"
)
# driver.get("https://uhdwallpapers.org/wallpapers/latest/?page=5")

# que multichoice deferredfeedback complete
time.sleep(2)
questions = driver.find_elements_by_css_selector(".que.multichoice")
# questions = driver.find_elements_by_xpath("//*[@class='multichoice' or @class='jsb']")
# questions[0].get_attribute("checked")
output = ""
print(questions)
for i in questions:
    # print(i)
    number = i.find_element_by_css_selector(".qno")
    print("number", number.text)
    print("")
    title = i.find_element_by_css_selector(".qtext")
    print("title", title.text)
    print("")
    block = i.find_element_by_css_selector(".ablock")
    print("content", block.text)
    print("")

    isTrue = i.find_element_by_css_selector(".grade")
    isCorrect = None
    print("isTrue", isTrue.text)
    if isTrue.text == "Đạt điểm 1,00 trên 1,00":
        keys = block.find_elements_by_tag_name("input")
        # print(keys)
        # print(len(keys))
        for index in range(len(keys)):
            # print("index", keys[index])
            print("key = ", keys[index].get_attribute("checked"), "index", index)
            # if index.get_attribute("checked")
            if keys[index].get_attribute("checked") == "true":
                for label in i.find_elements_by_tag_name("label"):
                    if label.get_attribute("for") == keys[index].get_attribute("id"):
                        isCorrect = label.text
                    print(
                        "isCorrect",
                        keys[index].get_attribute("id"),
                        label.get_attribute("for") == keys[index].get_attribute("id"),
                        label.text,
                        isCorrect,
                    )
    try:
        imgs = i.find_elements_by_tag_name("img")
        count = 0
        for img in imgs:
            # img = i.find_element_by_tag_name("img")
            src = img.get_attribute("src")
            pos = len(src) - src[::-1].index(".")

            print("src", src)
            with open(f"{parent}/{number.text}={count}.png", "wb") as file:
                file.write(img.screenshot_as_png)
                count += 1
    except Exception as e:
        print("src none", str(e))
    output += str(number.text)
    output += "\n"
    output += str(title.text)
    output += "\n"
    output += str(block.text)
    output += "\n"
    # output += isCorrect if isCorrect != None else "Ai ma biet"
    output += "dap an la: " + str(isCorrect)
    output += "\n"


# output to file
with open(f"{parent}/de.txt", "w", encoding="utf-8") as file:
    file.write(output)

time.sleep(2)
driver.close()
# r = driver.find_elements_by_tag_name("img")
# uri = []
# folder = "/user"
# for v in r:
#     src = v.get_attribute("src")
#     uri.append(src)
#     pos = len(src) - src[::-1].index("/")
#     with open(src[pos:], "wb") as file:
#         file.write(v.screenshot_as_png)

# for src in uri:
#     pos = len(src) - src[::-1].index("/")
#     print(src[pos:], src)

#     # src = ""
#     # if src.endswith(".png"):
#     driver.get(src)
#     # driver.save_screenshot(src[pos:])
#     # print(type(src))

#     # with open(src[pos:], "wb") as file:
#     #     file.write(src.screenshot_as_png)
#     # time.sleep(2)
#     # import requests

#     # # url = "https://www.facebook.com/favicon.ico"
#     # url = src
#     # r = requests.get(url, allow_redirects=True)

#     # open(src[pos:], "wb").write(r.content)
#     # # g = urllib.request.urlretrieve(src, "/".join([folder, src[pos:]]))

# for i in range(20):
#     # create instance of Chrome webdriver
#     # driver = webdriver.Chrome()
#     driver.get("http://bmktdt.cscvn.com:8080/moodle/")

#     # find the element where we have to
#     # enter the xpath
#     # target mobile number, change it to victim's number and
#     # also ensure that it's registered on flipkart

#     driver.find_element_by_xpath('//*[@id="ap_email"]').send_keys("xxxx6126")
#     # find the element continue
#     # request using xpath
#     # clicking on that element

#     driver.find_element_by_xpath('//*[@id="continue"]').click()
#     # find the element to send a forgot password
#     # request using xpath

#     driver.find_element_by_xpath('//*[@id="auth-fpp-link-bottom"]').click()
#     driver.find_element_by_xpath('//*[@id="continue"]').click()

#     # set the interval to send each sms
#     time.sleep(4)

#     # Close the browser
#     driver.close()
