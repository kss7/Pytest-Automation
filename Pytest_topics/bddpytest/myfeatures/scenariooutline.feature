Feature: Scenario outlines

  Scenario Outline: Scene Outline Test
        Given there are <start> cucumbers
        When I deposit <deposit> cucumbers
        And I withdraw <withdraw> cucumbers
        Then I should have <final> cucumbers

        Examples:
        | start | deposit | withdraw | final |
        |  12   |   5     |   7      |  10   |
        |  10   |   5     |   20     | -7    |
        |  10   |   5     |   20     | -5    |


##It’s possible to declare example table once for the whole feature, and it can be shared among all the scenarios of that feature: