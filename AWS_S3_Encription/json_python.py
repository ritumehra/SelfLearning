import datetime
import json
#
json_str = {'ResponseMetadata':
{'RequestId': '333FF41DC1456B44',
'HostId': 'Xooo9sFzlL7GuE9QLEXGN26DgTOnjpr9KaZTg0R+EA/HhP/lPHk1FIDeUsjVdxhyBjPLUbpOvAs=', 'HTTPStatusCode': 200,
 'HTTPHeaders': {'x-amz-id-2': 'Xooo9sFzlL7GuE9QLEXGN26DgTOnjpr9KaZTg0R+EA/HhP/lPHk1FIDeUsjVdxhyBjPLUbpOvAs=',
 'x-amz-request-id': '333FF41DC1456B44', 'date': 'Tue, 29 May 2018 10:13:02 GMT',
 'last-modified': 'Tue, 29 May 2018 10:12:06 GMT', 'etag': '"c6c1611d0e1731a36a06f2b63980b3f1"',
 'x-amz-server-side-encryption': 'aws:kms',
 'x-amz-server-side-encryption-aws-kms-key-id': 'arn:aws:kms:us-east-1:151528745488:key/97d1b282-df5f-488b-9f21-92a55da542bd',
 'x-amz-meta-workflowid': 'c9314da1-ea9d-4443-ab10-9f5f5c84b3b0',
 'x-amz-meta-externalreference': '968', 'content-encoding': 'gzip',
 'accept-ranges': 'bytes', 'content-type': 'application/x-ndjson', 'content-length': '20', 'server': 'AmazonS3'},
 'RetryAttempts': 0},
 'AcceptRanges': 'bytes',
 'ContentLength': 20, 'ETag': '"c6c1611d0e1731a36a06f2b63980b3f1"', 'ContentEncoding': 'gzip',
 'ContentType': 'application/x-ndjson', 'ServerSideEncryption': 'aws:kms',
 'Metadata': {'workflowid': 'c9314da1-ea9d-4443-ab10-9f5f5c84b3b0', 'externalreference': '968'},
'SSEKMSKeyId': 'arn:aws:kms:us-east-1:151528745488:key/97d1b282-df5f-488b-9f21-92a55da542bd'}

# json_str = {'ResponseMetadata': {'RequestId': '77F55CAAFEDBE554', 'HostId': 'IzhHfUb2QWJktFsn5HsOJz0sgsjdKDKoTWwvoKHoEL0XVPZoUO4SXLMxgDdr7ATmRXrRgPw9OqI=', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amz-id-2': 'IzhHfUb2QWJktFsn5HsOJz0sgsjdKDKoTWwvoKHoEL0XVPZoUO4SXLMxgDdr7ATmRXrRgPw9OqI=', 'x-amz-request-id': '77F55CAAFEDBE554', 'date': 'Tue, 29 May 2018 10:13:01 GMT', 'last-modified': 'Tue, 29 May 2018 10:08:58 GMT', 'etag': '"1ebd24179124722064465d690e64c698"', 'x-amz-server-side-encryption': 'aws:kms', 'x-amz-server-side-encryption-aws-kms-key-id': 'arn:aws:kms:us-east-1:151528745488:key/ca971680-69d5-459f-9835-f6ca5e726a67',
#         'x-amz-meta-fninput': '{"entityReqId":968,"sourceId":7,"fileName":"968/ADVERSE_MEDIA-ba8f675e-04ff-4d0a-9ae7-0aef692af1a4-2018.05.29.10.08.57.json.gz"}', 'accept-ranges': 'bytes', 'content-type': 'application/x-gzip', 'content-length': '4128', 'server': 'AmazonS3'}, 'RetryAttempts': 0}, 'AcceptRanges': 'bytes', 'ContentLength': 4128, 'ETag': '"1ebd24179124722064465d690e64c698"', 'ContentType': 'application/x-gzip',
#             'ServerSideEncryption': 'aws:kms',
#             'Metadata': {'fninput': '{"entityReqId":968,"sourceId":7,"fileName":"968/ADVERSE_MEDIA-ba8f675e-04ff-4d0a-9ae7-0aef692af1a4-2018.05.29.10.08.57.json.gz"}'}, 'SSEKMSKeyId': 'arn:aws:kms:us-east-1:151528745488:key/ca971680-69d5-459f-9835-f6ca5e726a67'}

if 'workflowid' in json_str['Metadata']:
    work_flow_id = json_str['Metadata']['workflowid']
    print(work_flow_id)
    print("Chawla")

if 'fninput' in json_str['Metadata']:
    meta_content = json.loads(json_str['Metadata']['fninput'])
    source_id = meta_content['sourceId']
    print(source_id)
    print("Ritu")