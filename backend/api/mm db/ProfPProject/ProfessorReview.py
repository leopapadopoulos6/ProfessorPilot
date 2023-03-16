
from datetime import datetime
import boto3
from ksuid import ksuid


class ProfessorReview:

    dynamodb = boto3.client('dynamodb',  aws_access_key_id   = 'AKIA3NT46V6BTBSGJC2K',
        aws_secret_access_key = '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',
        region_name = 'us-east-2')

    def __init__(self, reviewer):
        
        self.type = 'professor'
        self.id = str(ksuid())
        self.reviewer = reviewer
    
    def create_review(self, professorName, criteria : list[int], text):
        try:
            self.dynamodb.transact_write_items (
                TransactItems = [
                    {
                    "Put": {
                            "TableName": "Reviews",
                            "Item": {
                                "PK": {"S": "REVIEW_TYPE#{}".format(self.type)},
                                "SK": {"S": "{}#{}".format(professorName, self.reviewer)},
                                "GSI1PK": {"S": self.reviewer},
                                "GSI1SK": {"S": "REVIEW_TYPE#{}".format(self.type)},
                                "ProfessorName" : {"S": professorName},            
                                "Communication ": {"N": criteria[0]},
                                "Organization": {"N": criteria[1]},
                                "Availability": {"N": criteria[2]},
                                "Grading": {"N":criteria[3]},
                                "Competency": {"N": criteria[4]},
                                "Rating": {"N": criteria[5]},
                                "ReviewText": {"S": text},
                                "Date": {"S": datetime.now().isoformat()},
                                'ReviewId': {"S": self.id},

                                },
                                "ConditionExpression": "attribute_not_exists(PK)",
                            },
                    }
                ]
           )
            print("Professor review created successfully.")
        except Exception as e:
                print("Could not add professor review to Reviews")
                print(e)

reviewer1 = ProfessorReview("joedoe@stevens.edu")
criteria1 = ['4', '2', '4', '4', '2', '3']

reviewer2 = ProfessorReview("janedoe@stevens.edu")
criteria2 = ['4', '5', '4', '4', '5', '4']

reviewer1.create_review("Paul Allen", criteria1, "I always enjoy his classes")

def delete_review(self):
        pass

def update_review(self):
    pass
    
def get_all_reviews(self):
    pass

def get_user_reviews(self):
    pass

def get_lastest_reviews(self):
    pass

def get_rating(self):
    pass

def update_upvotes(self):
    pass

def get_total_upvotes(self):
    pass