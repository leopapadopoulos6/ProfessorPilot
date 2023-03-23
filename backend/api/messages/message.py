class Message:
    def __init__(self, text):
        self.text = text
        self.metadata = vars(Metadata())

class Metadata:
    def __init__(self):
        self.api = "api_flask_python_hello-world"
        self.branch = "basic-role-based-access-control"


# class Professor:
#     def __init__(self, professor_id, fname, lname, email, school, overall, difficulty, take_again):
#         self.professor_id = professor_id
#         self.fname = fname
#         self.lname = lname
#         self.email = email
#         self.school = school
#         self.overall = overall
#         self.difficulty = difficulty
#         self.take_again = take_again


# class Course:
#     def __init__(self, course_id, course_name, department, description):
#         self.course_id = course_id
#         self.course_name = course_name
#         self.department = department
#         self.description = description

#     def __str__(self):
#         return f"{self.course_id}: {self.course_name} ({self.department}) {self.description}"
    
# class CourseReview:
#     def __init__(self, overall_rating, easiness, interest, usefulness, difficulty, professor_name, term, year, delivery_method, grade, workload, course_review_description, professor_review_description):
#         self.overall_rating = overall_rating
#         self.easiness = easiness
#         self.interest = interest
#         self.usefulness = usefulness
#         self.difficulty = difficulty
#         self.professor_name = professor_name
#         self.term = term
#         self.year = year
#         self.delivery_method = delivery_method
#         self.grade = grade
#         self.workload = workload
#         self.course_review_description = course_review_description
#         self.professor_review_description = professor_review_description

#     def __str__(self):
#         return f"Course Review: {self.overall_rating}/5, {self.easiness}/5, {self.interest}/5, {self.usefulness}/5, {self.difficulty}/5, {self.professor_name}, {self.term}, {self.year}, {self.delivery_method}, {self.grade}, {self.workload}, {self.course_review_description}, {self.professor_review_description}"


# class ProfessorReview:
#     def __init__(self, overall_rating, easiness, punctuality, leniency, difficulty, course_name, term, year, delivery_method, grade, workload, review_description):
#         self.overall_rating = overall_rating
#         self.easiness = easiness
#         self.punctuality = punctuality
#         self.leniency = leniency
#         self.difficulty = difficulty
#         self.course_name = course_name
#         self.term = term
#         self.year = year
#         self.delivery_method = delivery_method
#         self.grade = grade
#         self.workload = workload
#         self.review_description = review_description

#     def __str__(self):
#         return f"Professor Review: {self.overall_rating}/5, {self.easiness}/5, {self.punctuality}/5, {self.leniency}/5, {self.difficulty}/5, {self.course_name}, {self.term}, {self.year}, {self.delivery_method}, {self.grade}, {self.workload}, {self.review_description}"