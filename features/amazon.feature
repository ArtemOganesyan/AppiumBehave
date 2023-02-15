Feature: Amazon IN app
    Background:
        Given I tap button English
        When I tap continue button
        And I skip signin

    @test1
    Scenario: Home Screen opening verification
        Then I see amazon logo

    @test2
    Scenario: Verify Sections Headers are displayed on Home Screen
        When I scroll down to Pocket friendly stores on Home Screen
        Then I see top picks under 199 image


