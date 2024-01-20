from behave import *
# from selenium.webdriver.common.keys import Keys
import requests
from unittest_assertions import AssertEqual


assert_equal = AssertEqual()
URL = "http://localhost:5000"

# Scenario 1
@when('I create an account using name: "{name}", last name: "{last_name}", pesel: "{pesel}"')
def create_account(context, name, last_name, pesel):
    json_body = {"name": name, "surname": last_name, "pesel": pesel}
    create_resp = requests.post(URL + "/api/accounts", json=json_body)
    assert_equal(create_resp.status_code, 201)

@step('Number of accounts in registry equals: "{count}"')
def check_account_count_in_registry(context, count):
    ile_kont = requests.get(URL + f"/api/accounts/count")
    assert_equal(ile_kont.json()["count"], int(count))

@then('Account with pesel "{pesel}" exists in registry')
def account_exists_in_registry(context, pesel):
    get_account_resp = requests.get(URL + f"/api/accounts/{pesel}")
    assert_equal(get_account_resp.status_code, 200)

@given('Account with pesel "{pesel}" exists in registry')
def given_account_exists_in_registry(context, pesel):
    get_account_resp = requests.get(URL + f"/api/accounts/{pesel}")
    assert_equal(get_account_resp.status_code, 200)

@given('Account with pesel "{pesel}" does not exist in registry')
def given_account_does_not_exist_in_registry(context, pesel):
   get_account_resp = requests.get(URL + f"/api/accounts/{pesel}")
   assert_equal(get_account_resp.status_code, 404)

@when('I save the account registry')
def save_account_registry(context):
    save_account_resp = requests.patch(URL  + f"/api/accounts/save")
    assert_equal(save_account_resp.status_code, 200)

@when('I delete account with pesel: "{pesel}"')
def delete_account(context, pesel):
    delete_account_resp = requests.delete(URL + f"/api/accounts/{pesel}")
    assert_equal(delete_account_resp.status_code, 200)

@step('Account with pesel "{pesel}" does not exist in registry')
def check_if_account_with_pesel_exists(context, pesel):
    get_account_resp = requests.get(URL + f"/api/accounts/{pesel}")
    assert_equal(get_account_resp.status_code, 404)

@when('I update account with pesel: "{pesel}" to last name: "{last_name}"')
def update_surname(context, pesel, last_name):
    json_body = {"surname": last_name}
    patch_account_resp = requests.patch(URL + f"/api/accounts/{pesel}", json=json_body)
    assert_equal(patch_account_resp.status_code, 200)

@then('Account with pesel "{pesel}" has surname "{last_name}"')
def check_updated_surname(context, pesel, last_name):
    get_account_resp = requests.get(URL + f"/api/accounts/{pesel}")
    assert_equal(get_account_resp.json()["surname"], last_name)

@when('I load the account registry')
def load_account_registry(context):
    load_account_resp = requests.patch(URL  + f"/api/accounts/load")
    assert_equal(load_account_resp.status_code, 200)

# Transfer-specific steps
@given('Saldo of account with pesel: "{pesel}" equals: "{saldo}"')
@then('Saldo of account with pesel: "{pesel}" equals: "{saldo}"')
def check_account_saldo(context, pesel, saldo):
    saldo_number = float(saldo)
    get_account_resp = requests.get(URL + f"/api/accounts/{pesel}")
    assert_equal(get_account_resp.status_code, 200)
    assert_equal(get_account_resp.json()["saldo"], saldo_number)

@when('I send a transfer with pesel: "{pesel}" using amount: "{saldo}" and type: "{type}"')
def check_transfer_outcome(context, pesel, saldo, type):
    json_body = {"amount": float(saldo), "type": type }
    transfer_resp = requests.post(URL + f"/api/accounts/{pesel}/transfer", json=json_body)
    assert_equal(transfer_resp.status_code, 200)