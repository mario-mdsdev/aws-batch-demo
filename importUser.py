#!/usr/bin/python3
import os
import boto3
import csv
from datetime import datetime
import pytz

s3_resource = boto3.resource('s3')

print('os environ:', os.environ)

table_name = os.environ['table_name']
bucket_name = os.environ['bucket_name']
key = os.environ['key']

table = boto3.resource('dynamodb').Table(table_name)

csv_file = s3_resource.Object(bucket_name, key)

items = csv_file.get()['Body'].read().decode('utf-8').splitlines()

reader = csv.reader(items)
header = next(reader)

current_date = datetime.now(pytz.timezone('America/Sao_Paulo')).isoformat()[:-6] + 'Z'

for row in reader:
  print('importing row:', row)
  table.put_item(
    Item={
      'id': row[header.index('id')],
      'number': row[header.index('number')],
      'createdAt': current_date
    }
  )

print('Records imported to DynamoDB table successfully.')