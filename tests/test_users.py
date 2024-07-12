import pytest
import requests

def test_valid_credentials(mocker):
    url = 'http://127.0.0.1:8000/users/'
    params = {'username': 'admin', 'password': 'qwerty'}
    
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mocker.patch('requests.get', return_value=mock_response)
    
    response = requests.get(url, params=params)
    assert response.status_code == 200

def test_invalid_credentials(mocker):
    url = 'http://127.0.0.1:8000/users/'
    params = {'username': 'admin', 'password': 'admin'}
    
    mock_response = mocker.Mock()
    mock_response.status_code = 401
    mocker.patch('requests.get', return_value=mock_response)
    
    response = requests.get(url, params=params)
    assert response.status_code == 401
