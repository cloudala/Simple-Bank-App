Feature: Account registry


 Scenario: User is able to create a new account
   Given Number of accounts in registry equals: "0"
   When I create an account using name: "kurt", last name: "cobain", pesel: "89091209875"
   Then Number of accounts in registry equals: "1"
   And Account with pesel "89091209875" exists in registry


 Scenario: User is able to create a second account
   Given Number of accounts in registry equals: "1"
   When I create an account using name: "stevie", last name: "wonder", pesel: "89091209876"
   Then Number of accounts in registry equals: "2"
   And Account with pesel "89091209876" exists in registry


 Scenario: Admin user is able to save the account registry
   When I save the account registry
   Then Number of accounts in registry equals: "2"


 Scenario: User is able to delete already created account
   Given Account with pesel "89091209875" exists in registry
   When I delete account with pesel: "89091209875"
   Then Account with pesel "89091209875" does not exists in registry


 Scenario: User is able to update last name saved in account
   Given Account with pesel "89091209876" exists in registry
   When I update account with pesel: "89091209876" to last name "wonders"
   Then Account with pesel "89091209876" has surname "wonders"


 Scenario: User is able to load account registry
   Given Number of accounts in registry equals: "0"
   And Account with pesel "89091209875" does not exist in registry
   And Account with pesel "89091209876" does not exist in registry
   When I load the account registry
   Then Number of accounts in registry equals: "2"
   And Account with pesel "89091209875" exists in registry
   And Account with pesel "89091209876" exists in registry


 Scenario: User is able to delete both accounts
   Given Account with pesel "89091209875" exists in registry
   And Account with pesel "89091209876" exists in registry
   When I delete account with pesel: "89091209875"
   And I delete account with pesel: "89091209876"
   Then Account with pesel "89091209875" does not exists in registry
   And Account with pesel "89091209876" does not exists in registry