import getopt
from pprint import pprint
import sys
from ns1 import NS1
from ns1.rest.errors import ResourceException
import pandas as pd
from tabulate import tabulate
from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint
from pyfiglet import figlet_format
from ns1auth import gk

api = NS1(apiKey=gk)

config = api.config
config["follow_pagination"] = True


def main(argv):
    r = None
    t = None
    z = None
    a = None
    x = None
    l = None

    try:
        opts, args = getopt.getopt(argv, "z:r:t:a::x:l:h")
    except getopt.GetoptError:
        pprint('invalid argument')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            cprint(figlet_format('ns1cli', font='starwars'), 'white', 'on_blue', attrs=['bold'])
            print()
            print(
                'Usage: Prints out the following as' + "\n" +
                'ns1cli-get -x' + " " + "'all'" + " " + "(prints all zones)" + "\n"
                                                                               'ns1cli-get -z <zone name> (returns all record data listed within zone)' + " " + "\n"
                                                                                                                                                                'ns1cli-get -z <zone name> -t <record type> (returns all record_types listed within zone)' + " " + "\n"
                                                                                                                                                                                                                                                                   'ns1cli-get -l <lookup zone name> -a <generic answer value> (returns record answers listed within zone)' + " " + "\n"
                                                                                                                                                                                                                                                                                                                                                                                    'ns1cli-get -r <record> -t <record type> (NS, MX, TXT, A, CNAME, etc)'
            )
            print()
            sys.exit()
        elif opt in ("-r", "--domain"):
            r: str = arg
        elif opt in ("-t", "--record_type"):
            t: str = arg
        elif opt in ("-z", "--zone"):
            z: str = arg
        elif opt in ("-a", "--answer"):
            a: str = arg
        elif opt in ("-x", "--all_zones"):
            x: str = arg
        elif opt in ("-l", "--look_up"):
            l: str = arg

    if r is not None and t is None:
        print("Error: Please add -t 'Record_Type' ")

    if x is not None and x == "all":
        try:
            all_zones = api.zones()
            a_df = pd.json_normalize(all_zones.list())
            ddf = a_df.reindex(columns=['name', 'zone', 'dns_servers'])
            print(tabulate(ddf, headers='keys', tablefmt='psql'))
        except ResourceException:
            pprint("Error retrieving zones")

    if r and t is not None:
        pprint("Domain" + ":" + " " + r)
        pprint("Record Type" + ":" + " " + t)

        try:
            rec = api.loadRecord(r, t)
            print(tabulate(rec.data["answers"], headers='keys', tablefmt='psql'))

        except ResourceException:
            print(
                "Error: The domain" + " " + r + " " + "or domain record type" + " " + t + " " + "does not exist in NS1. Please check the zone for record lookup")

    if l and a is not None:
        try:
            zone = api.loadZone(l)
            df = pd.json_normalize(zone.data["records"])
            ddf = df[df['short_answers'].astype(str).str.contains(a)]
            dddf = ddf.reindex(columns=['domain', 'type', 'short_answers'])
            print(tabulate(dddf, headers='keys', tablefmt='psql'))

        except ResourceException:
            print("Error: The Zone" + " " + l + " " + "and record answer" + " " + a + " " + "does not exist in NS1")

    if l is None and t is None and r is None and z is not None:
        pprint("Zone" + ":" + " " + z)

        try:
            zone = api.loadZone(z)
            df = pd.json_normalize(zone.data["records"])
            ddf = df.reindex(columns=['domain', 'type', 'short_answers'])
            print(tabulate(ddf, headers='keys', tablefmt='psql'))

        except ResourceException:
            print("Error: The Zone" + " " + z + " " + "does not exist in NS1")

    if z and t is not None:
        print("Zone" + ":" + " " + z + " " + "and record type is" + " " + t)

        try:
            zone = api.loadZone(z)
            df = pd.json_normalize(zone.data["records"])
            ddf = df[df['type'].str.match(t)]
            dddf = ddf.reindex(columns=['domain', 'type', 'short_answers'])
            print(tabulate(dddf, headers='keys', tablefmt='psql'))

        except ResourceException:
            print("Error: The Zone" + " " + z + " " + "and record type" + " " + t + " " + "does not exist in NS1")

    exit(0)


if __name__ == "__main__":
    main(sys.argv[1:])
