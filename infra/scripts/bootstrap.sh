#!/bin/bash
aws cloudformation deploy \
--template-file bootstrap/github.yaml \
--stack-name GitHub-Bootstrap-Stack \
--capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM \
--no-fail-on-empty-changeset \
--parameter-overrides \
    GitHubRepo=Manuel3567/agent-observability-poc