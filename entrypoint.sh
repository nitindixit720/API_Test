#!/usr/bin/env bash

# Environment setup
##TODO take environment outside
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirement.txt
#pip freeze |grep slacker
export TEST_ENV=staging
export PYTHONPATH=.
export SLACK_AUTH_TOKEN="Provide SLACK_AUTH_TOKEN"
export SLACK_CHANNEL="Provide SLACK_CHANNEL name"
export PROJECT_NAME=${PWD##*/}
echo $PROJECT_NAME



# Create report folder
LOCAL_REPORTS_DIR="reports"
REPORT_DIR_NAME=`date +'%Y-%m-%d-%H-%M-%S'`
export S3_PREFIX="$TEST_ENV/$PROJECT_NAME/$REPORT_DIR_NAME"
echo $S3_PREFIX
if test ! -d reports/; then
    echo "reports directory not found, creating the same"
    mkdir -p reports/
fi
echo "Creating directory reports/$REPORT_DIR_NAME"
mkdir -p reports/${REPORT_DIR_NAME}

SERVER_URL="S3 server URL"

# S3 upload
FINAL_PREFIX=$SERVER_URL$S3_PREFIX

# Run code
TEST_SKIP_MESSAGE="*[$TEST_ENV] One or more services required for API tests are unavailable, skipping tests.* :sleeping:"
TEST_FAIL_MESSAGE="*[$TEST_ENV] One or more tests from one or more suites have failed.* :cry:"
TEST_PASS_MESSAGE="*[$TEST_ENV] All tests from all suites have passed.* :dancing_panda:"
export SLACK_MESSAGE_TEMPLATE="[$TEST_ENV] genie-api-test: {passed}/{enabled} passed | $FINAL_PREFIX/report/report.html"
lcc run --enable-reporting slack console html --exit-error-on-failure
export CURRENT_SUITE_EXECUTION_STATUS=$?
python scripts/upload_report_to_s3.py report/report.html
python scripts/upload_report_to_s3.py report/report.js
python scripts/upload_report_to_s3.py report/.html/report.css
python scripts/upload_report_to_s3.py report/.html/report.js


# Slack message
if [ ${CURRENT_SUITE_EXECUTION_STATUS} -eq 0 ]; then
    python scripts/send_message_to_slack.py -t "${SLACK_AUTH_TOKEN}" -c "${SLACK_CHANNEL}" -m "${TEST_PASS_MESSAGE}"
else
    python scripts/send_message_to_slack.py -t "${SLACK_AUTH_TOKEN}" -c "${SLACK_CHANNEL}" -m "${TEST_FAIL_MESSAGE}"
fi
echo "Test suite execution completed with exit code" ${CURRENT_SUITE_EXECUTION_STATUS}
