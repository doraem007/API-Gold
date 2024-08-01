FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# ติดตั้ง mysql-client
RUN apt-get update && apt-get install -y mysql-client

COPY wait-for-it.sh /usr/src/app/wait-for-it.sh
RUN chmod +x /usr/src/app/wait-for-it.sh

CMD ["sh", "-c", "./wait-for-it.sh mysql:3306 -- uvicorn api:app --host 0.0.0.0 --port 5000"]
