FROM python:3.10

WORKDIR /app

COPY consumer_script/. /app/.

RUN pip3 install -r requirements.txt

CMD ["python3", "-u", "mailing.py"]
