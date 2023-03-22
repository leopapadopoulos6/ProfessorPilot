from datetime import datetime
import boto3
from ksuid import ksuid
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key



class ProfessorReview:

    resource = boto3.resource('dynamodb',  aws_access_key_id   = '',
        aws_secret_access_key = '',
        region_name = '')
    
    TABLE_NAME = "ProfessorReviews" # default table where professor reviews will be added

    table = resource.Table(TABLE_NAME) 

    def __init__(self):
        
        self.type = 'Professor'
        self.id = str(ksuid())
        self.date = datetime.now().isoformat()
    
    def create_review(self, reviewer, professorname, criteria : list[int], text):
        try:
            self.table.put_item (
                
                    Item =  {
                        "PK": "TYPE#{}".format(self.type),
                        "SK": "{}#{}".format(professorname, reviewer),
                        "GSI1PK": reviewer,
                        "Communication": criteria[0],
                        "Organization": criteria[1],
                        "Availability": criteria[2],
                        "Grading":  criteria[3],
                        "Competency": criteria[4],
                        "Rating": criteria[5],
                        "ReviewText": text,
                        "CreateDate": self.date,
                        'ReviewId': self.id
                        },
                        ConditionExpression =  "attribute_not_exists(SK)",
                    )
            
            print("Professor review created successfully.")
        
        except ClientError as ce:
                if ce.response['Error']['Code'] == 'ConditionalCheckFailedException':
                    print("Review already exists. Please select yes to update existing review") 
        except Exception as unknown:
                print("Could not create professor review")
                print(unknown)


    def delete_review(self,reviewer, professorname):
          
        """
        Deletes a professor review from the Reviews table.
        """
        try:
            self.table.delete_item(
                Key={"PK": "TYPE#{}".format(self.type),  "SK": "{}#{}".format(professorname, reviewer)},
                )
            print("professor review deleted successfully")
        except Exception as e:
            print(" review could not be deleted.")
            print(e)

    def update_review(self,reviewer, professorname, criteria:list[int], text):
        """
        Updates course review in the Reviews table
        """
        try:
            self.table.update_item(
                Key = {"PK": "TYPE#{}".format(self.type),  "SK": "{}#{}".format(professorname, reviewer)},
                UpdateExpression = "SET #com =:c, #org =:g, #avl =:a, #grd=:r, #cpy =:y, #rtg =:i, #txt =:t, #mod=:d" ,
                ExpressionAttributeNames =  { 
                    "#com": "Communication",                          
                    "#org": "Organization",
                    "#avl": "Availability",
                    "#grd": "Grading",
                    "#cpy": "Competency",
                    "#rtg": "Rating",
                    "#txt": "ReviewText",
                    "#mod": "ModifiedDate"
                },
                ExpressionAttributeValues = {
                    ':c': criteria[0],
                    ':g': criteria[1],
                    ':a': criteria[2],
                    ':r': criteria[3],
                    ':y': criteria[4],
                    ':i': criteria[5],
                    ':t': text,
                    ':d': self.date
                    },
                    ReturnValues="UPDATED_NEW"
                        )

            print("professor review was updated sucessfully")
            
        except Exception as e:
            print("professor review could not be updated. Errror: {}".format(e))


    def get_professor_reviews(self, professorname):
        """Gets reviews of a specific professor
        """
        try:
            response=self.table.query(KeyConditionExpression = Key('PK').eq("TYPE#{}".format(self.type))
                                    & Key("SK").begins_with(professorname)
            )
            print(response['Items'])

        except Exception as e:
              print("could not query {} reviews.".format(self.type))
              print(e)

    def get_all_reviews(self):
        """Gets all professor reviews 
        """
        try:         
            response = self.table.query(KeyConditionExpression = Key('PK').eq("TYPE#{}".format(self.type))
                    )         
            print(response['Items'])

        except Exception as e:
              print("could not query {} reviews.".format(self.type))
              print(e)     
    

# professorname = ["Paul Allen", "Henry Lee", "Frank Zac"]
# reviewer = ["johndoe@stevens.edu", "janedoe@stevens.edu"]
# criteria1 = [5, 5, 5, 4, 5, 5]
# criteria2 = [4, 3, 2, 3, 2, 3]

# review = ProfessorReview()

# # review.update_review(reviewer[0], professorname[0], criteria1, " He is a good Professor")

# # review.delete_review(reviewer[1], professorname[1])
# # review.get_professor_reviews(professorname[2])