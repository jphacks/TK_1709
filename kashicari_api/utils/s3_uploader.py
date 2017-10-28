import boto3
from botocore.utils import fix_s3_host

from django.conf import settings


def upload_feed_to_s3(data, site_name):
    # アップロード先のS3の設定
    region_name = settings.STATIC_SETTINGS.get('FEED_REGION_NAME')
    bucket_name = settings.STATIC_SETTINGS['FEED_BUCKET_NAME']
    feed_dir = settings.STATIC_SETTINGS['FEED_DIRECTORY']
    # 任意設定（デバッグ用）
    # fake_s3_endpoint = 'http://localhost:4567'
    fake_s3_endpoint = settings.STATIC_SETTINGS.get('FAKE_S3_ENDPOINT')
    # S3接続
    s3 = boto3.resource(service_name='s3', region_name=region_name)
    if fake_s3_endpoint and settings.DEBUG:
        # ローカルの開発環境用の設定で上書き
        # https://github.com/jubos/fake-s3 をインストールして起動する
        # > gem install fakes3
        # > fakes3 -r ~/fake_s3 -p 4567
        s3 = boto3.resource(service_name='s3', endpoint_url=fake_s3_endpoint)
        s3.meta.client.meta.events.unregister('before-sign.s3', fix_s3_host)
    s3.Bucket(bucket_name).put_object(Key='{}/{}.xml'.format(feed_dir, site_name),
                                      Body=data,
                                      ContentType='application/xml')
