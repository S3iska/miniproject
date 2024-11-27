*** Settings ***
Library  ../RefLibrary.py
Library  Collections
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser

*** Variables ***
${REF_NAME}       testref
${AUTHOR}         Test Author
${TITLE}          Test Title
${YEAR}           2020
${PUBLISHER}      Test Publisher

*** Test Cases ***
Add Article Reference and Verify in Database
    # Add a new reference via the web form
    Go To Add Ref Page
    Set Default Values
    Submit Values

    # Verify the reference is stored in the database
    ${criteria}=    Create Dictionary    ref_name=${REF_NAME}    author=${AUTHOR}    title=${TITLE}    year=${YEAR}    publisher=${PUBLISHER}
    ${results}=     Get Refs From Database    &{criteria}

    # Assert that the reference exists
    Should Not Be Empty    ${results}    No references found for criteria: ${criteria}

    # Assert the specific values match
    ${result}=      Get From List    ${results}    0
    Should Be Equal As Strings    ${result}[ref_name]    ${REF_NAME}
    Should Be Equal As Strings    ${result}[author]      ${AUTHOR}
    Should Be Equal As Strings    ${result}[title]       ${TITLE}
    Should Be Equal As Numbers    ${result}[year]        ${YEAR}
    Should Be Equal As Strings    ${result}[publisher]   ${PUBLISHER}

Add Article Referance With Incorrect Year
    Go To Add Ref Page
    Set Default Values
    Set Year    1234
    Submit Values
    Page Should Contain    Could not add reference


*** Keywords ***
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

Set Publisher
    [Arguments]  ${publisher}
    Input Text  publisher  ${publisher}


Set Default Values
    Set Ref Name  ${REF_NAME}
    Set author  ${AUTHOR}
    Set Title  ${TITLE}
    Set Year  ${YEAR}
    Set Publisher  ${PUBLISHER}

Submit Values
    Click Button  Lisää
