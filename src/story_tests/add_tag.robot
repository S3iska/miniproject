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
    Page Should Contain  Intel
    Page Should Contain  AMD NVIDIA

Delete Tags From Ref
    Go To Home Page
    Page Should Contain  Intel AMD
    Go To Add Tag Page
    Click Button  Delete
    Click Button  Delete
    Click Button  Confirm
    Page Should Not Contain  Intel AMD

Tag Added Only Once To Ref
    Go To Home Page
    Page Should Contain  Intel AMD
    Go To Add Tag Page
    Click Button  xpath=//button[text()="AMD"]
    Click Button  Confirm
    Page Should Not Contain  Intel AMD AMD

Cancel Button Does Not Trigger a Warning on an Unchanged Add Tag Page
    Go To Add Tag Page
    Click Button  Cancel
    Verify That This Is the Home Page

Cancel Button Triggers a Warning on a Changed Add Tag Page
    Go To Add Tag Page
    Click Button  Add new tag
    Click Button  Cancel
    Alert Should Be Present