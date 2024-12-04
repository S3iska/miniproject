*** Settings ***
Library  ../RefLibrary.py
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup  Setup Test Db

*** Test Cases ***
BibTex is Shown correctly
    Go To Home Page
    Page Should Contain    @article{ref1,
    Page Should Contain    author = {John Doe},
    Page Should Contain    title = {Dah Wah},
    Page Should Contain    year = {1999},
    Page Should Contain    journal = {ABC}