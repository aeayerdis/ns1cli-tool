import sys

from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint
from pyfiglet import figlet_format


cprint(figlet_format('ns1cli', font='starwars'), 'white', 'on_blue', attrs=['bold'])


cprint(
       'Welcome to NS1CLI command line tool for communincating with the NS1 API. This API is written in python v3.8 and uses the following libraries:' + "\n"
       'getopt, sys, pprint, ns1, pandas, tabulate'
)


print()

print(
       'This utility calls on multiple methods such as:' + "\n"
       "\n"                                                  
       'ns1cli-get' + ' ' + '-' + ' ' + 'Pulls information from NS1 such as zones, records, and answers. More information can be provided with "ns1cli-get -h"' + "\n"
       "\n"
       'ns1cli-add' + ' ' + '-' + ' ' + 'Adds an answer value to an existing DNS record. More information can be provided with "ns1cli-add -h"' + "\n"
       "\n"
       'ns1cli-a' + ' ' + '-' + ' ' + 'Adds a DNS A Record to the zone of your choice. More information can be provided with "ns1cli-a -h"' + "\n"
       "\n"
       'ns1cli-alias' + ' ' + '-' + ' ' + 'Adds a DNS ALIAS Record to the zone of your choice. More information can be provided with "ns1cli-alias -h"' + "\n"
       "\n"
       'ns1cli-cname' + ' ' + '-' + ' ' + 'Adds a DNS CNAME Record to the zone of your choice. More information can be provided with "ns1cli-cname -h"' + "\n"
       "\n"
       'ns1cli-spf' + ' ' + '-' + ' ' + 'Adds a DNS SPF Record to the zone of your choice. More information can be provided with "ns1cli-spf -h"' + "\n"
       "\n"
       'ns1cli-txt' + ' ' + '-' + ' ' + 'Adds a DNS TXT Record to the zone of your choice. More information can be provided with "ns1cli-txt -h"' + "\n"
)

print()

print()

print(
       'Note: each method is a ALIAS created from function that references the python script. Please refer to Windows or MacOS documentation for creating these in their respective PS/BASH Profile settings'
)

print()
