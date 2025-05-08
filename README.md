# 🏠 591 Auto Rental Crawler

This is an automated web crawler project that scrapes rental listings from [591 Rental Website](https://rent.591.com.tw) based on your filter settings. It saves the title and link into an SQLite database and sends notifications via Gmail.

✅ Docker-supported deployment  
✅ Uses `.env` for configuration  
✅ Gmail notification support  
✅ Can be scheduled to run daily

---

## 📦 Project Structure

```
auto_crawler/
├── main.py                # Main script
├── db_helper.py           # SQLite database logic
├── gmail_helper.py        # Gmail notification module
├── utils.py               # Selenium settings and crawler logic
├── Dockerfile             # Docker build instructions
├── .env                   # Your environment variables
└── example.db             # Database file (auto-generated)
```

---

## 🚀 How to Use

### 1️⃣ Create `.env` Configuration File

Create a `.env` file in the root directory with the following content:

```
591_FILTER_URL=https://rent.591.com.tw/?region=1&section=8
GMAIL_USER=your_gmail_account@gmail.com
GMAIL_PASSWORD=your_gmail_app_password
TO_EMAIL=recipient_email@gmail.com
```

> 📌 Your Gmail password must be an [App Password](https://myaccount.google.com/apppasswords), not your regular login password.

---

### 2️⃣ Install Dependencies (Non-Docker Users)

```bash
python main.py
```

---

### 🐳 Run with Docker

#### 🔨 Build Image:

```bash
docker build -t auto-crawler .
```

#### ▶️ Run:

```bash
docker run --rm --env-file .env auto-crawler
```

> 📦 To persist the database between runs:
```bash
docker run --rm --env-file .env -v %cd%/example.db:/app/example.db auto-crawler
```

---

## ⏰ Scheduling Suggestions

### 🖥️ For Windows Users:
You can use Task Scheduler to run the following command daily:

```powershell
docker run --rm --env-file C:\path	o\.env auto-crawler
```

---

## 📧 Gmail Notification Example

When new listings are found, you will receive an email like this:

```
New listing on 591!
🏷️ Affordable Studio · $10,000/month
🔗 https://rent.591.com.tw/rent-detail-123456.html
```
