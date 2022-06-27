import getopt
from pprint import pprint
import sys
from ns1 import NS1
from ns1.rest.errors import ResourceException
import json
from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint
from pyfiglet import figlet_format

from ns1auth import pk

api = NS1(apiKey=pk)

config = api.config
config["follow_pagination"] = True


def ns1cli_txt(argv):
    r = None
    z = None
    a = None

    try:
        opts, args = getopt.getopt(argv, "z:r:a:h")
    except getopt.GetoptError:
        pprint('invalid argument')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            cprint(figlet_format('ns1cli', font='starwars'), 'white', 'on_blue', attrs=['bold'])
            print()
            print(
                'Usage: Creates TXT Record:' + "\n"
                'ns1cli-txt -z <zone name> -r <record> -a <answer>'
            )
            print()
            sys.exit()
        elif opt in ("-r", "--record"):
            r: str = arg
        elif opt in ("-z", "--zone"):
            z: str = arg
        elif opt in ("-a", "--answer"):
            a: str = arg

    if z and r and a is not None:
        try:
            zone = api.loadZone(z)
            print("Loaded Zone:" + " " + z)
            print("Domain Record:" + " " + r)
            print("Record Answer:" + " " + a)
            rec = zone.add_TXT(r, a, ttl=3600)
            print(json.dumps(rec.data, indent=4))

        except ResourceException:
            pprint("Error: The Zone" + " " + z + " " + "does not exist in NS1")

    exit(0)


if __name__ == "__main__":
    ns1cli_txt(sys.argv[1:])
