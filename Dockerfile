FROM python:3

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

ADD requirements.txt /code/
RUN pip3 install -r requirements.txt

ADD . /code/

# Add extra information in docker container
ARG VCS_REF
ARG BUILD_DATE
ARG BUILD_VERSION
LABEL authors="Vincent MERCIER" \
    org.label-schema.schema-version="1.0.0-rc.1" \
    org.label-schema.name="Slack phonebook" \
    org.label-schema.description="Simple phonebook for Slack" \
    org.label-schema.url="https://github.com/vmercierfr/slack-phonebook" \
    org.label-schema.usage="See https://github.com/vmercierfr/slack-phonebook/blob/master/README.md" \
    org.label-schema.vendor="Vincent MERCIER" \
    org.label-schema.vcs-type="git" \
    org.label-schema.vcs-url="https://github.com/vmercierfr/slack-phonebook" \
    org.label-schema.vcs-ref=$VCS_REF \
    org.label-schema.build-date=$BUILD_DATE \
    org.label-schema.version=$BUILD_VERSION

CMD ["/usr/local/bin/gunicorn", "phonebook.app:app", "-w", "1", "-b", ":80", "--reload"]