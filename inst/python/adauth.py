import json
import argparse

from adhelper import adauth

parser = argparse.ArgumentParser(description='authentication')
parser.add_argument('--address', required=True, type=str, help='LDAP hostname or IP')
parser.add_argument('--user_email', required=True, type=str, help='user email')
parser.add_argument('--password', required=True, type=str, help='password')

args = parser.parse_args()
response = adauth(args.address, args.user_email, args.password)

print(json.dumps(response, sort_keys=True, indent=4, separators=(',', ': ')))

