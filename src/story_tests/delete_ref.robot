*** Settings ***
Library   ../RefLibrary.py
Library   Collections
Resource  resource.robot

Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Setup Test Db

*** Test Cases ***
Remove Article Reference
    Go To Home Page
    Page Should Contain       ref1
    Scroll Element Into View  id:deleteref1
    Click Button              id:deleteref1
    Handle Alert              ACCEPT
    Go To Home Page
    Page Should Not Contain   ref1

Reference Is Not Removed If Pop Up Is Cancelled
    Go To Home Page
    Page Should Contain       ref1
    Scroll Element Into View  id:deleteref1
    Click Button              id:deleteref1
    Handle Alert              DISMISS
    Go To Home Page
    Page Should Contain       ref1
