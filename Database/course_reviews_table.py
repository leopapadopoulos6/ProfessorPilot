import boto3
from botocore.exceptions import ClientError


resource = boto3.resource('dynamodb', aws_access_key_id   = '',
        aws_secret_access_key = '',
        region_name = '')

TABLE_NAME = "CourseReviews" 

def create_table():

    try:
        resource.create_table(
            TableName= TABLE_NAME,
            AttributeDefinitions=[
                {"AttributeName": "PK", "AttributeType": "S"},
                {"AttributeName": "SK", "AttributeType": "S"},
                {"AttributeName": "GSI1PK", "AttributeType": "S"},

            ],
            KeySchema=[
            {"AttributeName": "PK", "KeyType": "HASH"},
            {"AttributeName": "SK", "KeyType": "RANGE"},
                
        ],
        GlobalSecondaryIndexes=[
        {
            "IndexName": "User-Reviews-Index",
            "KeySchema": [
                {"AttributeName": "GSI1PK", "KeyType": "HASH"},
            ],
            "Projection": {
            "ProjectionType": "INCLUDE",
            'NonKeyAttributes':['CourseCode','Interest', 'Difficulty', 'Usefulness', 'Workload', 
                                'Organization','Rating', 'ReviewText','Upvotes', 'Status', 'CreateDate',
                                'ModifiedDate','ReviewId','Term', 'Year'
                                ]
                            },   
            "ProvisionedThroughput": {
                "ReadCapacityUnits": 5,
                "WriteCapacityUnits": 5,
            },
        }
            ],
            ProvisionedThroughput={"ReadCapacityUnits": 5, "WriteCapacityUnits": 5},
        )
        print("Table created successfully.")
    except Exception as e:
        print("Could not create table. Error:")
        print(e)

create_table()


def table_exists(self):
    
    try:
        resource.describe_table(TableName=TABLE_NAME)
        exists = True
    except ClientError as ce:
        if ce.response['Error']['Code'] == 'ResourceNotFoundException':
            print("Table " + {self.table} + " does not exist. Create the table first and try again.")
            exists = False
    return exists
            
def delete_table():
    pass
   