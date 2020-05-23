from selenium import webdriver
import time
import logging
logging.basicConfig(format = u'[%(asctime)s]  %(message)s', level = logging.DEBUG)

username = input('Username: ')
password = input('Password: ')
hours = int(input('How long do you want the program to work?(hours) '))

Username, Password, Hours = username,password,hours


    