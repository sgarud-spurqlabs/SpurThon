from behave import *
import time

#use_step_matcher("re")
use_step_matcher("parse")



@given("I am on Calculator homepage")
def step_impl(context):
    print("use is on calc page")

@when('I enter "{n}" in calculator')
def step_impl(context, n):
    context.calcpage.EnterNumber(n)


@step('I press "{op}"')
def step_impl(context, op):
     context.calcpage.selectOperation(op)

@then('I see the result is "{res}"')
def step_impl(context, res):
    actual_result = context.calcpage.ReturnResult()
    print(actual_result)
    assert actual_result == res
    time.sleep(1)