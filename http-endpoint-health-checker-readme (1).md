# HTTP Endpoint Health Checker Read me.

Below Python script checks the health of a set of HTTP endpoints defined in a YAML configuration file. It periodically sends requests to each endpoint and calculates the availability percentage for each domain (endpoint)

## Features

- Reads endpoint configurations from a YAML file  
- Supports GET and POST requests  
- Handles custom headers and request bodies  
- Checks endpoints every 15 seconds  
- Calculates and logs availability percentage for each domain  
- Continues running until manually stopped

## Requirements

- Python 3.6+  
- `requests` library  
- `pyyaml` library

## Installation

1. Clone this repository or download the script.  
2. Install the required libraries:

pip install requests pyyaml

## Usage

1. Create a YAML configuration file with your endpoints. Example:

\- name: fetch index page

  url: https://fetch.com/

  method: GET

  headers:

    user-agent: fetch-synthetic-monitor

\- name: fetch some fake post endpoint

  url: https://fetch.com/some/post/endpoint

  method: POST

  headers:

    content-type: application/json

    user-agent: fetch-synthetic-monitor

  body: '{"foo":"bar"}'

2. Run the script with the path to your configuration file:

python health\_checker.py path/to/your/config.yaml

3. The script will start checking the endpoints and logging the results to the console every 15 seconds.  
     
4. To stop the script, press Ctrl+C.

## Output

The script will print the availability percentage for each domain after every check cycle. For example:

fetch.com has 67% availability percentage

www.fetchrewards.com has 100% availability percentage

## Notes:

- An endpoint is considered UP if it returns a 2xx status code and responds in less than 500ms.  
- The availability percentage is calculated over the lifetime of the program execution.  
- Percentages are rounded to the nearest whole number.

