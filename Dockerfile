FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

COPY wait-for-it.sh /usr/src/app/wait-for-it.sh
COPY database.sql /docker-entrypoint-initdb.d/

CMD ["sh", "-c", "./wait-for-it.sh mysql:3306 -- uvicorn api:app --host 0.0.0.0 --port 5000"]
