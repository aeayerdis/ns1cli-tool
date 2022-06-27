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


def ns1cli_spf(argv):
    r = None
    t = None
    a = None

    try:
        opts, args = getopt.getopt(argv, "t:r:a:h")
    except getopt.GetoptError:
        pprint('invalid argument')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            cprint(figlet_format('ns1cli', font='starwars'), 'white', 'on_blue', attrs=['bold'])
            print()
            print(
                'Usage: Adds Record Answer Value to existing Record:' + "\n"
                'ns1cli-add  -r <record> -t <record_type> -a <answer>'
            )
            print()
            sys.exit()
        elif opt in ("-r", "--record"):
            r: str = arg
        elif opt in ("-t", "--type"):
            t: str = arg
        elif opt in ("-a", "--answer"):
            a: str = arg

    if t and r and a is not None:
        try:
            print("Loaded Record:" + " " + r)
            print("Record Type:" + " " + t)
            print("Record Answer:" + " " + a)
            rec = api.loadRecord(r, t)
            rec.addAnswers(a)
            print(json.dumps(rec.data, indent=4))

        except ResourceException:
            print("Error: The Zone" + " " + t + " " + "does not exist in NS1")

    exit(0)


if __name__ == "__main__":
    ns1cli_spf(sys.argv[1:])