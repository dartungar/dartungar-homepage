from selenium import webdriver

import subprocess


cwd = "C:\gdrive\sites\dartungar-homepage"
addrs = "http://127.0.0.1:5000/apps/seofy"

driver = webdriver.Chrome()
driver.get(addrs)

subprocess.run("flask run", cwd=cwd)


