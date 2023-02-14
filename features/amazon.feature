Feature: Amazon IN app
    Background:
        Given I tap button English
        When I tap continue button
        And I skip signin

    Scenario: Verify home screen opens
        Then I see amazon logo

    Scenario Outline: Verify 'Pocket friendly' section is displayed
        Then I scroll down to text '<header>'

        Examples:
        |header|
        |Pocket friendly stores|
        |Curated stores for you|

