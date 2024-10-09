FROM python:3.9-slim

WORKDIR /myProject

ADD . /myProject

RUN pip install  --no-cache-dir -r requirements.txt

CMD ["python","WeatherFetch.py"]
