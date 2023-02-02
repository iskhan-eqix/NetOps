import json
import requests
import pprint
from jq import jq
import io, sys

def get_pdb_data(asn):
    url = "https://peeringdb.com/api/net?asn=" + asn
    resp = requests.get(url=url)
    pdb_json = json.loads(resp.text)
    data = jq(".data | map({name, info_prefixes4, info_prefixes6}) | .[]").transform(pdb_json)
    return data

data_list = []
with open("asn_list.txt") as f:
    asn_list = f.read().split()
    fd = io.open(r'PATH/output-pdb', 'w')
    old_stdout = sys.stdout
    sys.stdout = fd

    for ASN in asn_list:
     try:
        url = "https://peeringdb.com/api/net?asn=" + ASN
        resp = requests.get(url=url)
        pdb_json = json.loads(resp.text)
        data = jq(".data | map({name, asn, info_prefixes4, info_prefixes6}) | .[]").transform(pdb_json)
        print(data)
     except:
        print("Error processing ASN: " + ASN)
     continue
