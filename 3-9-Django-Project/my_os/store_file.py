import os

import boto3


if __name__ == '__main__':
    session = boto3.session.Session()
    client = session.client(service_name='s3',
                            aws_access_key_id=os.environ['S3_ACCESS_KEY_ID'],
                            aws_secret_access_key=os.environ['S3_SECRET_ACCESS_KEY'],
                            endpoint_url=os.environ['S3_ENDPOINT_URL'])

    key = 'nixos'
    body = open('/home/my_os/static/images/nixos.png', 'rb').read()
    client.put_object(Bucket=os.environ['S3_BUCKET_NAME'], Key=key, Body=body)
    url = client.generate_presigned_url('get_object',
                                        Params={
                                            'Bucket': os.environ['S3_BUCKET_NAME'],
                                            'Key': key
                                        },
                                        ExpiresIn=3600)
    print(url)
