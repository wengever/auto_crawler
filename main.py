import os
import time
from dotenv import load_dotenv
from utils import get_page_content, use_selenium
from db_helper import init_db, insert_listing, close_db

load_dotenv()
filter_url = os.getenv("591_FILTER_URL")
if not filter_url:
    print("沒有讀到 591_FILTER_URL，請確認 .env")
    exit(1)

def write_titles_and_links(driver, start_url, conn):
    page = 1
    soup = get_page_content(driver, start_url)
    time.sleep(1)

    new_count = 0  # 統計新增資料筆數

    # 如果沒有找到 class="empty" 的標籤，就代表這一頁還有資料
    while soup.find(class_='empty') is None:
        print(f'getting page {page}')

        wrapper = soup.find('div', class_='list-wrapper')
        items = wrapper.find_all('div', class_='item') if wrapper else []

        for item in items:
            title_element = item.find('a', class_='link v-middle')
            if title_element:
                title = title_element.text.strip()
                link = title_element['href']
                success = insert_listing(conn, title, link)
                if success:
                    new_count += 1

        print(f'successfully crawl page: {page}')
        page += 1
        soup = get_page_content(driver, start_url + f'&page={page}')
        time.sleep(1)

    print(f'抓取完畢，本次新增 {new_count} 筆資料')
    return new_count

# def write_titles_and_links(driver, start_url, conn):
#     page = 1
#     soup = get_page_content(driver, start_url)
#     time.sleep(1)

#     new_count = 0  # 新增一個統計用的變數

#     while soup.select_one('.empty') is None:
#         print(f'getting page {page}')
#         items = soup.select('.list-wrapper .item')
#         for item in items:
#             title_element = item.select_one('a.link')
#             if title_element:
#                 title = title_element.text.strip()
#                 link = title_element['href']
#                 success = insert_listing(conn, title, link)  # 改成能知道是否成功
#                 if success:
#                     new_count += 1  # 成功新增才累加
#         print(f'successfully crawl page: {page}')
#         page += 1
#         soup = get_page_content(driver, start_url + f'&page={page}')
#         time.sleep(1)

#     print(f'抓取完畢，本次新增 {new_count} 筆資料')
#     return new_count  # 把新增數量回傳


def main():
    driver = use_selenium()
    conn = init_db()
    new_records = write_titles_and_links(driver, filter_url, conn)
    close_db(conn)
    print(f'本次總共新增了 {new_records} 筆資料到資料庫！')  # 最後也提醒一次

if __name__ == "__main__":
    main()
