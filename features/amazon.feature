Feature: Amazon IN app
    Background:
        Given I tap button English
        When I tap continue button
        And I skip signin

    @smoke
    Scenario: Home Screen opening verification
        Then I see amazon logo

    @regression
    Scenario: Verify Sections Headers are displayed on Home Screen
        When I scroll down to Pocket friendly stores on Home Screen
        Then I see top picks under 199 image

    @interruption
    Scenario: Verify incoming call interruption
        When I scroll down to Pocket friendly stores on Home Screen
        And I receive incoming call
        And I accept incoming call
        And I cancel incoming call
        And I tap navi burger
        Then I see "Hell. Sign In" in side menu header





