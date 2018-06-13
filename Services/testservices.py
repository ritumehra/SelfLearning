import json
import requests
import os
import boto3

payload = {
    "entityRequestId": "781",
    "bucketName": "rrf-dev-normalized-json-bkt-spectrum",
    "key": "781/normalized_LITIGATION_781.json"
}

print("Starting LITIGATION Service:")
lit_url = "https://rrf-qa-pythonsrv.abb.com:5001/process/Litigation"
print("lit_url", type(lit_url), ":", lit_url)
res = requests.post(lit_url, data=json.dumps(payload), verify=False)

print(res.text)

#
#
# os.environ['IS_SELF_SIGNED_CERT'] = "true"
# os.environ['END_POINT_URL'] = "https://s3.amazonaws.com/"
# os.environ['RRF_SOLR_SSL_CERTIFICATE_FILE'] = "rrf-spectrum-deployment-qa/RRF_QA_Solr_Binary.pem"
# os.environ['EC2_SERVER'] = 'rrf-qa-pythonsrv.abb.com'
# os.environ['LITIGATION_PORT'] = '5001'
#
# payload = {
#     "entityRequestId": "781",
#     "bucketName": "rrf-dev-normalized-json-bkt-spectrum",
#     "key": "781/normalized_LITIGATION_781.json"
# }
#
# if str(os.environ.get('IS_SELF_SIGNED_CERT')).lower() == 'true' and str(os.environ['IS_SELF_SIGNED_CERT']).lower() == 'true':
#     print("With Certificate")
#
#     ssl_string = os.environ['RRF_SOLR_SSL_CERTIFICATE_FILE']
#     print("ssl_string:{}".format(ssl_string))
#
#     strVar = ssl_string.split('/')
#     print("strVar:{}".format(strVar))
#
#     s3 = boto3.resource('s3', endpoint_url=os.environ['END_POINT_URL'])
#
#     if len(strVar) == 2:
#         s3.meta.client.download_file(strVar[0], strVar[1],
#                                      '/tmp/RRF_QA_Solr_Binary.pem')
#
#     print("Starting LITIGATION Service:")
#     lit_url = "https://" + os.environ['EC2_SERVER'] + ":" + os.environ['LITIGATION_PORT'] + "/process/Litigation"
#     print("lit_url", type(lit_url), ":", lit_url)
#     requests.post(lit_url, data=json.dumps(payload), verify = '/tmp/RRF_QA_Solr_Binary.pem')
