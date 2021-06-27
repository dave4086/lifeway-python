FROM python:3.8.5

RUN mkdir /app
WORKDIR /app
ADD . /app/
RUN pip install -r requirements.txt

EXPOSE 80
CMD ["python", "/app/app.py"]