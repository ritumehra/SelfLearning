package com.amazonaws.lambda.demo;

import java.io.BufferedReader;
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.Arrays;

import com.amazonaws.AmazonServiceException;
import com.amazonaws.SDKGlobalConfiguration;
import com.amazonaws.SdkClientException;
import com.amazonaws.auth.DefaultAWSCredentialsProviderChain;
import com.amazonaws.regions.RegionUtils;
import com.amazonaws.services.kms.AWSKMS;
import com.amazonaws.services.kms.AWSKMSClientBuilder;
import com.amazonaws.services.kms.model.CreateKeyResult;
import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.amazonaws.services.s3.AmazonS3;
import com.amazonaws.services.s3.AmazonS3ClientBuilder;
import com.amazonaws.services.s3.AmazonS3EncryptionClientBuilder;
import com.amazonaws.services.s3.model.CryptoConfiguration;
import com.amazonaws.services.s3.model.KMSEncryptionMaterialsProvider;
import com.amazonaws.services.s3.model.S3Object;
import com.amazonaws.services.s3.model.S3ObjectInputStream;

public class LambdaFunctionHandler implements RequestHandler<Input, String> {

	String bucketName = "";// "rrf-qa-sources-static-indexing-bkt-spectrum";
	String keyName = "test.json";
	String clientRegion = "us-east-1";
	String kms_cmk_id = "";// "arn:aws:kms:us-east-1:151528745488:key/ca971680-69d5-459f-9835-f6ca5e726a67";
	int readChunkSize = 4096;

	@Override
	public String handleRequest(Input input, Context context) {
		System.setProperty(SDKGlobalConfiguration.ENABLE_S3_SIGV4_SYSTEM_PROPERTY, "true");
		System.out.println("Received event: " + input.toString());
		kms_cmk_id = input.getKey1();
		bucketName = input.getKey2();
		String clientFlg = input.getIsSelfSignedCert();

		try {

			/*AWSKMS kmsClient = AWSKMSClientBuilder.standard().withCredentials(new DefaultAWSCredentialsProviderChain())
					.withRegion(clientRegion).build();
			CreateKeyResult keyResult = kmsClient.createKey();
			kms_cmk_id = keyResult.getKeyMetadata().getKeyId();
			
			System.out.println("###kms_cmk_id : " + kms_cmk_id);*/

			KMSEncryptionMaterialsProvider materialProvider = new KMSEncryptionMaterialsProvider(kms_cmk_id);
			CryptoConfiguration cryptoConfig = new CryptoConfiguration()
					.withAwsKmsRegion(RegionUtils.getRegion(clientRegion));
			System.out.println("###masterkeyid : " + materialProvider.getEncryptionMaterials().getCustomerMasterKeyId());

			AmazonS3 encryptionClient  = null;
			if("true".equals(clientFlg)){
				 encryptionClient = AmazonS3EncryptionClientBuilder.standard()
							.withCredentials(new DefaultAWSCredentialsProviderChain())
							.withEncryptionMaterials(materialProvider)
							.withCryptoConfiguration(cryptoConfig)
//							.withKmsClient(kmsClient)
							.withRegion(clientRegion).build();
			}else{
				System.out.println("*****");
				encryptionClient = AmazonS3ClientBuilder.defaultClient();
			}
			
			
			

			System.out.println("####encryptionClient : " + encryptionClient);

			// Upload an object using the encryption client.
			String origContent = "S3 Encrypted Object Using KMS-Managed Customer Master Key.";
			int origContentLength = origContent.length();
			encryptionClient.putObject(bucketName, keyName, origContent);

			// Download the object. The downloaded object is still encrypted.
			S3Object downloadedObject = encryptionClient.getObject(bucketName, keyName);
			InputStream inputStream = downloadedObject.getObjectContent();
			BufferedReader streamReader = null;
			try {
				streamReader = new BufferedReader(new InputStreamReader(inputStream, "UTF-8"));
				StringBuilder responseStrBuilder = new StringBuilder();

				String inputStr;
				while ((inputStr = streamReader.readLine()) != null) {
					responseStrBuilder.append(inputStr);
				}

				String data = responseStrBuilder.toString();
				System.out.println("S3 data decrypted " + data);

			} catch (IOException e) {
				e.printStackTrace();
				System.out.println("Error occured " + Arrays.toString(e.getStackTrace()));
			}
			inputStream.close();
		} catch (AmazonServiceException e) {
			// The call was transmitted successfully, but Amazon S3 couldn't
			// process
			// it, so it returned an error response.
			e.printStackTrace();
		} catch (SdkClientException e) {
			// Amazon S3 couldn't be contacted for a response, or the client
			// couldn't parse the response from Amazon S3.
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

		return "Success";
	}
}