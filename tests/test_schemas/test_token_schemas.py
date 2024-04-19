import pytest
from pydantic import ValidationError
from app.schemas.token_schemas import Token, TokenData, RefreshTokenRequest

# Test Token model
def test_token_model():
    # Initialization with explicit values
    access_token = "jhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
    token = Token(access_token=access_token, token_type="bearer")
    assert token.access_token == access_token
    assert token.token_type == "bearer"

    # Validate default and schema correctness
    default_token = Token(access_token=access_token)
    assert default_token.token_type == "bearer"
    assert Token.schema()["properties"]["token_type"]["default"] == "bearer"

    # Test against model example
    example_token = Token(**Token.schema()['example'])
    assert example_token.access_token == access_token
    assert example_token.token_type == "bearer"

# Test TokenData model
def test_token_data_model():
    # Initialization with explicit values
    username = "user@example.com"
    token_data = TokenData(username=username)
    assert token_data.username == username

    # Test for None as a default value
    no_username_token_data = TokenData()
    assert no_username_token_data.username is None

    # Test against model example
    example_token_data = TokenData(**TokenData.schema()['example'])
    assert example_token_data.username == username

# Test RefreshTokenRequest model
def test_refresh_token_request_model():
    # Initialization with explicit values
    refresh_token = "jhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
    refresh_request = RefreshTokenRequest(refresh_token=refresh_token)
    assert refresh_request.refresh_token == refresh_token

    # Test against model example
    example_refresh_request = RefreshTokenRequest(**RefreshTokenRequest.schema()['example'])
    assert example_refresh_request.refresh_token == refresh_token

    # Test for schema validation errors
    with pytest.raises(ValidationError):
        RefreshTokenRequest()  # Missing mandatory field
