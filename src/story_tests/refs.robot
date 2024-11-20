*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser

*** Test Cases ***
Add Article Reference
    Go To Add Article Page
    Input Text  refname    testref
    Input Text  author     Test Author
    Input Text  title      Test Title
    Input Text  year       2020
    Input Text  publisher  Test Publisher
    Click Button  Add
