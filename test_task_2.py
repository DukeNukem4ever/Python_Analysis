##### ЧАСТЬ 2 #####

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup

# Запуск драйвера
option = Options()
option.add_argument("--disable-infobars")
browser = webdriver.Chrome()

# Открытие ссылки через драйвер
browser.get("https://example.com")
soup = BeautifulSoup(browser.page_source,
                            features="lxml")

# Поиск слова "Example" в заголовке страницы
post_check = soup.find('title').text
if "Example" in post_check:
    print("True")

# Поиск по CSS-селектору
content = browser.find_element(By.CSS_SELECTOR, 'body > div > p:nth-child(3) > a')
print("Ссылка, найденная по CSS-селектору: " + content.get_attribute("href"))
time.sleep(5)

# Кликаем на ссылку
content.click()
print()
print("Текущая ссылка, после перехода по селектору: " + browser.current_url)
time.sleep(5)

# Закрываем драйвер
browser.close()

