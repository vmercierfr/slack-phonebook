FROM python:3

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

ADD requirements.txt /code/
RUN pip3 install -r requirements.txt

ADD . /code/

CMD ["/usr/local/bin/gunicorn", "app:app", "-w", "1", "-b", ":80", "--reload"]