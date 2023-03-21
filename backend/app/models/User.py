import boto3
from datetime import datetime


class User:
     
    dynamodb = boto3.client('dynamodb',   aws_access_key_id   = 'AKIA3NT46V6BTBSGJC2K',
        aws_secret_access_key = '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',
        region_name = 'us-east-2',)
     
    def __init__(self, University,Username, Email, Position) -> None:
          
        self.university = University
        self.username = Username
        self.email = Email
        self.position = Position
        self.table = "Reviews" # default table name where users will be added
     
    def create_user(self):

        try:
            self.dynamodb.transact_write_items(
                TransactItems = [
                    {  
                    "Put": {
                    "TableName": "Reviews",
                            "Item": {
                                "PK" : {"S": "UNIV#{}".format(self.university)},
                                "SK" : {"S" : self.email},
                                "Username" :{"S": self.username},
                                "Position": {"S": self.position},
                                "Date": {"S": datetime.now().isoformat()},
                                },
                                "ConditionExpression": "attribute_not_exists(SK)",
                                },
                        }
                    ]
                )  
            print("Added {} as a {}. Email:{}".format(self.username, self.position, self.email))
            
        except Exception as e:
                print("Could not add User. Error:"+{e})

    def update_user():
        pass

    def get_user():
        pass
    
    def delete_user(self):
        pass
        
    
        
