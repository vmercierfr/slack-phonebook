FROM python:3

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

ADD requirements.txt /code/
RUN pip3 install -r requirements.txt

ADD . /code/

# Add extra information in docker container
ARG VCS_REF
LABEL authors="Vincent MERCIER" \
      org.org.label-schema.schema-version="1.0.0-rc.1" \
      org.org.label-schema.vcs-type="git" \
      org.org.label-schema.vcs-url="https://github.com/vmercierfr/slack-phonebook" \
      org.org.label-schema.vcs-ref=$VCS_REF

CMD ["/usr/local/bin/gunicorn", "phonebook.app:app", "-w", "1", "-b", ":80", "--reload"]