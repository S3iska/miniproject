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
    Go To Add Article Page
    Input Text  refname    ${REF_NAME}
    Input Text  author     ${AUTHOR}
    Input Text  title      ${TITLE}
    Input Text  year       ${YEAR}
    Input Text  publisher  ${PUBLISHER}
    Click Button  Lisää

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
   
