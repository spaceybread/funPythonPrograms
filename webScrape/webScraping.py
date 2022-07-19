from selenium import webdriver
from selenium.webdriver.common.by import By
n = 0

with open('databank.txt', 'a+') as fp:
    pass


file = open('databank.txt', 'a+')

driver = webdriver.Edge()


def webpageCycle():
    URL = input("URL: ")
    cName = input("Class Name: ")
    driver.get(URL)
    items = driver.find_elements(By.CLASS_NAME, cName)
    for element in items:
        file.write(cName + " " + element.text)
        file.write('\n')


def manualEdit():
    file.write(input('add text: '))


def delAll():
    file.truncate()
    file.close()


def close():
    file.close()


def read():
    content = file.read()
    print(content)


while n == 0:
    check = input("webscrape(w), manual add(m), read(r), del(d), close(c): ")
    fCheck = check.lower()
    if fCheck in ["m"]:
        manualEdit()
    if fCheck in ["w"]:
        webpageCycle()
    if fCheck in ["r"]:
        read()
    if fCheck in ["d"]:
        delAll()
    if fCheck in ["c"]:
        close()
        n = n + 1
