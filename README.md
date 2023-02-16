# ***APPIUM BEHAVE PROJECT***

## SET UP TO RUN TESTS

1. Appium server up and running (see config for host and port)
2. Matching emulator up and running

## ALLURE REPORT GENERATION 

CLI commands*:
1. behave -f allure_behave.formatter:AllureFormatter -o ./reports
2.  allure serve ./reports 

*Java, allure-behave package must be installed