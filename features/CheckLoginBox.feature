Feature: Check Login Box

    Scenario: Login text in home page
        Given launch chrome browser
        When Flipkart home page opens
        Then Verify Login Text is Present
        And Verify Username field is Present
        And Verify Password field is Present
        And Close Browser