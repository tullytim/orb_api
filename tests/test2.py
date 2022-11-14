import sys
import unittest

sys.path.append('/home/ubuntu/Orb/src/')

from Orb.Orb import Orb

def header(s):
    BOLD = "\033[1m"
    END = "\033[0m"
    print(f"{BOLD}{s}{END}")

apikey = "63cbfc7a2a00196cf7b67e5434279a5c52e09c246945797aeaedd4cd50e03b96"
o = Orb(apikey, True)
CUSTOMER = "UR8dFa28HzuQiNx2"
event_id_test = "ed085e39-d65f-48ac-9b8f-b0ba0195cfb5"
EXTERN_CUSTOMER_ID="EXTERN_CUSTOMER_ID1234"

class TestOrb(unittest.TestCase):
    def test_foo(self):
        self.assertEqual(1, 1, "Should be 1")

    def test_log_event(self):
        rv = o.log_event(CUSTOMER, "asdf", props={"foo":"bar"})
        self.assertEqual(True, rv[0])

    def test_search_event(self):
        rv = o.search_event([event_id_test])
        self.assertEqual(True, rv[0])

    def test_search_event(self):
        rv = o.search_event([event_id_test])
        self.assertEqual(True, rv[0])
        rv = rv[1]
        timestamp = rv['data'][0]['timestamp']
        event_name = rv['data'][0]['event_name']
        customer = rv['data'][0]['customer_id']
        event_id = rv['data'][0]['id']
        rv = o.amend_event(event_id, CUSTOMER, event_name, timestamp, {"foo":"bar"})
        self.assertEqual(True, rv[0])
    def test_deprecate_event(self):
        rv = o.deprecate_event("87c4b589-78f2-4a0d-9609-fafd7380fd3c")
        self.assertEqual(True, rv[0])
    def test_create_customer(self):
        rv = o.create_customer("extern cust", "stripe2@yahoo.com",  external_customer_id=EXTERN_CUSTOMER_ID, shipping_address={"city": "string","country": "US","line1": "1234 main st","line2": "string","postal_code": "string","state": "string"})
        self.assertEqual(True, rv[0])
    def test_get_customer(self):
        rv = o.get_customer("UR8dFa28HzuQiNx2")
        self.assertEqual(True, rv[0])
    def test_update_customer(self):
        rv = o.update_customer("gjo6Ab9A7xnhNzrs", "updated name", "stripe@yahoo.com", payment_provider_id="myid", payment_provider="stripe", shipping_address={"city": "string","country": "US","line1": "1234 main st","line2": "string","postal_code": "string","state": "string"})
        self.assertEqual(True, rv[0])
    def test_check_availability(self):
        rv = o.check_availability()
        self.assertEqual(True, rv[0])
    def test_view_external_customer(self):
        rv = o.view_external_customer(EXTERN_CUSTOMER_ID)
        self.assertEqual(True, rv[0])
    def test_view_external_customer_costs(self):
        rv = o.view_external_customer_costs(EXTERN_CUSTOMER_ID)
        self.assertEqual(True, rv[0])
    def test_retrieve_credit(self):
        rv = o.retrieve_credit_balance("DE9C9zcXjq8HwB4f")
        self.assertEqual(True, rv[0])
    def test_get_balance_transactions(self):
        rv = o.get_balance_transactions("DE9C9zcXjq8HwB4f")
        self.assertEqual(True, rv[0])
    def test_credits_ledger_add(self):
        rv = o.credits_ledger_add("UR8dFa28HzuQiNx2", 100.0, 'increment')
        self.assertEqual(True, rv[0])

    def _test_view_credits_ledger(self):
        rv = o.view_credits_ledger("UR8dFa28HzuQiNx2")
        self.assertEqual(True, rv[0])

    def test_list_invoices(self):
        rv = o.list_invoices()
        self.assertEqual(True, rv[0])

    def test_get_invoice(self):
        rv = o.get_invoice("gYN9QyrAXQgR8cKR")
        self.assertEqual(True, rv[0])

    def test_retrieve_upcoming(self):
        rv = o.retrieve_upcoming("BTMvkWxEccYhTRmZ")
        self.assertEqual(True, rv[0])

    def test_create_subscription(self):
        rv = o.create_subscription("LP3AYZcMEgh5WwkR", "eaBB93GA6isQZjoX",  "2022-12-01")
        self.assertEqual(True, rv[0])

    def test_list_subscriptions(self):
        rv = o.list_subscriptions()
        self.assertEqual(True, rv[0])

    def test_cancel_subscription(self):
        rv = o.cancel_subscription("mPkuo4atfnK6AMrs", "immediate")
        self.assertEqual(True, rv[0])
    def test_retrieve_plan(self):
        rv = o.retrieve_plan("MZogb5HsiNpPDXBG")
        self.assertEqual(True, rv[0])

    def test_retrieve_subscription(self):
        rv = o.retrieve_subscription("mPkuo4atfnK6AMrs")
        self.assertEqual(True, rv[0])


    def test_view_subscription_usage(self):
        rv = o.view_subscription_usage("mPkuo4atfnK6AMrs")
        self.assertEqual(True, rv[0])

    def test_view_subscription_costs(self):
        rv = o.view_subscription_costs("mPkuo4atfnK6AMrs")
        self.assertEqual(True, rv[0])

    def test_view_subscription_schedule(self):
        rv = o.view_subscription_schedule("mPkuo4atfnK6AMrs")
        self.assertEqual(True, rv[0])

    def test_list_plans(self):
        rv = o.list_plans()
        self.assertEqual(True, rv[0])


if __name__ == '__main__':
    pass
    unittest.main()

header("Log Event")
rv = o.log_event(CUSTOMER, "asdf", props={"foo":"bar"})
print(rv, "\n")

rv = o.search_event([event_id_test])
rv = rv[1]
timestamp = rv['data'][0]['timestamp']
event_name = rv['data'][0]['event_name']
customer = rv['data'][0]['customer_id']
event_id = rv['data'][0]['id']

o.amend_event(event_id, CUSTOMER, event_name, timestamp, {"foo":"bar"})
o.deprecate_event("87c4b589-78f2-4a0d-9609-fafd7380fd3c")

print("Test Print")
print(o)
print(repr(o))
EXTERN_CUSTOMER_ID="EXTERN_CUSTOMER_ID1234"

header("Create Customer")
o.create_customer("extern cust", "stripe2@yahoo.com",  external_customer_id=EXTERN_CUSTOMER_ID, shipping_address={"city": "string","country": "US","line1": "1234 main st","line2": "string","postal_code": "string","state": "string"})
#o.list_customers()

header("Get Customer: ")
o.get_customer("UR8dFa28HzuQiNx2")
#header("View Customer Costs")
#o.view_customer_costs("UR8dFa28HzuQiNx2")
header("Update Customer")
o.update_customer("gjo6Ab9A7xnhNzrs", "updated name", "stripe@yahoo.com", payment_provider_id="myid", payment_provider="stripe", shipping_address={"city": "string","country": "US","line1": "1234 main st","line2": "string","postal_code": "string","state": "string"})
header("Check Availability")
o.check_availability()
header("View extern customer")
o.view_external_customer(EXTERN_CUSTOMER_ID)
header("View EXTERN COSTS")
o.view_external_customer_costs(EXTERN_CUSTOMER_ID)
header("Retrieve Credit Balance")
o.retrieve_credit_balance("DE9C9zcXjq8HwB4f")
header("Get Balance Transactions")
o.get_balance_transactions("DE9C9zcXjq8HwB4f")

header("Add Credits Ledger")
o.credits_ledger_add("UR8dFa28HzuQiNx2", 100.0, 'increment')
header("View Credits Ledger")
o.view_credits_ledger("UR8dFa28HzuQiNx2")
header("List Invoices")
o.list_invoices()

header("Get Invoice")
o.get_invoice("gYN9QyrAXQgR8cKR")

header("Retrieve Upcoming")
o.retrieve_upcoming("BTMvkWxEccYhTRmZ")

header("Create Subscription")
o.create_subscription("LP3AYZcMEgh5WwkR", "eaBB93GA6isQZjoX",  "2022-12-01")

header("List Subscriptions")
o.list_subscriptions()

header("Cancel Subscription")
o.cancel_subscription("mPkuo4atfnK6AMrs", "immediate")

header("Retrieve Plan")
o.retrieve_plan("MZogb5HsiNpPDXBG")

header("Retrieve Subscription")
o.retrieve_subscription("mPkuo4atfnK6AMrs")

header("View Subscription Usage")
o.view_subscription_usage("mPkuo4atfnK6AMrs")

header("View Subscription Costs")
o.view_subscription_costs("mPkuo4atfnK6AMrs")

header("View Subscription Schedule")
o.view_subscription_schedule("mPkuo4atfnK6AMrs")

header("List Plans")
o.list_plans()