*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser

*** Test Cases ***
Home Page Loads
    Go To Home Page
    Page Should Contain Link    Lisää uusi viite
    Page Should Contain Button    NUKE
