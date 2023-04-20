## 1)To run tests first need to install Selenium
pip install selenium

## 2)Install Webdriver Manager
pip install webdriver-manager

## 3)Install Behave
pip install behave

## 4)Install Allure to generate the report
pip install allure-behave
pip install allure-python-commons

## 5)To run all the feature file
behave Features -f allure_behave.formatter:AllureFormatter -o Report_Json

## 6)To run single feature file
behave Features/SignIn.feature -f allure_behave.formatter:AllureFormatter -o Report_Json

## 7)To run test cases using Tag name from single feature file
behave Features/SignIn.feature --tags=mobile  -f allure_behave.formatter:AllureFormatter -o Report_Json

## 8)To run test cases using Tag name from all feature files
behave Features --tags=mobile -f allure_behave.formatter:AllureFormatter -o Report_Json

## 9)To generate HTML report from JSON report
allure generate Report_Json -o Report_Html --clean

