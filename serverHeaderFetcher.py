import requests
from requests.exceptions import HTTPError
import sys
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

hosts_file = open(sys.argv[1], 'r')
for i in hosts_file.readlines():
    i = i.strip("\n")
    i = "https://"+i
    i_s = "https://"+i
    try:
        r = requests.get(i, verify=False, timeout=3)
        print(i + ": " + r.headers['Server'] + "\n")
    except HTTPError as http_err:
        print("[-] Host: " + i + " Connection error 1\n")
        error1 = f'HTTP error occurred: {http_err}'  
    except Exception as err:
        error2 = f'Other error occurred: {err}'
        print("[-] Host: " + i + " Connection error 2\n")
