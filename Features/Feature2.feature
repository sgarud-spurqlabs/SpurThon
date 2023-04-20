
Feature:To verify math functions


    @calc
	Scenario: Verify cos function
		Given I am on Calculator homepage
		When I press "cos"
		And I enter "180" in calculator
		And I press "="
		Then I see the result is "-1"
