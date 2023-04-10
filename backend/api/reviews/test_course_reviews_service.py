from api.reviews.course_reviews_service import submit_course_review, course_reviews, get_reviews_by_course_code


def test_submit_course_review(mocker):
    mocker.patch(
        'api.reviews.course_reviews_service.course_reviews.insert_one',
        return_value=True
    )

    mocker.patch(
        'api.reviews.course_reviews_service.uuid.uuid4',
        return_value="1"
    )

    mocker.patch(
        'api.reviews.course_reviews_service.time.time',
        return_value="1680495280"
    )

    json_from_create = {'reviewer': 'JOE',
                        "course_code": 'SSW 695',
                        'difficulty': '4',
                        'interest': '4',
                        'usefulness': '4',
                        'organization': '4',
                        'workload': '4',
                        'review_text': 'This is text',
                        'term': 'spring',
                        'year': '2000'}

    expected = {"Message": "Submit Review Success"}
    actual = submit_course_review(json_from_create)

    expected_db_parameter = {
        '_id':"1",
        'Reviewer': "JOE",
        "course_code":'SSW 695',
        'Term': "spring",
        'Year': "2000",
        'Difficulty': "4",
        'Interest': "4",
        'Usefulness': "4",
        'Organization': "4",
        'Workload': "4",
        'ReviewText': "This is text",
        'UpVotes': 0,
        'DownVotes': 0,
        'Status': 'active',
        'CreateDate': "1680495280",
        'ModifiedDate': "1680495280",
    }

    course_reviews.insert_one.assert_called_once_with(expected_db_parameter)
    assert expected == actual

def test_get_reviews_by_course_code(mocker):
    
    mocker.patch(
        'api.reviews.course_reviews_service.course_reviews.find',
        return_value = [ {
        '_id':"1",
        'Reviewer': "Jack",
        "course_code":'SSW 565',
        'Term': "Fall",
        'Year': "2020",
        'Difficulty': "4",
        'Interest': "4",
        'Usefulness': "4",
        'Organization': "4",
        'Workload': "4",
        'ReviewText': "This is text",
        'UpVotes': 0,
        'DownVotes': 0,
        'Status': 'active',
        'CreateDate': "1680495280",
        'ModifiedDate': "1680495280",
    } 
        ]
    )

    argument_1 = get_reviews_by_course_code('SSW 565')

    expected_outcome_1 = [ {
        '_id':"1",
        'Reviewer': "Jack",
        "course_code":'SSW 565',
        'Term': "Fall",
        'Year': "2020",
        'Difficulty': "4",
        'Interest': "4",
        'Usefulness': "4",
        'Organization': "4",
        'Workload': "4",
        'ReviewText': "This is text",
        'UpVotes': 0,
        'DownVotes': 0,
        'Status': 'active',
        'CreateDate': "1680495280",
        'ModifiedDate': "1680495280",
    } 
    ]

    course_reviews.find.assert_called_once_with({"course_code": "SSW 565"})

    assert expected_outcome_1 ==  argument_1


# test case with empty or incorrect input
    mocker.patch(
        'api.reviews.course_reviews_service.course_reviews.find',
        return_value = []
    )

    argument_2 =  get_reviews_by_course_code('')
    expected_outcome_2 = []

    course_reviews.find.assert_called_once_with({'course_code': ''})

    assert expected_outcome_2 ==  argument_2

