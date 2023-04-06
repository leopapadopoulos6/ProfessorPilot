
from api.reviews.course_reviews_service import submit_professor_review, professor_reviews


def test_submit_professor_review(mocker):
    
    mocker.patch(
        'api.reviews.course_reviews_service.professor_reviews.insert_one',
        return_value = True
    )

    mocker.patch(
        'api.reviews.course_reviews_service.uuid.uuid4',
        return_value = "1"
    )

    mocker.patch(
        'api.reviews.course_reviews_service.time.time',
        return_value = "1680495280"
    )

    json_from_create = {
        'professor': "John Doe",
        'Communication': "5",
        'Organization': "5",
        'Availability': "5",
        'Grading': "5",
        'Competency': "5",
        'ReviewText': "This is a test"
    }

    expected = {"Message": "Submit Review Success"}
    actual = submit_professor_review(json_from_create)

    expected_db_parameter = {
        '_id':"1",
        'professor': "John Doe",
        'Communication': "5",
        'Organization': "5",
        'Availability': "5",
        'Grading': "5",
        'Competency': "4",
        'ReviewText': 'This is a test',
        'Upvotes': 0,
        'Status' : "active",
        'CreateDate': "1680495280"
    }
    
    professor_reviews.insert_one.assert_called_once_with(expected_db_parameter)
    assert expected == actual


