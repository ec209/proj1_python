FROM ubuntu:18.04
MAINTAINER TaegiKim "felimox.kim@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
RUN apt-get install -y sqlite3 libsqlite3-dev
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["dbinit.py"]
CMD ["hello.py"]
