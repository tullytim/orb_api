# Copyright 2022 Menlo Ventures
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import datetime
import json
import uuid
import requests
from termcolor import colored


class Orb:
    """
    Simple API interface for Orb - works for all aspects of the published REST API.

    Attributes
    ----------
    api_key : str
        the api key for the Orb account
    debug : bool
        indicates whether we are in debug mode

    Methods
    -------
    """
    __slots__ = 'api_key', 'debug'

    @property
    def endpoint_url(self):
        return "https://api.billwithorb.com/v1"

    def __init__(self, apikey, debug=False):
        self.api_key = apikey
        self.debug = debug

    def __gen_idem():
        return str(uuid.uuid4())

    def log_event(self, customer_id, eventname, idempotency_key=__gen_idem(), props={}, timestamp=datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")):
        endpoint = "/ingest"
        data = {"events": [{"idempotency_key": idempotency_key, "customer_id": customer_id,
                            "event_name": eventname, "timestamp": timestamp, "properties": props}]}
        return self.__docall(endpoint, data)

    def search_event(self, eventids):
        endpoint = "/events/search"
        data = {"event_ids": eventids}
        return self.__docall(endpoint, data)

    def amend_event(self, eventid, customer_id, eventname, timestamp, props={}):
        endpoint = f"/events/{eventid}"
        data = {"customer_id": customer_id, "event_name": eventname,
                "timestamp": timestamp, "properties": props}
        return self.__docall(endpoint, data, 'put')

    def deprecate_event(self, eventid):
        endpoint = f"/events/{eventid}/deprecate"
        return self.__docall(endpoint, {}, 'put')

    def list_customers(self):
        endpoint = "/customers"
        return self.__docall(endpoint, {}, 'get')

    def create_customer(self, name, email, **kwargs):
        endpoint = "/customers"
        data = {"name": name, "email": email}
        data.update(kwargs)
        return self.__docall(endpoint, data, 'post')

    def get_customer(self, customer_id):
        endpoint = f"/customers/{customer_id}"
        return self.__docall(endpoint, {}, 'get')

    def update_customer(self, customer_id, name, email, **kwargs):
        endpoint = f"/customers/{customer_id}"
        data = {"name": name, "email": email}
        data.update(kwargs)
        return self.__docall(endpoint, data, 'put')

    def view_customer_costs(self, customer_id):
        endpoint = f"/customers/{customer_id}/costs"
        return self.__docall(endpoint, {}, 'get')

# External Customer APIs
    def view_external_customer(self, external_customer_id):
        endpoint = f"/customers/external_customer_id/{external_customer_id}"
        return self.__docall(endpoint, {}, 'get')

    def view_external_customer_costs(self, external_customer_id):
        endpoint = f"/customers/external_customer_id/{external_customer_id}/costs"
        return self.__docall(endpoint, {}, 'get')

    def get_balance_transactions(self, customer_id):
        endpoint = "/customers/" + customer_id + "/balance_transactions"
        return self.__docall(endpoint, {}, 'get')

# Credit APIs
    def retrieve_credit_balance(self, customer_id):
        endpoint = "/customers/" + customer_id + "/credits"
        return self.__docall(endpoint, {}, 'get')

    def view_credits_ledger(self, customer_id):
        endpoint = "/customers/" + customer_id + "/credits/ledger"
        return self.__docall(endpoint, {}, 'get')

    def credits_ledger_add(self, customer_id, amount, ledger_type, **kwargs):
        endpoint = "/customers/" + customer_id + "/credits/ledger_entry"
        data = {"amount": amount, "entry_type": ledger_type}
        data.update(kwargs)
        return self.__docall(endpoint, data)

# Invoices
    def list_invoices(self):
        endpoint = "/invoices"
        return self.__docall(endpoint, {}, 'get')

    def get_invoice(self, invoice_id):
        endpoint = f"/invoices/{invoice_id}/"
        return self.__docall(endpoint, {}, 'get')

    def retrieve_upcoming(self, subscription_id):
        endpoint = f"/invoices/upcoming?subscription_id={subscription_id}"
        return self.__docall(endpoint, {}, 'get')
# Subscriptions

    def list_subscriptions(self):
        endpoint = "/subscriptions"
        return self.__docall(endpoint, {}, 'get')

    def create_subscription(self, customer_id, plan_id, start_date, **kwargs):
        endpoint = f"/subscriptions"
        data = {"customer_id": customer_id,
                "plan_id": plan_id, "start_date": start_date}
        data.update(kwargs)
        return self.__docall(endpoint, data, 'post')

    def view_subscription_usage(self, subscription_id):
        endpoint = f"/subscriptions/{subscription_id}/usage"
        return self.__docall(endpoint, {}, 'get')

    def view_subscription_costs(self, subscription_id):
        endpoint = f"/subscriptions/{subscription_id}/costs"
        return self.__docall(endpoint, {}, 'get')

    def cancel_subscription(self, subscription_id, cancel_option):
        if cancel_option != "immediate" and cancel_option != "end_of_subscription_term":
            raise ValueError(
                "cancel_option should be one of \"immediate\" or \"end_of_subscription_term\"")
        endpoint = f"/subscriptions/{subscription_id}/cancel"
        return self.__docall(endpoint, {"cancel_option": cancel_option}, 'post')

# untested
    def unschedule_pending_plan_changes(self, subscription_id):
        endpoint = f"/subscriptions/{subscription_id}/unschedule_pending_plan_changes"
        return self.__docall(endpoint, {}, 'post')

    def unschedule_pending_cancellation(self, subscription_id):
        endpoint = f"/subscriptions/{subscription_id}/unschedule_cancellation"
        return self.__docall(endpoint, {}, 'post')

    def view_subscription_schedule(self, subscription_id):
        endpoint = f"/subscriptions/{subscription_id}/schedule"
        return self.__docall(endpoint, {}, 'get')

    def retrieve_subscription(self, subscription_id):
        endpoint = f"/subscriptions/{subscription_id}"
        return self.__docall(endpoint, {}, 'get')

# Plans
    def retrieve_plan(self, plan_id):
        endpoint = f"/plans/{plan_id}"
        return self.__docall(endpoint, {}, 'get')

    def list_plans(self):
        endpoint = f"/plans/"
        return self.__docall(endpoint, {}, 'get')

#not tested
    def retrieve_plan_with_external_id(self, external_plan_id):
        endpoint = f"/plans/external_plan_id/{external_plan_id}"
        return self.__docall(endpoint, {}, 'get')


# Misc APIs

    def check_availability(self):
        endpoint = "/ping"
        return self.__docall(endpoint, {}, 'get')

    def __eq__(self, other):
        return True if self.api_key == other.api_key else False

# Start Internal
    def __http_term_colored(self, code):
        if (code >= 200 and code < 300):
            return colored(code, 'green')
        return colored(code, 'red')

    def __builduri(self, endpoint):
        uri = "".join([self.endpoint_url, endpoint])
        if(not self.debug):
            return uri
        if("?" in endpoint):
            uri = f"{uri}&debug=true"
        else:
            uri = f"{uri}?debug=true"
        return uri

    def __docall(self, endpoint, payload, http_verb='post'):
        uri = self.__builduri(endpoint)
        if self.debug:
            print(f"URI: {uri}")
        jsonblob = json.dumps(payload)
        if self.debug:
            print(f"HTTP Verb: {http_verb}, Payload:, {jsonblob}")
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'Bearer ' + self.api_key}
        response = requests.request(http_verb, uri,
                                    headers=headers,
                                    data=jsonblob
                                    )
        if self.debug:
            print(
                f"Got {self.__http_term_colored(response.status_code)}: {response.content}")
        return (response.status_code >= 200 and response.status_code < 300, json.loads(response.content), response.status_code)

    def __repr__(self):
        return f"Orb(\"{self.api_key}\", {self.debug})"

    def __str__(self):
        BOLD = "\033[1m"
        END = "\033[0m"
        return f"Orb API Object:\n\t{BOLD}endpoint:{END}{self.endpoint_url}\n\t{BOLD}apikey:{END}{self.api_key}"
