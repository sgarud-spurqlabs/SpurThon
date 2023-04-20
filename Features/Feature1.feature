
Feature:To verify calculator functions
  @101 @calc
	Scenario: Verify Addition of two numbers
		Given I am on Calculator homepage
		When I enter "200" in calculator
		And I press "+"
		And I enter "100" in calculator
		Then I see the result is "300"

	@102 @calc
   Scenario Outline: Verify Basic operations
		Given I am on Calculator homepage
		When I enter "<n>" in calculator
		And I press "<op>"
		And I enter "<m>" in calculator
		Then I see the result is "<res>"
		Examples:
			| n   | op |m  | res |
			| 200 | *  |10 | 2000|
			| 20  | -  |10 | 10  |
			| 500 | /  |5  | 100 |