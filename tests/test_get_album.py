from requests_folder.albums.get_album import get_album_without_market, get_album_with_valid_market, \
    get_album_with_invalid_market


class TestAlbums:

    
#GET ALBUM NO MARKET
    
    def test_get_album_without_market_status_code(self):
        response = get_album_without_market("01u9MdrytYwPidRT0uoCXR")
        assert response.status_code == 200
    
    def test_get_album_without_market_response_time(self):
        response = get_album_without_market("01u9MdrytYwPidRT0uoCXR")
        assert response.responseTime < 3000
    
    def test_get_album_without_market_response_contains_album_type(self):
        response = get_album_without_market("01u9MdrytYwPidRT0uoCXR")
        assert "album_type" in response.text()
    
    def test_get_album_without_market_response_contains_id(self):
        response = get_album_without_market("01u9MdrytYwPidRT0uoCXR")
        assert "ID" in response.text()
    
    def test_get_album_without_market_response_contains_keys_specified_in_api(self):
        response = get_album_without_market("01u9MdrytYwPidRT0uoCXR")
        keys_to_check = ["market", "release_date", "id", "total_tracks", "available_markets"]
        for key in keys_to_check:
            assert key in response.text()
    


#GET ALBUM with valid market

    def test_get_album_with_valid_market_status_code(self):
        response = get_album_with_valid_market("7qNY7C7rkJwioya4lKLrJt", "RO")
        assert response.status_code == 200
    
    def test_get_album_with_valid_market_response_time(self):
        response = get_album_with_valid_market("7qNY7C7rkJwioya4lKLrJt", "RO")
        assert response.responseTime < 3000
    
    def test_get_album_with_valid_market_response_contains_album_type(self):
        response = get_album_with_valid_market("7qNY7C7rkJwioya4lKLrJt", "RO")
        assert "album_type" in response.text()
    
    def test_get_album_with_valid_market_response_contains_id(self):
        response = get_album_with_valid_market("7qNY7C7rkJwioya4lKLrJt", "RO")
        assert "ID" in response.text()
    
    def test_get_album_with_valid_market_response_contains_keys_specified_in_api(self):
        response = get_album_with_valid_market("7qNY7C7rkJwioya4lKLrJt", "RO")
        keys_to_check = ["tracks", "images", "href", "artists", "available_markets"]
        for key in keys_to_check:
            assert key in response.text()



#GET ALBUM with invalid market

    def test_get_album_with_invalid_market_status_code(self):
        response = get_album_with_invalid_market("7qNY7C7rkJwioya4lKLrJt", "kkk")
        assert response.status_code == 400
    
    def test_get_album_with_invalid_market_response_time(self):
        response = get_album_with_invalid_market("7qNY7C7rkJwioya4lKLrJt", "kkk")
        assert response.responseTime < 3000
    
    def test_get_album_with_invalid_market_check_error_object_exists(self):
        response = get_album_with_invalid_market("7qNY7C7rkJwioya4lKLrJt", "kkk")
        assert "error" in response.json()
    
    def test_get_album_with_invalid_market_check_response_is_valid_json(self):
        response = get_album_with_invalid_market("7qNY7C7rkJwioya4lKLrJt", "kkk")
        assert response.to_be_json
    
    def test_get_album_with_invalid_market_check_error_in_response(self):
        response = get_album_with_invalid_market("7qNY7C7rkJwioya4lKLrJt", "kkk")
        assert "error" in response.text()
    
    def test_get_album_with_invalid_market_check_error_message_type(self):
        response = get_album_with_invalid_market("7qNY7C7rkJwioya4lKLrJt", "kkk")
        assert type(response.json().error.message) == str
    
    def test_get_album_with_invalid_market_check_error_message_contains_invalid_market_code(self):
        response = get_album_with_invalid_market("7qNY7C7rkJwioya4lKLrJt", "kkk")
        assert "Invalid market code" in response.json().error.message
    
    def test_get_album_with_invalid_market_check_error_object_not_empty(self):
        response = get_album_with_invalid_market("7qNY7C7rkJwioya4lKLrJt", "kkk")
        assert response.json().error
    


#GET ALBUM with invalid market 2

    def test_get_album_with_invalid_market2_status_code(self):
        response = get_album_with_invalid_market("7qNY7C7rkJwioya4lKLrJt", "288")
        assert response.status_code == 400
    
    def test_get_album_with_invalid_market2_response_time(self):
        response = get_album_with_invalid_market("7qNY7C7rkJwioya4lKLrJt", "288")
        assert response.responseTime < 3000
    
    def test_get_album_with_invalid_market2_check_error_object_exists(self):
        response = get_album_with_invalid_market("7qNY7C7rkJwioya4lKLrJt", "288")
        assert "error" in response.json()
    
    def test_get_album_with_invalid_market2_check_response_is_valid_json(self):
        response = get_album_with_invalid_market("7qNY7C7rkJwioya4lKLrJt", "288")
        assert response.to_be_json
    
    def test_get_album_with_invalid_market2_check_error_in_response(self):
        response = get_album_with_invalid_market("7qNY7C7rkJwioya4lKLrJt", "288")
        assert "error" in response.text()
    
    def test_get_album_with_invalid_market2_check_error_message_type(self):
        response = get_album_with_invalid_market("7qNY7C7rkJwioya4lKLrJt", "288")
        assert type(response.json().error.message) == str
    
    def test_get_album_with_invalid_market2_check_error_message_contains_invalid_market_code(self):
        response = get_album_with_invalid_market("7qNY7C7rkJwioya4lKLrJt", "288")
        assert "Invalid market code" in response.json().error.message
    
    def test_get_album_with_invalid_market2_check_error_object_not_empty(self):
        response = get_album_with_invalid_market("7qNY7C7rkJwioya4lKLrJt", "288")
        assert response.json().error
