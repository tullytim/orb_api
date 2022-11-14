<img src="icon.png" align="right" />

[![License](https://img.shields.io/badge/License-Apache_2.0-yellowgreen.svg)](https://opensource.org/licenses/Apache-2.0)  


# Orb

orb_api is a simple [Orb](https://www.withorb.com) API for all of the CRUD operations in the orb product.

## Installation
Package coming w/ pip install capabilities.

## Contributing and Questions
Contributions are very welcome, as are feature requests and suggestions.

## Quickstart and Client Examples

The module is incredible easy to use. 
1. Instantiate an Orb instance passing the api_key you obtained from your onboarding as well as the [optional] debug flag you need for testing.
2. Profit
```python
o = Orb(<YOUR_API_KEY_HERE>, True)
rv = o.log_event(CUSTOMER, "asdf", props={"foo": "bar"})
```
