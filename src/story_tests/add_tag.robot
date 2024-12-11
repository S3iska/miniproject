*** Settings ***
Library   ../RefLibrary.py
Resource  resource.robot

Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Setup Test Db

*** Variables ***
${TAG_NAME}       tagtest549


*** Test Cases ***
Add a Tag
    Go To Add Tag Page
    Input Text      id=tag_id    ${TAG_NAME}
    Press Keys      id=tag_id    ENTER
    Go To Home Page
    Page Should Contain    ${TAG_NAME}

One Or Multiple Tags
    Go To Home Page
    Page Should Contain  AMD
    Page Should Contain  Intel

Delete Tags From Ref
    Go To Add Tag Page
    Click Button  Delete
    Click Button  Delete
    Click Button  Confirm
    Page Should Not Contain  Intel AMD

