# VERSİYON DEĞİŞTİRDİK: 3.11 yaptık ki senin pc ile aynı olsun
FROM python:3.11

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]