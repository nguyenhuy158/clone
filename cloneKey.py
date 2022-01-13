from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os


def writeKey(folder, url):
    print(folder, url)

    # LOGIN
    driver = webdriver.Chrome()
    driver.get("http://bmktdt.cscvn.com:8080/moodle/")
    user = "quãng đại ngân"
    passs = "ngandeptrai123"
    driver.find_element_by_id("login_username").send_keys(user)
    driver.find_element_by_id("login_password").send_keys(passs)
    time.sleep(2)
    driver.find_element_by_id("login_password").send_keys(Keys.RETURN)

    parent = f"./{folder}"
    driver.get(url)

    time.sleep(2)

    questions = driver.find_elements_by_css_selector(".que.multichoice")
    output = ""
    print(questions)
    for i in questions:
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
                        if label.get_attribute("for") == keys[index].get_attribute(
                            "id"
                        ):
                            isCorrect = label.text
                        print(
                            "isCorrect",
                            keys[index].get_attribute("id"),
                            label.get_attribute("for")
                            == keys[index].get_attribute("id"),
                            label.text,
                            isCorrect,
                        )
        # try:
        #     imgs = i.find_elements_by_tag_name("img")
        #     count = 0
        #     for img in imgs:
        #         # img = i.find_element_by_tag_name("img")
        #         src = img.get_attribute("src")
        #         pos = len(src) - src[::-1].index(".")

        #         print("src", src)
        #         with open(f"{parent}/{number.text}={count}.png", "wb") as file:
        #             file.write(img.screenshot_as_png)
        #             count += 1
        # except Exception as e:
        #     print("src none", str(e))
        if isCorrect != None:
            output += str(number.text)
            output += "\n"
            output += str(title.text)
            output += "\n"
            # output += str(block.text)
            # output += "\n"
            # output += isCorrect if isCorrect != None else "Ai ma biet"
            output += "dap an la: " + str(isCorrect)
            output += "\n"

    # output to file
    with open(f"{parent}.txt", "w", encoding="utf-8") as file:
        file.write(output)

    time.sleep(2)
    driver.close()


# output to file
links = []
with open(f"input.txt", "r", encoding="utf-8") as file:
    inputs = file.read().split("\n")
    for i in inputs:
        print(len(i), i)
        if len(i) != 0 and len(i) < 10:
            try:
                os.mkdir(i)
            except Exception as e:
                print("error", str(e))

inputs.pop()
print(len(inputs))
print("CLONE*" * 10)
home = 0
indexLink = 1
while home < len(inputs):
    writeKey(inputs[home], inputs[indexLink])

    home += 2
    indexLink += 2
