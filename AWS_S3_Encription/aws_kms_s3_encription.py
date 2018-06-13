import boto3

s3 = boto3.resource('s3', endpoint_url='https://s3.amazonaws.com/')

# s3.meta.client.put_object(Bucket: bucket,key: item,sse_customer_algorithm: 'aws:kms',sse_customer_key: key,  sse_customer_key_md5: md5)

s3.meta.client.put_object(Bucket='rrf-qa-sources-static-indexing-bkt-spectrum',
                          Key='normalized_LITIGATION_702.json', SSECustomerAlgorithm='aws:kms',
                          SSECustomerKey='arn:aws:kms:us-east-1:151528745488:alias/RRFDevImportIO')
