# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 14:47:43 2024

@author: serv5cgpepe
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

inicio = time.time()
url = "https://www.instagram.com/"
driver = webdriver.Chrome()

#Ingreso a Instagram
driver.get(url)
time.sleep(3)
input_user = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label')
input_user.send_keys('a.r.l.10')
time.sleep(2)
input_pass = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label')
input_pass.send_keys('Larios.2022')
time.sleep(2)
input_login = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
input_login.click()
time.sleep(25)
input_notnow = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div')
input_notnow.click()
time.sleep(25)
input_notnow2 = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
input_notnow2.click()

#Inicio de la búsqueda del # que nos involucre la contaminación con 
time.sleep(25)
input_search = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[1]/div/div[2]/div[2]/span/div/a/div/div/div/div')
input_search.click()
time.sleep(5)
input_search_info = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input')
input_search_info.send_keys("#fastfashion")
time.sleep(5)
input_search_info2 = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/a[1]/div[1]/div/div/div[2]/div/div').click()
time.sleep(5)

#Ingreso de las URL's de los post mas interesantes (SCROLL)
scrolldown = driver.execute_script(
    "window.scrollTo(0, document.body.scrollHeight);var scrolldown=document.body.scrollHeight;return scrolldown;")
match = False
while (match == False):
    last_count = scrolldown
    time.sleep(3)
    scrolldown = driver.execute_script(
        "window.scrollTo(0, document.body.scrollHeight);var scrolldown=document.body.scrollHeight;return scrolldown;")
    if last_count == scrolldown:
        match = True

time.sleep(4)
posts = []
links = driver.find_elements("tag name", "a")
for link in links:
    post = link.get_attribute('href')
    if '/p/' in post:
        posts.append(post)

print(posts)
fin = time.time()

tiempo_final = fin - inicio

print(f"El tiempo fue de: {tiempo_final} segundos")
