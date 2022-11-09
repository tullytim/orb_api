import requests
import json
import datetime
import uuid

class Orb:
    __slots__ = 'api_key', 'debug'

    @property
    def endpoint_url(self):
        return "https://api.billwithorb.com/v1"

    def __init__(self, apikey, debug=False):
        self.api_key = apikey
        self.debug = debug
        print(type(self.debug))

    def __gen_idem():
        return str(uuid.uuid4())

    def log_event(self, customer_id, eventname, idempotency_key=__gen_idem(), props={}, timestamp=datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")):
        endpoint = "/ingest"
        data = {"events":[{"idempotency_key": idempotency_key, "customer_id":customer_id, "event_name":eventname, "timestamp":timestamp, "properties":props}]}
        return self.__docall(endpoint, data)

    def search_event(self, eventids):
        endpoint = "/events/search"
        data = {"event_ids":eventids}
        return self.__docall(endpoint, data)

    def amend_event(self, eventid, customer_id, eventname, timestamp, props={}):
        endpoint = f"/events/{eventid}"
        data = {"customer_id":customer_id, "event_name":eventname, "timestamp":timestamp, "properties":props}
        return self.__docall(endpoint, data, 'put')

    def deprecate_event(self, eventid):
        endpoint = f"/events/{eventid}/deprecate"
        return self.__docall(endpoint, {}, 'put')

    def list_customers(self):
        endpoint = "/customers"
        return self.__docall(endpoint, {}, 'get')

    def create_customer(self, name, email, **kwargs):
        endpoint = "/customers"
        data = {"name":name, "email":email} 
        data.update(kwargs)
        return self.__docall(endpoint, data, 'post')

    def get_customer(self, customer_id):
        endpoint = f"/customers/{customer_id}"
        return self.__docall(endpoint, {}, 'get')

    def update_customer(self, customer_id, name, email, **kwargs):
        endpoint = f"/customers/{customer_id}"
        data = {"name":name, "email":email} 
        data.update(kwargs)
        return self.__docall(endpoint, data, 'put')

    def view_customer_costs(self, customer_id):
        endpoint = f"/customers/{customer_id}/costs"
        return self.__docall(endpoint, {}, 'get')

#External Customer APIs
    def view_external_customer(self, external_customer_id):
        endpoint = f"/customers/external_customer_id/{external_customer_id}"
        return self.__docall(endpoint, {}, 'get')

    def view_external_customer_costs(self, external_customer_id):
        endpoint = f"/customers/external_customer_id/{external_customer_id}/costs"
        return self.__docall(endpoint, {}, 'get')

    def get_balance_transactions(self, customer_id):
        endpoint = "/customers/" + customer_id + "/balance_transactions"
        return self.__docall(endpoint, {}, 'get')

#Credit APIs
    def retrieve_credit_balance(self, customer_id):
        endpoint = "/customers/" + customer_id + "/credits"
        return self.__docall(endpoint, {}, 'get')

    def view_credits_ledger(self, customer_id):
        endpoint = "/customers/" + customer_id + "/credits/ledger"
        return self.__docall(endpoint, {}, 'get')

    def credits_ledger_add(self, customer_id, amount, ledger_type, **kwargs):
        endpoint = "/customers/" + customer_id + "/credits/ledger_entry"
        data = {"amount":amount, "entry_type":ledger_type}
        data.update(kwargs)
        return self.__docall(endpoint, data)

#Invoices
    def list_invoices(self):
        endpoint = "/invoices"
        return self.__docall(endpoint, {}, 'get')

    def get_invoice(self, invoice_id):
        endpoint = f"/invoices/{invoice_id}/"
        return self.__docall(endpoint, {}, 'get')

    def retrieve_upcoming(self, subscription_id):
        endpoint = f"/invoices/upcoming?subscription_id={subscription_id}"
        return self.__docall(endpoint, {}, 'get')


#Misc APIs
    def check_availability(self):
        endpoint = "/ping"
        return self.__docall(endpoint, {}, 'get')

# Start Internal
    def __builduri(self, endpoint):
        return "".join([self.endpoint_url, endpoint, "?debug=true" if self.debug == True else ""])

    def __docall(self, endpoint, payload, http_verb='post'):
        uri = self.__builduri(endpoint)
        print("URI: ", uri)
        jsonblob = json.dumps(payload)
        print("VERB: ", http_verb, "Payload: ", jsonblob)
        headers = {'Content-Type': 'application/json', 'Authorization':'Bearer ' + self.api_key}
        response = requests.request(http_verb, uri,
            headers=headers,
            data=jsonblob
        )
        print(response.content)
        return json.loads(response.content)

    def __str__(self):
        BOLD = "\033[1m"
        END = "\033[0m"
        return f"Orb API Object:\n\t{BOLD}endpoint:{END}{self.endpoint_url}\n\t{BOLD}apikey:{END}{self.api_key}"
