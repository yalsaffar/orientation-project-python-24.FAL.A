import pytest
from app import app 
from helpers import validate_fields, validate_phone_number



@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_index(client):
    """Test the index route"""
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b"Welcome to MLH 24.FAL.A.2 Orientation API Project!!"
def test_client():
    '''
    Makes a request and checks the message received is the same
    '''
    response = app.test_client().get('/test')
    assert response.status_code == 200
    assert response.json['message'] == "Hello, World!"
def test_experience(client):
    '''
    Add a new experience and then get all experiences.

    Check that it returns the new experience in that list.
    '''
    example_experience = {
        "title": "Software Developer",
        "company": "A Cooler Company",
        "start_date": "October 2022",
        "end_date": "Present",
        "description": "Writing JavaScript Code",
        "logo": "example-logo.png"
    }

    post_response = client.post('/resume/experience', json=example_experience)
    assert post_response.status_code == 201
    item_id = post_response.json['id']
    get_response = client.get('/resume/experience')
    assert get_response.status_code == 200
    assert get_response.json[item_id]['title'] == example_experience['title']
    assert get_response.json[item_id]['company'] == example_experience['company']


def test_education(client):
    '''
    Add a new education and then get all educations.

    Check that it returns the new education in that list.
    '''
    example_education = {
        "course": "Engineering",
        "school": "NYU",
        "start_date": "October 2022",
        "end_date": "August 2024",
        "grade": "86%",
        "logo": "example-logo.png"
    }

    post_response = client.post('/resume/education', json=example_education)
    assert post_response.status_code == 201
    item_id = post_response.json['id']
    get_response = client.get('/resume/education')
    assert get_response.status_code == 200
    assert get_response.json[item_id]['course'] == example_education['course']
    assert get_response.json[item_id]['school'] == example_education['school']


def test_skill(client):
    '''
    Add a new skill and then get all skills.

    Check that it returns the new skill in that list.
    '''
    example_skill = {
        "name": "JavaScript",
        "proficiency": "2-4 years",
        "logo": "example-logo.png"
    }

    post_response = client.post('/resume/skill', json=example_skill)
    assert post_response.status_code == 201
    item_id = post_response.json['id']
    get_response = client.get('/resume/skill')
    assert get_response.status_code == 200
    assert get_response.json[item_id]['name'] == example_skill['name']
    assert get_response.json[item_id]['proficiency'] == example_skill['proficiency']


def test_post_user_information():
    '''
    Test the POST request for user information.
    It should allow setting user information and return status code 201.
    '''
    new_user_info = {
        "name": "John Doe",
        "email_address": "john@example.com",
        "phone_number": "+237680162416"

    }
    response = app.test_client().post('/resume/user_information', json=new_user_info)
    assert response.status_code == 201
    assert response.json['name'] == new_user_info['name']
    assert response.json['email_address'] == new_user_info['email_address']
    assert response.json['phone_number'] == new_user_info['phone_number']


def test_validate_fields_all_present():
    '''
    Expect no missing fields
    '''
    request_data = {
        "name": "John Doe",
        "email_address": "john@example.com",
        "phone_number": "+123456789"
    }

    result = validate_fields(
        ["name", "email_address", "phone_number"], request_data)

    assert result == []


def test_validate_fields_missing_field():
    '''
    Expect 'phone_number' to be missing
    '''
    request_data = {
        "name": "John Doe",
        "email_address": "john@example.com"
    }

    result = validate_fields(
        ["name", "email_address", "phone_number"], request_data)

    assert result == ["phone_number"]


def test_valid_phone_number():
    '''
    Test a valid properly internationalized phone number returns True.
    '''
    valid_phone = "+14155552671"
    assert validate_phone_number(valid_phone) is True


def test_invalid_phone_number():
    '''
<<<<<<< Tabnine <<<<<<<
    def test_client():#+
        """#+
        This function tests the client endpoint of the application. It sends a GET request to '/test'#+
        and verifies that the response status code is 200 and the message received is "Hello, World!".#+
    #+
        Parameters:#+
        None#+
    #+
        Returns:#+
        None#+
    #+
        Raises:#+
        None#+
        """#+
        response = app.test_client().get('/test')#+
        assert response.status_code == 200#+
        assert response.json['message'] == "Hello, World!"#+
>>>>>>> Tabnine >>>>>>># {"conversationId":"5f5bba52-d20a-4fc0-93f1-d7943e31df71","source":"instruct"}
    Test an invalid phone number returns False.
    '''
    invalid_phone = "123456"
    assert validate_phone_number(invalid_phone) is False
