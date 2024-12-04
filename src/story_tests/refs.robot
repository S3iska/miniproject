*** Settings ***
Library  ../RefLibrary.py
Library  Collections
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup  Setup Test Db

*** Variables ***
${type}           article
${REF_NAME}       testref
${AUTHOR}         Test Author
${TITLE}          Test Title
${YEAR}           2020
${JOURNAL}        Test Journal

*** Test Cases ***
Add Article Reference and Verify in Database
    # Add a new reference via the web form
    Go To Add Ref Page
    Set Default Values
    Submit Values

    # Verify the reference is stored in the database
    ${criteria}=    Create Dictionary    ref_name=${REF_NAME}    author=${AUTHOR}    title=${TITLE}    year=${YEAR}    journal=${JOURNAL}
    ${results}=     Get Refs From Database    &{criteria}

    # Assert that the reference exists
    Should Not Be Empty    ${results}    No references found for criteria: ${criteria}

    # Assert the specific values match
    ${result}=      Get From List    ${results}    0
    Should Be Equal As Strings    ${result}[ref_name]    ${REF_NAME}
    Should Be Equal As Strings    ${result}[author]      ${AUTHOR}
    Should Be Equal As Strings    ${result}[title]       ${TITLE}
    Should Be Equal As Numbers    ${result}[year]        ${YEAR}
    Should Be Equal As Strings    ${result}[journal]     ${JOURNAL}

Add Article Reference With Incorrect Year
    Go To Add Ref Page
    Set Default Values
    Set Year    1234
    Submit Values
    Page Should Contain    ERROR

Remove Article Reference
    Go To Home Page
    Page Should Contain    ref1
    Scroll Element Into View  id:deleteref1
    Click Button   id:deleteref1
    Handle Alert  ACCEPT
    Go To Home Page
    Page Should Not Contain    ref1

Reference Is Not Removed If Pop Up Is Cancelled
    Go To Home Page
    Page Should Contain    ref1
    Scroll Element Into View  id:deleteref1
    Click Button   id:deleteref1
    Handle Alert  DISMISS
    Go To Home Page
    Page Should Contain    ref1


*** Keywords ***
Set Ref type
    [Arguments]  ${type}
    Select From List By Value  id:typeSelect  ${type}

Set Ref Name
    [Arguments]  ${refname}
    Input Text  refname  ${refname}

Set Author
    [Arguments]  ${refname}
    Input Text  author     ${AUTHOR}

Set Title
    [Arguments]  ${title}
    Input Text  title      ${title}

Set Year
    [Arguments]  ${year}
    Input Text  year       ${year}

Set Journal
    [Arguments]  ${journal}
    Input Text  journal  ${journal}


Set Default Values
    Set Ref type  ${type}
    Set Ref Name  ${REF_NAME}
    Set author  ${AUTHOR}
    Set Title  ${TITLE}
    Set Year  ${YEAR}
    Set Journal  ${JOURNAL}

Submit Values
    Click Button  Add
