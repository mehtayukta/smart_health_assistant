#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 18:12:26 2023

@author: yuktamehta
"""


from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver


options = Options()
driver = webdriver.Chrome(service=Service('/Users/yuktamehta/Desktop/MS/Courses/Fall23/Data-270_Data_Analtyical_Processing/Project/scripts/chromedriver'), options=options)
driver.get('https://people.dbmi.columbia.edu/~friedma/Projects/DiseaseSymptomKB/index.html')
#l = driver.find_elements_by_xpath ("/html/body/div/table")
element = driver.find_element(By.XPATH, "/html/body/div/table")
# Get the text or attribute value from the element
data = element.text  # or element.get_attribute('attribute_name')

# Close the browser when done
driver.quit()


file_path = "/Users/yuktamehta/Desktop/MS/Courses/Fall23/Data-270_Data_Analtyical_Processing/Project/output_data/diease_and_data.txt"

data = data.replace("^", "\n")
with open(file_path, 'w') as file:
    file.write(data)

print(f"Data has been saved to {file_path}")

