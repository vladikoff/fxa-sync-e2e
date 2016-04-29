#!/bin/bash -ex

# From: https://circleci.com/docs/nightly-builds/
# Usage: run-tests.sh example-corp/project-foo master ${CIRCLE_TOKEN}

_project=$1
_branch=$2
_circle_token=$3

trigger_build_url=https://circleci.com/api/v1/project/${_project}/tree/${_branch}?circle-token=${_circle_token}

post_data=$(cat <<EOF
{
  "build_parameters": {
    "RUN_NIGHTLY_BUILD": "true"
  }
}
EOF)

curl \
--header "Accept: application/json" \
--header "Content-Type: application/json" \
--data "${post_data}" \
--request POST ${trigger_build_url}