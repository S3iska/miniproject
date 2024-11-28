*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser

*** Test Cases ***
Home Page Loads
    Go To Home Page
    Page Should Contain Link    Add a new reference
    Page Should Contain Button    Delete all
