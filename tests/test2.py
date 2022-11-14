import sys
import unittest
import string
import random

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
EXTERN_CUSTOMER_ID = "EXTERN_CUSTOMER_ID1234"

class TestOrb(unittest.TestCase):

    def test_foo(self):
        self.assertEqual(1, 1, "Should be 1")

    def test_log_event(self):
        rv = o.log_event(CUSTOMER, "asdf", props={"foo": "bar"})
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
        rv = o.amend_event(event_id, CUSTOMER, event_name,
                           timestamp, {"foo": "bar"})
        self.assertEqual(True, rv[0])

    def test_deprecate_event(self):
        rv = o.deprecate_event("87c4b589-78f2-4a0d-9609-fafd7380fd3c")
        self.assertEqual(True, rv[0])

    def test_get_customer(self):
        rv = o.get_customer("UR8dFa28HzuQiNx2")
        self.assertEqual(True, rv[0])

    def test_update_customer(self):
        rv = o.update_customer("gjo6Ab9A7xnhNzrs", "updated name", "stripe@yahoo.com", payment_provider_id="myid", payment_provider="stripe", shipping_address={
                               "city": "string", "country": "US", "line1": "1234 main st", "line2": "string", "postal_code": "string", "state": "string"})
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

    @unittest.expectedFailure
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

    @unittest.expectedFailure
    def test_retrieve_upcoming(self):
        rv = o.retrieve_upcoming("BTMvkWxEccYhTRmZ")
        self.assertEqual(True, rv[0])
        
    def test_list_subscriptions(self):
        rv = o.list_subscriptions()
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

class CustomerSubscriptionTests(unittest.TestCase):
    @classmethod
    def __make_rand(cls):
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=cls.random_k))
    def setUp(self):
        pass
    @classmethod
    def setUpClass(cls):
        print("Setting up customer tests")
        cls.o = Orb(apikey)
        cls.random_k = 12
        cls.customer_name = cls.__make_rand()
        cls.external_customer_id = cls.__make_rand()
        cls.subscription_id = cls.__make_rand()
        cls.customer_id =''
        pass
    def tearDown(self):
        pass
    
    #lazy forcing of test order
    def test_1_create_customer(self):
        rv = o.create_customer(self.customer_id, "stripe2@yahoo.com",  external_customer_id=self.external_customer_id, shipping_address={
                               "city": "string", "country": "US", "line1": "1234 main st", "line2": "string", "postal_code": "string", "state": "string"})
        data_res = rv[1]
        CustomerSubscriptionTests.customer_id = data_res['id']
        self.assertEqual(True, rv[0])

    def test_2_create_subscription(self):
        rv = o.create_subscription(self.customer_id, "eaBB93GA6isQZjoX",  "2022-12-01")
        data_res = rv[1]
        CustomerSubscriptionTests.subscription_id = data_res['id']
        self.assertEqual(True, rv[0])

    @unittest.expectedFailure
    def test_3_retrieve_upcoming(self):
        rv = o.retrieve_upcoming(CustomerSubscriptionTests.subscription_id)
        self.assertEqual(True, rv[0])
    
    def test_4_cancel_subscription(self):
        rv = o.cancel_subscription(CustomerSubscriptionTests.subscription_id, "immediate")
        self.assertEqual(True, rv[0])
    

def run_tests():
    test_classes = [TestOrb, CustomerSubscriptionTests]
    #test_classes = [CustomerSubscriptionTests]

    loader = unittest.TestLoader()
    suites_list = []
    for c in test_classes:
        suite = loader.loadTestsFromTestCase(c)
        suites_list.append(suite)
    big_suite = unittest.TestSuite(suites_list)
    runner = unittest.TextTestRunner()
    results = runner.run(big_suite)
    print(results)

if __name__ == '__main__':
    run_tests()