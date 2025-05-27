# Task 1: How to find total page number in daraz category page and implement in your code to iterate the page number. Please implement a code

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

driver = webdriver.Chrome()

# driver.get('https://www.daraz.pk/invisible-unisex-fashion-3/')
driver.get('https://www.daraz.pk/laptops/')

driver.maximize_window()

title_list = []

total_items = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[1]/div/div[1]/div/div/span[1]').text

# '//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[1]/div/div[1]/div/div/span[1]'

# print(total_items)

total_item = int(total_items.split()[0].replace(",", ""))
# total_item = int(total_item)
# print(total_item)

# 40 items per page
items_per_page = 40
total_page = math.ceil(total_item / items_per_page)

# print(total_page)

print(f"Total items: {total_items}")
print(f"Total pages: {total_page}")

for page in range(1, total_page + 1):
    driver.get(f'https://www.daraz.pk/laptops/?page={page}')

    for i in range(1, items_per_page + 1):
        j = str(i)
        title = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div['+j+']/div/div/div[2]/div[2]/a').text 
        title_list.append(title)

print(title_list)
print(len(title_list))

# Task 2: How to do same work by clicking on pagination button without traversing page number. (Please make a idea. Code can be bonus but not mandatory)

