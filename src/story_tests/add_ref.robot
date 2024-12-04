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
${PAGES}          123-132
${MONTH}          January
${DOI}            10.1000/182
${NOTE}           Test Note
${KEY}            Test Key
${PUBLISHER}      Test Publisher
${SERIES}         Test Series
${ADDRESS}        Test Address
${EDITION}        Test Edition
${URL}            Test URL
${BOOKTITLE}      Test Book Title
${EDITOR}         Test Editor
${ORGANIZATION}   Test Organization

*** Test Cases ***
Add Full Article Reference and Verify in Database
    Go To Add Ref Page
    Set Ref type  article
    Input Text  xpath=//div[@id='articleForm']//form//input[@name='ref_name']  ${REF_NAME}
    Input Text  xpath=//div[@id='articleForm']//form//input[@name='author']    ${AUTHOR}
    Input Text  xpath=//div[@id='articleForm']//form//input[@name='title']     ${TITLE}
    Input Text  xpath=//div[@id='articleForm']//form//input[@name='journal']   ${JOURNAL}
    Input Text  xpath=//div[@id='articleForm']//form//input[@name='year']      ${YEAR}
    Input Text  xpath=//div[@id='articleForm']//form//input[@name='volume']    ${VOLUME}
    Input Text  xpath=//div[@id='articleForm']//form//input[@name='month']     ${MONTH}
    Input Text  xpath=//div[@id='articleForm']//form//input[@name='pages']     ${pages}
    Input Text  xpath=//div[@id='articleForm']//form//input[@name='doi']       ${DOI}
    Input Text  xpath=//div[@id='articleForm']//form//input[@name='note']      ${NOTE}
    Input Text  xpath=//div[@id='articleForm']//form//input[@name='key']       ${KEY}
    Click Button  xpath=//div[@id='articleForm']//form//button

    ${criteria}=  Create Dictionary
    Set To Dictionary    ${criteria}    ref_type=article
    Set To Dictionary    ${criteria}    ref_name=${REF_NAME}
    Set To Dictionary    ${criteria}    author=${AUTHOR}
    Set To Dictionary    ${criteria}    title=${TITLE}
    Set To Dictionary    ${criteria}    journal=${JOURNAL}
    Set To Dictionary    ${criteria}    year=${YEAR}
    Set To Dictionary    ${criteria}    volume=${VOLUME}
    Set To Dictionary    ${criteria}    pages=${PAGES}
    Set To Dictionary    ${criteria}    month=${MONTH}
    Set To Dictionary    ${criteria}    doi=${DOI}
    Set To Dictionary    ${criteria}    note=${NOTE}
    Set To Dictionary    ${criteria}    key=${KEY}

    ${results}=     Get Refs From Database    &{criteria}
    Should Not Be Empty    ${results}    No references found for criteria: ${criteria}

Add Full Book Reference and Verify in Database
    Go To Add Ref Page
    Set Ref type   book
    Input Text  xpath=//div[@id='bookForm']//form//input[@name='ref_name']   ${REF_NAME}
    Input Text  xpath=//div[@id='bookForm']//form//input[@name='author']     ${AUTHOR}
    Input Text  xpath=//div[@id='bookForm']//form//input[@name='title']      ${TITLE}
    Input Text  xpath=//div[@id='bookForm']//form//input[@name='publisher']  ${PUBLISHER}
    Input Text  xpath=//div[@id='bookForm']//form//input[@name='year']       ${YEAR}
    Input Text  xpath=//div[@id='bookForm']//form//input[@name='volume']     ${VOLUME}
    Input Text  xpath=//div[@id='bookForm']//form//input[@name='series']     ${SERIES}
    Input Text  xpath=//div[@id='bookForm']//form//input[@name='address']    ${ADDRESS}
    Input Text  xpath=//div[@id='bookForm']//form//input[@name='edition']    ${EDITION}
    Input Text  xpath=//div[@id='bookForm']//form//input[@name='month']      ${MONTH}
    Input Text  xpath=//div[@id='bookForm']//form//input[@name='note']       ${NOTE}
    Input Text  xpath=//div[@id='bookForm']//form//input[@name='key']        ${KEY}
    Input Text  xpath=//div[@id='bookForm']//form//input[@name='url']        ${URL}
    Click Button  xpath=//div[@id='bookForm']//form//button

    ${criteria}=  Create Dictionary
    Set To Dictionary    ${criteria}    ref_type=book
    Set To Dictionary    ${criteria}    ref_name=${REF_NAME}
    Set To Dictionary    ${criteria}    author=${AUTHOR}
    Set To Dictionary    ${criteria}    title=${TITLE}
    Set To Dictionary    ${criteria}    publisher=${PUBLISHER}
    Set To Dictionary    ${criteria}    year=${YEAR}
    Set To Dictionary    ${criteria}    volume=${VOLUME}
    Set To Dictionary    ${criteria}    series=${SERIES}
    Set To Dictionary    ${criteria}    address=${ADDRESS}
    Set To Dictionary    ${criteria}    edition=${EDITION}
    Set To Dictionary    ${criteria}    month=${MONTH}
    Set To Dictionary    ${criteria}    note=${NOTE}
    Set To Dictionary    ${criteria}    key=${KEY}
    Set To Dictionary    ${criteria}    url=${URL}

    ${results}=     Get Refs From Database    &{criteria}
    Should Not Be Empty    ${results}    No references found for criteria: ${criteria}

Add Full Inproceedings Reference and Verify in Database
    Go To Add Ref Page
    Set Ref type  inproceedings
    Input Text  xpath=//div[@id='inproceedingsForm']//form//input[@name='ref_name']      ${REF_NAME}
    Input Text  xpath=//div[@id='inproceedingsForm']//form//input[@name='author']        ${AUTHOR}
    Input Text  xpath=//div[@id='inproceedingsForm']//form//input[@name='title']         ${TITLE}
    Input Text  xpath=//div[@id='inproceedingsForm']//form//input[@name='booktitle']     ${BOOKTITLE}
    Input Text  xpath=//div[@id='inproceedingsForm']//form//input[@name='year']          ${YEAR}
    Input Text  xpath=//div[@id='inproceedingsForm']//form//input[@name='editor']        ${EDITOR}
    Input Text  xpath=//div[@id='inproceedingsForm']//form//input[@name='volume']        ${VOLUME}
    Input Text  xpath=//div[@id='inproceedingsForm']//form//input[@name='series']        ${SERIES}
    Input Text  xpath=//div[@id='inproceedingsForm']//form//input[@name='pages']         ${PAGES}
    Input Text  xpath=//div[@id='inproceedingsForm']//form//input[@name='address']       ${ADDRESS}
    Input Text  xpath=//div[@id='inproceedingsForm']//form//input[@name='month']         ${MONTH}
    Input Text  xpath=//div[@id='inproceedingsForm']//form//input[@name='organization']  ${ORGANIZATION}
    Input Text  xpath=//div[@id='inproceedingsForm']//form//input[@name='publisher']     ${PUBLISHER}
    Input Text  xpath=//div[@id='inproceedingsForm']//form//input[@name='note']          ${NOTE}
    Input Text  xpath=//div[@id='inproceedingsForm']//form//input[@name='key']           ${KEY}
    Click Button  xpath=//div[@id='inproceedingsForm']//form//button

    ${criteria}=  Create Dictionary
    Set To Dictionary    ${criteria}    ref_type=inproceedings
    Set To Dictionary    ${criteria}    ref_name=${REF_NAME}
    Set To Dictionary    ${criteria}    author=${AUTHOR}
    Set To Dictionary    ${criteria}    title=${TITLE}
    Set To Dictionary    ${criteria}    booktitle=${BOOKTITLE}
    Set To Dictionary    ${criteria}    year=${YEAR}
    Set To Dictionary    ${criteria}    editor=${EDITOR}
    Set To Dictionary    ${criteria}    volume=${VOLUME}
    Set To Dictionary    ${criteria}    series=${SERIES}
    Set To Dictionary    ${criteria}    pages=${PAGES}
    Set To Dictionary    ${criteria}    address=${ADDRESS}
    Set To Dictionary    ${criteria}    month=${MONTH}
    Set To Dictionary    ${criteria}    organization=${ORGANIZATION}
    Set To Dictionary    ${criteria}    publisher=${PUBLISHER}
    Set To Dictionary    ${criteria}    note=${NOTE}
    Set To Dictionary    ${criteria}    key=${KEY}

    ${results}=     Get Refs From Database    &{criteria}
    Should Not Be Empty    ${results}    No references found for criteria: ${criteria}

*** Keywords ***
Set Ref type
    [Arguments]  ${type}
    Select From List By Value  id:typeSelect  ${type}