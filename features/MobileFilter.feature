Feature: Mobile Category

    Scenario: Open Mobile Category and Verify filters
        Given launch chrome browser
        When Flipkart home page opens
        Then Click Mobile Category
        And Click First phone
        And Verify Filter text on left navbar
        And Set price filter to 20000
        And Close Browser