import os
import boto3
from io import BytesIO
os.environ['IS_SELF_SIGNED_CERT'] = "true"
os.environ['END_POINT_URL'] = "https://s3.amazonaws.com/"
os.environ['RRF_SOLR_SSL_CERTIFICATE_FILE'] = "rrf-spectrum-deployment-qa/RRF_QA_Solr_Binary.pem"

import requests
import simplejson

url_str = 'https://10.62.138.39:8983/solr/naics' + '/select?q=description:'
# url_str = 'http://10.62.137.191:8983/solr/naics' + '/select?q=description:'
desc_express = "'" + 'Crop Production' + "'"
url_str = url_str + desc_express + "&rq={!rniRerank reRankQuery=$rrq reRankMode=replace reRankWeight=1.0 minimumScoreToCheck=0} &rrq={!func}rniMatch(description,"
url_str = url_str + desc_express + ")&fl=naics,description,score&wt=json"


print("SOLR URL:", url_str)
print(str(os.environ.get('IS_SELF_SIGNED_CERT')).lower())

if str(os.environ.get('IS_SELF_SIGNED_CERT')).lower() == 'true':
    print("Env Found")
else:
    print("Not Found")

# s3.meta.client.download_file('rrf-qa-normalized-json-bkt', 'RRF_QA_Solr_Binary.pem', '/tmp/RRF_QA_Solr_Binary.pem')

# Check if an environment variable is present or not
if str(os.environ.get('IS_SELF_SIGNED_CERT')).lower() == 'true' and str(os.environ['IS_SELF_SIGNED_CERT']).lower() == 'true':
    print("With Certificate")

    ssl_string = os.environ['RRF_SOLR_SSL_CERTIFICATE_FILE']
    print("ssl_string:{}".format(ssl_string))

    strVar = ssl_string.split('/')
    print("strVar:{}".format(strVar))

    s3 = boto3.resource('s3', endpoint_url=os.environ['END_POINT_URL'])

    if len(strVar) == 2:
        s3.meta.client.download_file(strVar[0], strVar[1],
                                     '/tmp/RRF_QA_Solr_Binary.pem')

        # response = requests.request("GET", url_str, verify='RRF_QA_Solr_Binary.pem')
        response = requests.request("GET", url_str, verify='/tmp/RRF_QA_Solr_Binary.pem')
    else:
        print ("Invalid ENV")
else:
    response = requests.request("GET", url_str)


try:
    if response is not None:
        json = simplejson.loads(response.text)

        if len(json['response']['docs']) > 0:

            naics_code = json['response']['docs'][0]['naics']
            print("Got Solar Response naics_code:", naics_code)
        else:
            print("Error in Solar Response")
            naics_code = None

        print(naics_code)
    else:
        naics_code = None

except Exception as e:
    print("Solr Error:", e)
