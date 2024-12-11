*** Settings ***
Library   ../RefLibrary.py
Library   Collections
Resource  resource.robot

Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Setup Test Db

*** Variables ***
${type}           article
${REF_NAME}       testref
${AUTHOR}         Test Author
${TITLE}          Test Title
${JOURNAL}        Test Journal
${YEAR}           2020
${VOLUME}         Test Volume

*** Test Cases ***
Home Page Loads
    Go To Home Page
    Page Should Contain Link    Add a new reference
    Page Should Contain Button    Delete all

Reference Is Visible On Home Page
    Go To Add Ref Page
    Set Ref type  article
    Input Text  xpath=//div[@id='articleForm']//form//input[@name='ref_name']  ${REF_NAME}
    Input Text  xpath=//div[@id='articleForm']//form//input[@name='author']    ${AUTHOR}
    Input Text  xpath=//div[@id='articleForm']//form//input[@name='title']     ${TITLE}
    Input Text  xpath=//div[@id='articleForm']//form//input[@name='journal']   ${JOURNAL}
    Input Text  xpath=//div[@id='articleForm']//form//input[@name='year']      ${YEAR}
    Click Button  xpath=//div[@id='articleForm']//form//button

    Page Should Contain    ${REF_NAME}
    Page Should Contain    ${AUTHOR}
    Page Should Contain    ${TITLE}
    Page Should Contain    ${YEAR}

Tag Filtering Filters References Correctly
    Go To Home Page
    Input Text    tag_filter   NVIDIA
    Click Button  Filter
    Page Should Not Contain    Intel

*** Keywords ***
Set Ref type
    [Arguments]  ${type}
    Select From List By Value  id:typeSelect  ${type}