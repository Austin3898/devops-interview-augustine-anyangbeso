import boto3


s3 = boto3.client('s3', region_name='us-east-1')
buckets = s3.list_buckets()["Buckets"]
for bucket in buckets:
    print(bucket['Name'])
