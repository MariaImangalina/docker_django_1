FROM django:3.0.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /web_app
WORKDIR /web_app

COPY . /web_app

RUN apt-get update
RUN pip install -r /web_app/requirements.txt

EXPOSE 8000

CMD [ "manage.py", 'runserver']
