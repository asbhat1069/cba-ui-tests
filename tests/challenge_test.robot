*** Settings ***
Variables   ./test_data/challenge_test_data.yaml
Variables   ../constants.py
Library     FakerLibrary    WITH NAME   faker
Library     MyKeywords     ${BROWSER}

Suite Setup     open    ${TEST_URL}
Suite Teardown  close_all
Test Teardown   Test Teardown

*** Keywords ***
Test Teardown
    [Arguments]     ${url}=${TEST_URL}
    open    ${url}

*** Test Cases ***

Create a player and start challenge
    ${name}=    faker.first_name
    enter name and create warrior      ${name}
    verify start journey button with name    ${name}
    start challenge journey

As a player Complete battlefield Challenge and check leaderboard
    ${name}=    faker.first_name
    enter name and create warrior      ${name}
    start challenge journey
    start battlefield challenge
    select answer   ${BattlefieldChallengeAnswer1}
    continue on correct answer
    select answer   ${BattlefieldChallengeAnswer2}
    continue on correct answer
    select answer   ${BattlefieldChallengeAnswer3}
    continue on correct answer
    click continue fighting on leaderboard


#As a player complete take a bus challenge and check leaderboard
#     ${name}=    faker.first_name
#    enter name and create warrior      ${name}
#    start challenge journey
#    start bus challenge
#    select answer   ${BusChallengeAnswer}
#    check leaderboard for final score
#    click continue fighting on leaderboard







