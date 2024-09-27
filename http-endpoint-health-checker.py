import sys
import yaml
import requests
import time
from collections import defaultdict
from urllib.parse import urlparse

def load_config(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def check_endpoint(endpoint):
    url = endpoint['url']
    method = endpoint.get('method', 'GET')
    headers = endpoint.get('headers', {})
    body = endpoint.get('body')

    try:
        start_time = time.time()
        response = requests.request(method, url, headers=headers, data=body, timeout=1)
        latency = (time.time() - start_time) * 1000  # Convert to milliseconds

        is_up = 200 <= response.status_code < 300 and latency < 500
        return is_up, urlparse(url).netloc
    except requests.RequestException:
        return False, urlparse(url).netloc

def main(config_file):
    endpoints = load_config(config_file)
    total_checks = defaultdict(int)
    successful_checks = defaultdict(int)

    while True:
        for endpoint in endpoints:
            is_up, domain = check_endpoint(endpoint)
            total_checks[domain] += 1
            if is_up:
                successful_checks[domain] += 1

        for domain in total_checks:
            availability = (successful_checks[domain] / total_checks[domain]) * 100
            print(f"{domain} has {round(availability)}% availability percentage")

        time.sleep(15)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <config_file_path>")
        sys.exit(1)
    
    config_file = sys.argv[1]
    main(config_file)
