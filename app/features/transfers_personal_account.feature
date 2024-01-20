Feature: Personal Account Transfers


 Scenario: User is able to create a new account
   Given Number of accounts in registry equals: "0"
   When I create an account using name: "kurt", last name: "cobain", pesel: "89091209875"
   Then Number of accounts in registry equals: "1"
   And Account with pesel "89091209875" exists in registry

 Scenario: User is able to send incoming transfer
   Given Saldo of account with pesel: "89091209875" equals: "0"
   When I send a transfer with pesel: "89091209875" using amount: "500" and type: "incoming"
   Then Saldo of account with pesel: "89091209875" equals: "500"

 Scenario: User is able to send outgoing transfer
   Given Saldo of account with pesel: "89091209875" equals: "500"
   When I send a transfer with pesel: "89091209875" using amount: "200" and type: "outgoing"
   Then Saldo of account with pesel: "89091209875" equals: "300"

 Scenario: User is able to delete already created account
   Given Account with pesel "89091209875" exists in registry
   When I delete account with pesel: "89091209875"
   Then Account with pesel "89091209875" does not exist in registry
 