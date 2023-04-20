pip install --upgrade pip  //incase if pip install gives error

Use pip install -r requirements.txt to install dependencies

To run allure report
Add allure-behave extension in python environment (pycharm)
install allure package in your device

To generate allure reports in json format command is ....
behave Feature1.feature -f allure_behave.formatter:AllureFormatter -o ReportFolder
Example - behave Features/SignIn.feature -f allure_behave.formatter:AllureFormatter -o Report_Json

To generate HTML report from JSON reports use command....
allure generate Folder_with_JSON_Reports -o Foldername_to_store_allure_HTML_Report --clean
Example - allure generate Report_Json -o Report_Html --clean

To tun PythonicRunner.py from cmd - python PythonicRunner.py


