import requests
import json
import csv
import os
import sys
import argparse


class Vendor:
    def __init__(self, company_name, company_address, country_code, oui, is_private):
        self.company_name = company_name
        self.company_address = company_address
        self.country_code = country_code
        self.oui = oui
        self.is_private = is_private


def get_api_key(file_path):
    with open(file_path, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                api_key = row['key']
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        return api_key


def display_company_details(vendor):
    print("*************** Company Details *****************")
    print("Company Name:{}".format(vendor.company_name))
    print("Company Country Code:{}".format(vendor.country_code))
    print("Company Address:{}".format(vendor.company_address))


def find_details_from_mac(address, output="json"):
    # First do the get request with the mac address
    requests_url = "https://api.macaddress.io/v1"
    query_param = {
        'output': output,
        'search': address
    }
    base_dir = os.path.dirname(__file__)
    key_file = os.path.join(base_dir, 'key.csv')
    api_key = get_api_key(key_file)
    header = {'X-Authentication-Token': api_key}
    response = requests.get(requests_url, params=query_param, headers=header)
    vendor_details = json.loads(response.text)['vendorDetails']
    vendor = Vendor(vendor_details['companyName'], vendor_details['companyAddress'], vendor_details['countryCode'],
                    vendor_details['oui'], vendor_details['isPrivate'])

    return vendor


parser = argparse.ArgumentParser(description="custom arguments")
parser.add_argument('--mac_address', type=str, help="My custom parser")
args, sys.argv[1:] = parser.parse_known_args(sys.argv[1:])
print("Mac Address:{}".format(str(args.mac_address)))
company_details = find_details_from_mac(str(args.mac_address))
display_company_details(company_details)
