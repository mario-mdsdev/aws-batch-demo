import boto3

client = boto3.client('batch')

response = client.create_job_queue(
    jobQueueName='dynamodb_import_queue',
    state='ENABLED',
    priority=1,
    computeEnvironmentOrder=[
        {
            'order': 100,
            'computeEnvironment': 'dynamodb_import_environment'
        }
    ]
)

print(response)