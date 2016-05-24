__author__ = 'Corey Petty'

import urllib3, json, certifi
import pandas as pd

def transactions():
    http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED',  # Force certificate check.
                               ca_certs=certifi.where(),  # Path to the Certifi bundle.
                               )

    dao_address = '0xbb9bc244d798123fde783fcc1c72d3bb8c189413'
    etherscan_url = 'https://api.etherscan.io/api?module=account&action=txlist&address=' + dao_address + '&sort=asc'

    with open('sample.json', 'w') as f, http.request('GET', etherscan_url, preload_content=False) as r:
        string_r = r.data.decode('utf-8')
        # shutil.copyfileobj(json.loads(string_r), f)
        # f.write(string_r)
        # f.close()
        obj = json.loads(string_r)
        json.dump(obj, f, sort_keys=True, indent=4)
    print(obj['message'])

transactions()