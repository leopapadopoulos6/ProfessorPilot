import boto3
from botocore.exceptions import ClientError


dynamodb = boto3.client('dynamodb',   aws_access_key_id   = 'AKIA3NT46V6BTBSGJC2K',
        aws_secret_access_key = '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',
        region_name = 'us-east-2',)


def create_table():

    try:
        dynamodb.create_table(
            TableName= "Reviews",
            AttributeDefinitions=[
                {"AttributeName": "PK", "AttributeType": "S"},
                {"AttributeName": "SK", "AttributeType": "S"},
                {"AttributeName": "GSI1PK", "AttributeType": "S"},
                {"AttributeName": "GSI1SK", "AttributeType": "S"},

            ],
            KeySchema=[
            {"AttributeName": "PK", "KeyType": "HASH"},
            {"AttributeName": "SK", "KeyType": "RANGE"},
                
        ],
        GlobalSecondaryIndexes=[
        {
            "IndexName": "User-Review-Index",
            "KeySchema": [
                {"AttributeName": "GSI1PK", "KeyType": "HASH"},
                {"AttributeName": "GSI1SK", "KeyType": "RANGE"},

            ],
            "Projection": {
            "ProjectionType": "INCLUDE",
            'NonKeyAttributes':['ProfessorName','Communication','Organization',
                                'Availability','Grading', 'Competency', 'Rating', 'ReviewText',
                                'Upvotes', 'Date', 'Status', 'ReviewId', 'CourseName', 'CourseCode',
                                'Interest', 'Difficulty', 'Usefulness', 'Workload',
                                'Term', 'Year'
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

def table_exists(table):

        table = dynamodb.Table(table)
        try:
            response = dynamodb.describe_table(TableName=table)
            return True    
        except ClientError as ce:
            if ce.response['Error']['Code'] == 'ResourceNotFoundException':
                print("Table " + {table} + " does not exist. Create the table first and try again.")
                return False
            
def delete_table():
    pass
   