*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${SERVER}          localhost:5001
${DELAY}           0.5 seconds
${HOME_URL}        http://${SERVER}
${ADD_URL}         http://${SERVER}/add
${ADD_TAG_URL}     http://${SERVER}/100/add_tags
${ADD_TAG_HREF}    100/add_tags
${BROWSER}         chrome
${HEADLESS}        false

*** Keywords ***
Open And Configure Browser
    IF  $BROWSER == 'chrome'
        ${options}  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys
    ELSE IF  $BROWSER == 'firefox'
        ${options}  Evaluate  sys.modules['selenium.webdriver'].FirefoxOptions()  sys
    END
    IF  $HEADLESS == 'true'
        Set Selenium Speed  0.1
        Call Method  ${options}  add_argument  --headless
        ${window_size}  Set Variable  --window-size=${1920},${3000}
        Call Method  ${options}  add_argument  ${window_size}
    ELSE
        Set Selenium Speed  ${DELAY}
    END
    Open Browser  browser=${BROWSER}  options=${options}

Go To Home Page
    Go To  ${HOME_URL}
    Title Should Be  Miniproject

Go To Add Ref Page
    Go To Home Page
    Click Link  Add a new reference
    Location Should Be  ${ADD_URL}

Go To Add Tag Page
    Go To Home Page
    Click Element   xpath=//a[@href="${ADD_TAG_HREF}"]
    Location Should Be  ${ADD_TAG_URL}
