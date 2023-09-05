import boto3
import paramiko

sftp_hostname = "s-0337e54afd80422bb.server.transfer.us-east-1.amazonaws.com"
sftp_username = "tf_sftp"
sftp_private_key = paramiko.RSAKey.from_private_key_file("./pkey", password=None)

bucket_name = 'batch-test-bucket-us-1'
bucket_key = 'sample.csv'

s3 = boto3.client('s3')

print('Establishing SFTP connection with ' + sftp_hostname)

transport = paramiko.Transport((sftp_hostname, 22))
transport.connect(username = sftp_username, pkey = sftp_private_key)

sftp = paramiko.SFTPClient.from_transport(transport)

print("SFTP connection succesfully stablished")

with sftp.open(bucket_key, 'wb', 32768) as f:
    print("Starting " + bucket_key + " file transfer")
    s3.download_fileobj(bucket_name, bucket_key, f)
    print("File transferred")

sftp.close()
print("SFTP connection succesfully closed")
