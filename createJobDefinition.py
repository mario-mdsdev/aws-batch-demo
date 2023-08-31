import boto3

iam = boto3.client('iam')
client = boto3.client('batch')

dynamodbImportRole = iam.get_role(RoleName='dynamodbImportRole')

response = client.register_job_definition(
    jobDefinitionName='dynamodb_import_job_definition',
    type='container',
    containerProperties={
        'image': 'mdsdevhub/aws-batch-demo:latest',
        'memory': 0.5,
        'vcpus': 0.25,
        'jobRoleArn': dynamodbImportRole['Role']['Arn'],
        'executionRoleArn': dynamodbImportRole['Role']['Arn'],
        'environment': [
            {
                'name': 'AWS_DEFAULT_REGION',
                'value': 'us-east-1'
            }
        ]
    }
)

print(response)