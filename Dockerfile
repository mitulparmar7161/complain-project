# pull the official base image
FROM python:3.11.1

# set work directory
WORKDIR /complain

# set environment variables
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN apt-get update

RUN apt-get install -y cron && touch /var/log/cron.log

RUN pip install --upgrade pip


COPY ./requirements.txt /complain/
RUN pip install -r requirements.txt

# copy project
COPY . /complain/

EXPOSE 8000

# ENTRYPOINT ["./docker-entrypoint.sh"]
CMD ["python", "manage.py", "runserver", "127.0.0.1:8000"]