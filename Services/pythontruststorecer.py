# import jks
#
# keystore = jks.KeyStore.load('rrf-qa-truststore.jks', 'Password1')
#
# print(keystore.private_keys)
# print(keystore.certs)
# print(keystore.secret_keys)

from __future__ import print_function
import sys, base64, textwrap
import jks
import requests
import simplejson
def print_pem(der_bytes, type, cer_name):

    print(cer_name)

    with open(cer_name+".pem", 'w') as f:
        print("-----BEGIN %s-----" % type, file=f)
        print("\r".join(textwrap.wrap(base64.b64encode(der_bytes).decode('ascii'), 64)), file=f)
        print("-----END %s-----" % type, file=f)

ks = jks.KeyStore.load('rrf-qa-truststore.jks', 'Password1')

for alias, c in ks.certs.items():
    print("Certificate: %s" % c.alias)
    print_pem(c.cert, "CERTIFICATE", c.alias)
    print()

def solr_query():

    url_str = 'https://10.62.138.39:8983/solr/naics' + '/select?q=description:'
    desc_express = "'" + 'Crop Production' + "'"
    url_str = url_str + desc_express + "&rq={!rniRerank reRankQuery=$rrq reRankMode=replace reRankWeight=1.0 minimumScoreToCheck=0} &rrq={!func}rniMatch(description,"
    url_str = url_str + desc_express + ")&fl=naics,description,score&wt=json"

    response = requests.request("GET", url_str, verify=False)

    json = simplejson.loads(response.text)
    naics_code = json['response']['docs'][0]['naics']
    print("Got Solar Response naics_code:", naics_code)

solr_query()