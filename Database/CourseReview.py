from ksuid import ksuid
from datetime import datetime
import boto3
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key

class CourseReview:
    
    resource = boto3.resource('dynamodb',  aws_access_key_id   = '',
        aws_secret_access_key = '',
        region_name = 'us-east-2')
    
    TABLE_NAME = "CourseReviews" # table where course reviews will be added
    table = resource.Table(TABLE_NAME)  

    def __init__(self):
        
        self.type = "Course"
        self.date = datetime.now().isoformat()
        self.id = str(ksuid())
        self.overall_rating = 0 # default overall rating
        self.total_reviews = 0  # def total number of reviews
              
    def create_review(self, reviewer, coursename, criteria : list[int], code, text, term, year):
        
        try:
            self.table.put_item(
                        Item = {
                                "PK": "TYPE#{}".format(self.type),
                                "SK": "{}#{}".format(coursename, reviewer),
                                "GSI1PK": reviewer,
                                "CourseCode": code,              
                                "Difficulty": criteria[0],
                                "Interest": criteria[1],
                                "Usefulness": criteria[2],
                                "Organization": criteria[3],
                                "Worload": criteria[4],
                                "Rating": criteria[5],
                                "ReviewText": text,
                                "Term": term,
                                "Year": year,
                                "CreateDate": self.date,
                                'ReviewId': self.id
                            },
                            ConditionExpression =  "attribute_not_exists(SK)"
                            ),
        
            print("Course review created successfully.") 

        except ClientError as ce:
                if ce.response['Error']['Code'] == 'ConditionalCheckFailedException':
                    print("Review already exists. Please update existing review")             
        except Exception as e:
                print("Could not create course review.")
                print(e)
    
    def delete_review(self, reviewer, coursename):
          
        """
        Deletes a course review from the Reviews table.
        """
        try:
            self.table.delete_item(
                Key={"PK": "TYPE#{}".format(self.type),  "SK": "{}#{}".format(coursename, reviewer)},
                )
            print("course review deleted successfully")
    
        except Exception as e:
            print("course review could not be deleted.")
            print(e)


    def update_review(self, reviewer, coursename, criteria:list[int], code, text, term, year):
        """
        Updates course review in the Reviews table
        """
        try:
            self.table.update_item(
                Key = {"PK": "TYPE#{}".format(self.type),  "SK": "{}#{}".format(coursename, reviewer)},
                UpdateExpression = "SET #cod = :o, #txt = :x, #trm = :r, #yr = :y, #dif =:f, #in =:i, #us = :u, #org = :g, #wkl =:w, #rt =:t, #mod =:d" ,
                ExpressionAttributeNames =  {
                    "#cod": "CourseCode",                         
                    "#txt": "ReviewText",                           
                    "#trm": "Term",
                    "#yr": "Year",
                    "#dif": "Difficulty",
                    "#in": "Interest",
                    "#us": "Usefulness",
                    "#org":"Organization",
                    "#wkl":"Workload",
                    "#rt": "Rating",
                    "#mod":"ModifiedDate"
                },
                ExpressionAttributeValues = {
                    ':o': code,
                    ':x': text, 
                    ':r': term, 
                    ':y': year,
                    ':f': criteria[0],
                    ':i': criteria[1],
                    ':u': criteria[2],
                    ':g': criteria[3],
                    ':w': criteria[4],
                    ':t': criteria[5],
                    ':d': self.date
                    },
                    ReturnValues="UPDATED_NEW"
                        )

            print("course review was updated sucessfully")
            
        except Exception as e:
            print("course review could not be updated. Errror: {}".format(e))
    
    def get_course_reviews(self, coursename):
        """Gets reviews of a specific course 
        """
        try:
            response=self.table.query(KeyConditionExpression = Key('PK').eq("TYPE#{}".format(self.type))
                                    & Key("SK").begins_with(coursename)
            )
            print(response['Items'])

        except Exception as e:
              print("could not query {} reviews.".format(self.type))
              print(e)
            
    def get_all_reviews(self):
        """Gets all course reviews 
        """
        try:         
            response = self.table.query(KeyConditionExpression = Key('PK').eq("TYPE#{}".format(self.type))
                    )         
            print(response['Items'])

        except Exception as e:
              print("could not query {} reviews.".format(self.type))
              print(e)     
    
 

# course_list = ["Calculus III", "Introduction to C++", "Calculus I"]
# # reviewer_list = ["johndoe@stevens.edu", "janedoe@stevens.edu"]
# # criteria1 = [4, 4, 5, 5, 3, 5]
# # criteria2 = [3, 1, 2, 3, 3, 3]

# review = CourseReview()

# review.update_review(reviewer_list[1], course_list[0], criteria1, "CS 470", "Great course","Summer","2021")
# reviewer2.create_review(criteria1, "CS 350-B", "Great course","Spring","2022")

# reviewer1.create_review(criteria1, "CS 350-B", " One of the best courses at SIT", "Spring","2023")
# reviewer2.create_review(criteria2, "MATH 250", "Did not meet my expectations","Spring","2021")

# review.delete_review(reviewer_list[1], course_list[0])

# review.get_all_reviews()