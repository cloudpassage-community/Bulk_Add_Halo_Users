# bulk_useradd.py
# Create Halo users from a .csv
#
# Version  1.0.0
# Date 07.10.2018
##############################################################################

# Import Python Modules
import json, csv, base64, requests, os, argparse
import cloudpassage
import yaml
import time
from time import sleep
global api_session


# Define Methods
def create_api_session(session):
    config_file_loc = "cloudpassage.yml"
    config_info = cloudpassage.ApiKeyManager(config_file=config_file_loc)
    session = cloudpassage.HaloSession(config_info.key_id, config_info.secret_key)
    return session


def post_users(session, file_name):
    input_file = csv.DictReader(open(file_name))
    post_users = cloudpassage.HttpHelper(session)
    for row in input_file:
        post_users.post("/v2/users", compose_json(row))


def compose_json(data_in):
    data_out = {"user" : {"username" : data_in['username'],
                "firstname" : data_in['firstname'],
                "lastname" : data_in['lastname'],
                "email" : data_in['email'],
                "sms_phone_number" : data_in['sms_phone_number'],
                "access" : [{"roles" : data_in['role'],
                             "group_id" : data_in['group_id']}]}}
    return data_out


### MAIN

if __name__ == "__main__":
    api_session = None
    api_session = create_api_session(api_session)
    post_users(api_session, "users.csv")
