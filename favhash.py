#!/usr/bin/env python3
import mmh3
import requests
import codecs
import sys
from termcolor import colored
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

if len(sys.argv) < 2:
	print("[!] Error!")
	print(f"[-] Use: python3 {sys.argv[0]} http://example.com/favicon.ico")
	sys.exit()

def main():

    try:
        response = requests.get(sys.argv[1], verify=False)
        if (response.status_code != 404):
            favicon = codecs.encode(response.content,"base64")
            hash_favicon = mmh3.hash(favicon)

            print(colored(f'http.favicon.hash:{hash_favicon}', "yellow"))
            print(colored(f'https://www.shodan.io/search?query=http.favicon.hash%3A'+str(hash_favicon), "green"))
        else:
            print(colored(f'http.favicon.hash: not found', "red"))

    except Exception as e:
        print(colored(e, "red"))

if __name__ == '__main__':
	main()