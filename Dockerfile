FROM selenium/standalone-chrome:latest

USER root

WORKDIR /app

RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip3 install --break-system-packages --no-cache-dir -r requirements.txt

COPY . .

CMD ["pytest", "-v", "--html=reports/report.html", "--self-contained-html"]