import boto3
import paramiko

sftp_hostname = "s-fa436dd293f84f7c8.server.transfer.us-east-1.amazonaws.com"
sftp_username = "tf_sftp"
sftp_private_key = paramiko.RSAKey.from_private_key_file("./pkey", password=None)

bucket_name = 'batch-test-bucket-us-1'

print('Establishing SFTP connection with ' + sftp_hostname)

transport = paramiko.Transport((sftp_hostname, 22))
transport.connect(username = sftp_username, pkey=sftp_private_key)

with paramiko.SFTPClient.from_transport(transport) as sftp:
    print("Connection succesfully stablished ... ")
    sftp.put('jwt-01.PNG', 'jwt-01.PNG')
    sftp.close()
    print("Connection succesfully closed ... ")
