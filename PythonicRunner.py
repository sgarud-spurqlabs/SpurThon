import sys
from behave import __main__ as pythnoic_runner
import shutil
import glob
import allure

if __name__=='__main__':
    sys.stdout.flush()
    reporting_folder_name='Report_Json'
    shutil.rmtree(reporting_folder_name,ignore_errors=True)  # removes if any reporting folder exists

    Path1 = 'Features/Feature1/Feature1.feature'
    Path2 = 'Features/Feature2/Feature1.feature'
    FolderPath1 = 'Features/Feature1'
    FolderPath2 = 'Feature2'
    path = 'Features'
    commonrunneroptions = ' --no-capture --no-capture-stderr -f plain '  # from here or using behave.ini file automatically
    taglist1 = "--tags=calc"  # all with tage calc only
    taglist2 = "--tags=-101"  # all except tag 101
    taglist3 = "--tags=103,calc"  # with either of tag tag 103 or tag 105
    taglist4 = "--tags=101 --tags=calc"  # with both tag compulsary tag 101 & tag calc
    # pythnoic_runner_example.main(commonrunneroptions+" "+FolderPath1+" "+taglist1)
    reportingrelated = ' -f allure_behave.formatter:AllureFormatter -o' + reporting_folder_name + ' '  # reporting in json format
    pythnoic_runner.main(path + " " + taglist1 + " " + reportingrelated + " " + commonrunneroptions)




