Feature: Update the customer based on id
  As a service I want to update the customer details.

  Scenario: Updating the customer name
    Given customer "Nicole Forsgren" with ID "12345" exists
    When I update customer with ID "12345" surname to "Doe"
    Then I should see customer "Nicole Doe"


