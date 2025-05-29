FROM python:3.13.2

WORKDIR /app

COPY requirements.txt .

RUN pip install  -r requirements.txt

COPY . .

EXPOSE 5000

ENV FLASK_APP=app.py
ENV FLASK_ENV=production

CMD ["python","api/app.py"]