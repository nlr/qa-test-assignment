import requests
import pytest

BASE_URL = 'https://jsonplaceholder.typicode.com'

GET_POSTS_ENDPOINT = '/posts'
POST_POSTS_ENDPOINT = '/posts'
DELETE_POSTS_ENDPOINT = '/posts'

PARAMS = {
    'userId': 1,
    'id': 1,
    'title': 'Test Title',
    'body': 'Test Body'
}


def test_get_posts():
    response = requests.get(BASE_URL + GET_POSTS_ENDPOINT)
    assert response.status_code == 200

    # Дополнительные проверки
    posts = response.json()
    assert len(posts) > 0  # Проверка, что получены как минимум один пост

    for post in posts:
        assert 'userId' in post
        assert 'id' in post
        assert 'title' in post
        assert 'body' in post


def test_post_posts():
    response = requests.post(BASE_URL + POST_POSTS_ENDPOINT, json=PARAMS)
    assert response.status_code == 201

    # Дополнительные проверки
    created_post = response.json()
    assert created_post['title'] == PARAMS['title']
    assert created_post['body'] == PARAMS['body']
    assert created_post['userId'] == PARAMS['userId']

    # Проверка, что созданный пост содержит сгенерированный id
    assert 'id' in created_post


def test_delete_posts():
    response = requests.delete(BASE_URL + DELETE_POSTS_ENDPOINT + '/1')
    assert response.status_code == 200
