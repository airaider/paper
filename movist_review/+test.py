# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep
import os

driver = webdriver.Chrome('./driver/chromedriver.exe')
driver.set_window_size(1200, 800)
driver.implicitly_wait(3)


f = open('+2017영화.txt', 'r')
lines = f.readlines()
i = 1
for line in lines:
    line = 'http://www.movist.com/movist3d/read.asp?type=2&type2=1&id='+line
    driver.get(line)
    contents = driver.find_element_by_xpath('//*[@id="subContentWrap"]/div[2]/div[2]/div[2]').text
    if not contents:
        continue
    title = driver.find_element_by_xpath('//*[@id="subContentWrap"]/div[2]/div[2]/div[1]/span[2]').text
    year = driver.find_element_by_xpath('//*[@id="subContentWrap"]/div[2]/div[2]/div[1]/span[3]').text
    year = year[0:4]
    text1 = title
    text1 = text1.replace('\n', '').replace(':', ' ').replace('\\', '').replace('*', '').replace('?', '').replace('<', '').replace('>', '').replace('|', '').replace('/', '').replace('"', '')
    contents = contents.replace('\n', '')
    a = text1 + '(' + year + ').txt'
    print(str(i)+':'+a)
    f2 = open(a, 'w', encoding='utf-8', newline='')
    contents = contents.split('시놉시스')[1]
    f2.write(contents.split('간단평')[0])
    f2.write("\n")
    f2.write(contents.split('간단평')[1].split('2017년')[0])
    i = i+1
    f2.close()
f.close()


f = open('+2016영화.txt', 'r')
lines = f.readlines()
i = 1
for line in lines:
    line = 'http://www.movist.com/movist3d/read.asp?type=2&type2=1&id='+line
    driver.get(line)
    contents = driver.find_element_by_xpath('//*[@id="subContentWrap"]/div[2]/div[2]/div[2]').text
    if not contents:
        continue
    title = driver.find_element_by_xpath('//*[@id="subContentWrap"]/div[2]/div[2]/div[1]/span[2]').text
    year = driver.find_element_by_xpath('//*[@id="subContentWrap"]/div[2]/div[2]/div[1]/span[3]').text
    year = year[0:4]
    text1 = title
    text1 = text1.replace('\n', '').replace(':', ' ').replace('\\', '').replace('*', '').replace('?', '').replace('<', '').replace('>', '').replace('|', '').replace('/', '').replace('"', '')
    contents = contents.replace('\n', '')
    a = text1 + '(' + year + ').txt'
    print(str(i)+':'+a)
    f2 = open(a, 'w', encoding='utf-8', newline='')
    contents = contents.split('시놉시스')[1]
    f2.write(contents.split('간단평')[0])
    f2.write("\n")
    f2.write(contents.split('간단평')[1].split('2016년')[0])
    i = i+1
    f2.close()
f.close()


f = open('+2015영화.txt', 'r')
lines = f.readlines()
i = 1
for line in lines:
    line = 'http://www.movist.com/movist3d/read.asp?type=2&type2=1&id='+line
    driver.get(line)
    contents = driver.find_element_by_xpath('//*[@id="subContentWrap"]/div[2]/div[2]/div[2]').text
    if not contents:
        continue
    title = driver.find_element_by_xpath('//*[@id="subContentWrap"]/div[2]/div[2]/div[1]/span[2]').text
    year = driver.find_element_by_xpath('//*[@id="subContentWrap"]/div[2]/div[2]/div[1]/span[3]').text
    year = year[0:4]
    text1 = title
    text1 = text1.replace('\n', '').replace(':', ' ').replace('\\', '').replace('*', '').replace('?', '').replace('<', '').replace('>', '').replace('|', '').replace('/', '').replace('"', '')
    contents = contents.replace('\n', '')
    a = text1 + '(' + year + ').txt'
    print(str(i)+':'+a)
    f2 = open(a, 'w', encoding='utf-8', newline='')
    contents = contents.split('시놉시스')[1]
    f2.write(contents.split('간단평')[0])
    f2.write("\n")
    f2.write(contents.split('간단평')[1].split('2015년')[0])
    i = i+1
    f2.close()
f.close()

f = open('+2014영화.txt', 'r')
lines = f.readlines()
i = 1
for line in lines:
    line = 'http://www.movist.com/movist3d/read.asp?type=2&type2=1&id='+line
    driver.get(line)
    contents = driver.find_element_by_xpath('//*[@id="subContentWrap"]/div[2]/div[2]/div[2]').text
    if not contents:
        continue
    title = driver.find_element_by_xpath('//*[@id="subContentWrap"]/div[2]/div[2]/div[1]/span[2]').text
    year = driver.find_element_by_xpath('//*[@id="subContentWrap"]/div[2]/div[2]/div[1]/span[3]').text
    year = year[0:4]
    text1 = title
    text1 = text1.replace('\n', '').replace(':', ' ').replace('\\', '').replace('*', '').replace('?', '').replace('<', '').replace('>', '').replace('|', '').replace('/', '').replace('"', '')
    contents = contents.replace('\n', '')
    a = text1 + '(' + year + ').txt'
    print(str(i)+':'+a)
    f2 = open(a, 'w', encoding='utf-8', newline='')
    contents = contents.split('시놉시스')[1]
    f2.write(contents.split('간단평')[0])
    f2.write("\n")
    f2.write(contents.split('간단평')[1].split('2014년')[0])
    i = i+1
    f2.close()
f.close()

driver.quit()

