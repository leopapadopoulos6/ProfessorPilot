from ksuid import ksuid
from datetime import datetime
import boto3


class CourseReview:

    dynamodb = boto3.client('dynamodb',  aws_access_key_id   = 'AKIA3NT46V6BTBSGJC2K',
        aws_secret_access_key = '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',
        region_name = 'us-east-2')

    def __init__(self, reviewer):
        
        self.type = 'course'
        self.id = str(ksuid())
        self.reviewer = reviewer
        
    def create_review(self, coursename, criteria : list[int], code, text, term, year):
        
        try:
            self.dynamodb.transact_write_items (
                TransactItems = [
                    {
                    "Put": {
                            "TableName": "Reviews",
                            "Item": {
                                "PK": {"S": "REVIEW_TYPE#{}".format(self.type)},
                                "SK": {"S": "{}#{}".format(coursename, self.reviewer)},
                                "GSI1PK": {"S": self.reviewer},
                                "CourseName" : {"S": coursename},
                                "CourseCode": {"S": code},              
                                "Difficulty": {"N": criteria[0]},
                                "Interest": {"N": criteria[1]},
                                "Usefulness": {"N": criteria[2]},
                                "Organization": {"N":criteria[3]},
                                "Worload": {"N": criteria[4]},
                                "Rating": {"N": criteria[5]},
                                "ReviewText": {"S": text},
                                "Term": {"S": term},
                                "Year": {"S": year},
                                "Date": {"S": datetime.now().isoformat()},
                                'ReviewId': {"S": self.id},

                                },
                                "ConditionExpression": "attribute_not_exists(PK)",
                            },
                    }
                ]
           )
            print("Course review created successfully.")
        except Exception as e:
                print("Could not add course review to Reviews")
                print(e)
    



    
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

    def add_upvotes(self):
        pass

    def get_total_upvotes(self):
        pass

    
