#!/usr/bin/env python

"""
Author: Angelo Pinelli
Purpose: Based on Nick Russo, adapted for EPN-M
List devices
"""

import requests

requests.packages.urllib3.disable_warnings()

def main():
    """
    Execution begins here.
    """

    api_path = "https://10.122.28.3/webacs/api/v4/data"

    # Basic authentication (no tokens) works for our simple example
    basic_auth = ("api_user", "password")

    get_headers = {"Accept": "application/json"}

    # First, issue HTTP GET to collect a list of EPNM-managed devices
    get_resp = requests.get(
        f"{api_path}/Devices",
        auth=basic_auth,
        headers=get_headers,
        verify=False
    )

    # Response 204 (no content) isn't an error, but carries an empty body
    if get_resp.status_code != 200:
        raise requests.exceptions.HTTPError("Empty device list")

    # Device list is present; parse JSON from HTTP body
    # See full_response.json for more details, but it isn't very interesting
    devices = get_resp.json()["queryResponse"]['entityId']

    temp = []
    temp2 = []
    
    for dev in devices:
        temp.append(dev['$'])

    # This temporary list contains the ID's from all devices:   
    print(temp)

    for i in temp:
        get_device_name = requests.get(
            f"{api_path}/Devices/{i}",
            auth=basic_auth,
            headers=get_headers,
            verify=False
        )
        temp2.append(get_device_name.json()['queryResponse']['entity'][0]['devicesDTO']['deviceName'])
    
    # This prints all device names:
    print(temp2)


if __name__ == "__main__":
    main()
