from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def use_disable_chrome_annoyings():
    options = Options()
    options.add_argument('--headless')  # ✅ 無視覺介面，才能跑在 Docker 裡
    options.add_argument('--no-sandbox')  # ✅ 避免權限問題
    options.add_argument('--disable-dev-shm-usage')  # ✅ 避免 /dev/shm 空間不足
    options.add_argument('--disable-notifications')
    options.add_argument('--disable-infobars')
    options.add_argument('--disable-extensions')
    options.add_argument('--user-data-dir=/tmp/chrome-user-data')  # ✅ 避免使用預設 user 資料夾
    options.add_experimental_option("prefs", {
        "profile.managed_default_content_settings.javascript": 2  # 可選擇禁用 JS
    })
    return options


def get_page_content(driver, url):
    driver.get(url)
    print('Getting page content of title: ', driver.title)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    return soup

def use_selenium():
    options = use_disable_chrome_annoyings()  # 設定安靜無干擾模式
    driver = webdriver.Chrome(options=options)  # 啟動 Chrome 瀏覽器
    driver.implicitly_wait(10)  # 每次找元素最多等 10 秒
    return driver  # 傳回這個瀏覽器控制物件
