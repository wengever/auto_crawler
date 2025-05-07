FROM python:3.10-slim

# 安裝 Chromium 及其依賴（用於 Selenium）
RUN apt-get update && apt-get install -y \
    chromium-driver \
    chromium \
    libglib2.0-0 \
    libnss3 \
    libgconf-2-4 \
    libx11-xcb1 \
    libxcomposite1 \
    libxcursor1 \
    libxdamage1 \
    libxi6 \
    libxtst6 \
    libappindicator1 \
    libxrandr2 \
    libasound2 \
    libatk-bridge2.0-0 \
    libgtk-3-0 \
    && rm -rf /var/lib/apt/lists/*

ENV CHROME_BIN=/usr/bin/chromium

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir selenium beautifulsoup4 python-dotenv pandas

CMD ["python", "crawl.py"]
