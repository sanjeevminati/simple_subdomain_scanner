import requests
import argparse
parser = argparse.ArgumentParser(description="Faster Subdomain Scanner using Threads")
parser.add_argument("domain", help="")
parser.add_argument("-w", "--wordlist", help="File that contains all subdomains to scan, line by line. Default is subdomains.txt",
                        default="word.txt")
args = parser.parse_args()    
domain = args.domain

wordlist = args.wordlist
#content = file.read()
subdomains = open(wordlist).read().splitlines()
for subdomain in subdomains:
    url =  f"http://{subdomain}.{domain}"
    try:
        requests.get(url)

    except requests.ConnectionError:
        # if the subdomain does not exist, just pass, print nothing
        #print("Errror")
        pass
    else:
        print("[+] Discovered subdomain:", url)    