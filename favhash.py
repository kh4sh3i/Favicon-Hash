#!/usr/bin/env python3
import argparse, requests, urllib3, mmh3, codecs
from termcolor import colored
urllib3.disable_warnings()

version = 0.1

def calfav(target):

    try:

        url = f'https://{target}/favicon.ico'
        response = requests.get(url, verify=False)

        if (response.status_code == 404):
            url = f'https://{target}/favicon.png'
            response = requests.get(url, verify=False)
            if (response.status_code == 404):
                url = f'https://{target}/favicon.gif'
                response = requests.get(url, verify=False)

        if (response.status_code != 404):
            favicon = codecs.encode(response.content,"base64")
            hash = mmh3.hash(favicon)
            print(colored(f'\nurl:{url}', "cyan"))
            #print(colored('\nhttp.favicon.hash:'+str(hash), "yellow", attrs=['bold']))
            print(colored(f'http.favicon.hash:{hash}', "yellow"))
        else:
            print(colored(f'\nurl:{target}', "cyan"))
            print(colored(f'http.favicon.hash: not found', "red"))

    except Exception as e:
        print(colored(e, "red"))

def banner():

    ## version
    print(colored("version {}" .format(version), "green", attrs=['bold']))

if __name__ == "__main__":

    ## version
    #banner()

    ## parse argument
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--target', help='The hostname of the target, eg: github.com', default=False)
    parser.add_argument("-l", "--list", action="store", help="List of target url saperated with new line", default=False)
    args = parser.parse_args()

    if args.target is not False:
        
        calfav(args.target) 
    
    elif args.list is not False:
                
        with open(args.list) as targets:
            
            for target in targets:
                target = target.rstrip()
                calfav(target) 

    else:

        parser.print_help()
        parser.exit()
