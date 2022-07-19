from selenium import webdriver
from selenium.webdriver.common.by import By

file = open('databank.txt', 'w')
n = 0

driver = webdriver.Edge()


def webpageCycle():
    URL = input("URL: ")
    cName = input("Class Name: ")
    driver.get(URL)
    items = driver.find_elements(By.CLASS_NAME, cName)
    for element in items:
        file.write(element.text + " ADDED BY WEBSCRAPE")
        file.write('\n')


def manualEdit():
    file.write(input('add text: '))


while n == 0:
    check = input("manual(m), webscrape(w), close(c), delete(d): ")
    if check in ['m']:
        manualEdit()
    if check in ['w']:
        webpageCycle()
    if check in ['d']:
        file.truncate()
        n = n + 1
    if check in ['c']:
        n = n + 1
