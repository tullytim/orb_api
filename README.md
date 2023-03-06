<img src="icon.png" align="right" />

[![License](https://img.shields.io/badge/License-Apache_2.0-yellowgreen.svg)](https://opensource.org/licenses/Apache-2.0)  


# Orb

orb_api is a simple [Orb](https://www.withorb.com) API for all of the CRUD operations in the orb product.
## Not For Production
This API was a gift for the team before we finallt wound uo investing.  the API works great and is fantastic for testing Orb, but this js not the official API or meant for production. 
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

## Description
An instance of the Orb object simply encapsulates connectivity and respective metadata for an account with a given API.  Beyond that, the instance provides access to instance methods, ie, no static methods on the class. 

## Third Party Libraries and Dependencies

The following libraries will be installed when you install the client library:
* datetime
* json
* uuid
* requests
* termcolor 

## License
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
