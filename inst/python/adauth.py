import json
import argparse

from adhelper import adauth

parser = argparse.ArgumentParser(description='authentication')
parser.add_argument('--address', required=True, type=str, help='LDAP hostname or IP')
parser.add_argument('--username', required=True, type=str, help='user name')
parser.add_argument('--password', required=True, type=str, help='password')

args = parser.parse_args()
response = adauth(args.address, args.username, args.password)

print(json.dumps(response, sort_keys=True, indent=4, separators=(',', ': ')))

