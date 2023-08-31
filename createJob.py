import boto3

client = boto3.client('batch')

response = client.submit_job(
    jobDefinition='dynamodb_import_job_definition',
    jobName='dynamodb_import_job10',
    jobQueue='dynamodb_import_queue',
    containerOverrides={
        'environment': [
            {
                'name': 'table_name',
                'value': 'batch-test-table',

            },
            {
                'name': 'bucket_name',
                'value': 'batch-test-bucket-us-1'
            },
            {
                'name': 'key',
                'value': 'sample.csv'
            }
        ]
    }
)

print(response)