FROM python:3.7.4

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /web_app
WORKDIR /web_app

COPY . /web_app

RUN apt-get update
RUN pip install -r /web_app/requirements.txt

EXPOSE 7000

CMD [ "python", "./manage.py", "runserver", "0.0.0.0:7000" ]

