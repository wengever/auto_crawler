import sqlite3
from gmail_helper import send_gmail  # ✅ 加這行

def init_db(db_path="example.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS listings (
            title TEXT NOT NULL,
            link TEXT NOT NULL UNIQUE
        )
    ''')
    conn.commit()
    return conn

def insert_listing(conn, title, link):
    try:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO listings (title, link) VALUES (?, ?)', (title, link))
        conn.commit()

        # ✅ 插入成功才寄信
        subject = "新增591房屋通知"
        body = f"新物件標題：{title}\n連結：{link}"
        send_gmail(subject, body)

        return True
    except sqlite3.IntegrityError:
        print(f'⚠️ 已存在，不重複新增: {title}')
        return False

def get_all_listings(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT title, link FROM listings')
    return cursor.fetchall()

def close_db(conn):
    conn.close()
