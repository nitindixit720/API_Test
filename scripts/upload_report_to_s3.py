from boto.s3.connection import S3Connection
from boto.s3.key import Key
import sys
import os

ACCESS_KEY = 'S3 access key'
SECRET = 'S3 secret Key'
BUCKET_NAME = 'S3 bucket name'  # note that you need to create this bucket first
HOST = 's3.ap-south-1.amazonaws.com'
PREFIX = os.environ.get('S3_PREFIX')


def upload_files(filename):
    conn = S3Connection(ACCESS_KEY, SECRET, host=HOST)
    bucket = conn.get_bucket(BUCKET_NAME)
    k = Key(bucket)
    k.key = PREFIX + '/' + filename
    k.set_contents_from_filename(filename)


def get_file_from_s3(filename):
    conn = S3Connection(ACCESS_KEY, SECRET, host=HOST)
    bucket = conn.get_bucket(BUCKET_NAME)
    k = Key(bucket)
    k.key = PREFIX + filename
    k.get_contents_to_filename(filename)


def list_backup_in_s3():
    conn = S3Connection(ACCESS_KEY, SECRET, host=HOST)
    bucket = conn.get_bucket(BUCKET_NAME)
    for i, key in enumerate(bucket.get_all_keys()):
        print("[%s] %s" % (i, key.name))


def delete_all_backups():
    # FIXME: validate filename exists
    conn = S3Connection(ACCESS_KEY, SECRET, host=HOST)
    bucket = conn.get_bucket(BUCKET_NAME)
    for i, key in enumerate(bucket.get_all_keys()):
        print("deleting %s" % (key.name))
        key.delete()


if __name__ == '__main__':
    upload_files(sys.argv[1])
