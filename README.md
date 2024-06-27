# Web Scrapping
A little example to extract meanings from longman dictionary, only for educational purposes

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

path = r'C:\Users\...\chromedriver.exe'

service = Service(executable_path=path)

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
browser = webdriver.Chrome(service=service, options=options)

def meaning(word='get-out'):

  browser.get('https://www.ldoceonline.com/')

  input_path = '//input[@class="search_input"]'
  box_input = browser.find_elements(By.XPATH, input_path)[0]
  box_input.send_keys(word)

  search_path = '//button[@type="submit"]'
  button_search = browser.find_elements(By.XPATH, search_path)[0]
  button_search.click()

  # dictentry shows a gropu of meanings as verb, noun, adjective
  dictentry_path = '//span[@class="dictentry"]'
  meaning_groups = browser.find_elements(By.XPATH, dictentry_path)

  meaning = ''

  for i, group in enumerate(meaning_groups):

    n = '[' + str(i+1) + ']'

    xpath_POS = dictentry_path + n + '//span[@class="POS"]'
    xpath_senses = dictentry_path + n + '//span[@class="DEF"]'

    POS = browser.find_elements(By.XPATH, xpath_POS)[0].text
    meaning += POS.upper() + ': '

    for sense in group.find_elements(By.XPATH, xpath_senses):

      meaning += sense.text + '; '

  return meaning
