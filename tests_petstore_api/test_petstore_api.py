import requests

BASE_URL = "https://petstore.swagger.io/v2"
HEADERS = {"Content-Type": "application/json"}


def test_create_pet_success():
    payload = {
        "id": 100101,
        "name": "Tommy",
        "photoUrls": ["https://example.com/photo.jpg"],
        "status": "available"
    }
    response = requests.post(f"{BASE_URL}/pet", json=payload, headers=HEADERS)

    assert response.status_code == 200
    assert response.json()["name"] == "Tommy"
    assert response.json()["status"] == "available"


def test_get_pet_by_id_success():
    pet_id = 100101
    response = requests.get(f"{BASE_URL}/pet/{pet_id}", headers=HEADERS)

    assert response.status_code == 200
    assert response.json()["id"] == pet_id
    assert response.json()["name"] == "Tommy"


import pytest

# Test creating a pet with missing required fields
def test_create_pet_missing_name():
    payload = {
        "id": 100102,
        "photoUrls": ["https://example.com/photo.jpg"],
        "status": "available"
    }
    response = requests.post(f"{BASE_URL}/pet", json=payload, headers=HEADERS)
    assert response.status_code == 400 or response.status_code == 405  # API may reject missing fields or method

# Test creating a pet with invalid ID type
def test_create_pet_invalid_id_type():
    payload = {
        "id": "invalid_id",
        "name": "InvalidIDPet",
        "photoUrls": ["https://example.com/photo.jpg"],
        "status": "available"
    }
    response = requests.post(f"{BASE_URL}/pet", json=payload, headers=HEADERS)
    assert response.status_code == 400

# Test updating an existing pet successfully
def test_update_pet_success():
    payload = {
        "id": 100101,
        "name": "Tommy Updated",
        "photoUrls": ["https://example.com/photo_updated.jpg"],
        "status": "sold"
    }
    response = requests.put(f"{BASE_URL}/pet", json=payload, headers=HEADERS)
    assert response.status_code == 200
    assert response.json()["name"] == "Tommy Updated"
    assert response.json()["status"] == "sold"

# Test updating non-existent pet
def test_update_nonexistent_pet():
    payload = {
        "id": 99999999,
        "name": "GhostPet",
        "photoUrls": ["https://example.com/ghost.jpg"],
        "status": "available"
    }
    response = requests.put(f"{BASE_URL}/pet", json=payload, headers=HEADERS)
    # Could be 404 or 200 depending on API behavior (it might create if not exist)
    assert response.status_code in [200, 404]

# Test deleting an existing pet
def test_delete_pet_success():
    pet_id = 100101
    response = requests.delete(f"{BASE_URL}/pet/{pet_id}", headers=HEADERS)
    assert response.status_code == 200

# Test deleting a pet that does not exist
def test_delete_pet_nonexistent():
    pet_id = 99999999
    response = requests.delete(f"{BASE_URL}/pet/{pet_id}", headers=HEADERS)
    assert response.status_code == 404 or response.status_code == 400

# Test deleting with invalid ID format
def test_delete_pet_invalid_id():
    pet_id = "invalid_id"
    response = requests.delete(f"{BASE_URL}/pet/{pet_id}", headers=HEADERS)
    assert response.status_code == 400
