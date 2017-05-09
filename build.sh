#!/bin/bash

set -e

# Run unittests
python app_tests.py

# Get GIT tag
vcsref=`git rev-parse --short HEAD`

docker build --build-arg VCS_REF=${vcsref} -t vmercier/slack-phonebook:$1 .
docker push vmercier/slack-phonebook:$1