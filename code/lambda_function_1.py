import json
import boto3
import csv
import io

s3Client = boto3.client('s3')
glue = boto3.client('glue')

def lambda_handler(event, context):

    LAMBDA_LOCAL_TMP_FILE = '/tmp/test.csv'
    OUTPUT_BUCKET = 'awslearning-bucket-2'

    # Extract bucket name and Key from event
    json_body = json.loads(event['Records'][0]['body'])['Records'][0]['s3']
    bucket = json_body['bucket']['name']
    key = json_body['object']['key']
    opkey = key.split('.')[0]+'.csv'
    print(bucket)
    print(key)

    #Extracting csv object from s3Client

    file_obj = s3Client.get_object(Bucket=bucket, Key=key)
    file_content = file_obj["Body"].read().decode('utf-8')
    json_content = json.loads(file_content)

    # print(json_content)
    header = ['id', 'region', 'order_id']
    data = []
    for lis in json_content['body']:
        data.append((lis['id'], lis['region'], lis['order_id']))

    with open(LAMBDA_LOCAL_TMP_FILE, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(data)

    s3Client.upload_file(LAMBDA_LOCAL_TMP_FILE, OUTPUT_BUCKET, opkey)
    response = glue.start_crawler(
    Name='orderCrawler'
    )


    # Returning the same output.
    return {
        'statusCode': '200'
    }
