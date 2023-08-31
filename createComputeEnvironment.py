import boto3

client = boto3.client('batch')

response = client.create_compute_environment(
    computeEnvironmentName='dynamodb_import_environment',
    type='MANAGED',
    state='ENABLED',
    computeResources={
        'type': 'EC2',
        'allocationStrategy': 'BEST_FIT',
        'minvCpus': 0,
        'maxvCpus': 256,
        'subnets': [
            'subnet-060a0a067683ab844',
            'subnet-0a175e4bf6554bd8a'
        ],
        'instanceRole': 'ecsInstanceRole',
        'securityGroupIds': [
            'sg-05453881731fab471'
        ],
        'instanceTypes': [
            'optimal'
        ]
    }
)

print(response)