from requests_folder.shows.get_show_episodes import get_show_episodes


class TestGetShowEpisodes:


#Get Show Episodes valid params
    
    def test_get_show_episodes_valid_params_status_code(self):
        response = get_show_episodes("2i93Ub9rGWTNVyEg0rsxPb", "2", "1", "RO")
        assert response.status_code == 200

    def test_get_show_episodes_valid_params_response_time(self):
        response = get_show_episodes("2i93Ub9rGWTNVyEg0rsxPb", "2", "1", "RO")
        assert response.response_time < 3000



#Get Show Episodes invalid market

    def test_get_show_episodes_invalid_market_status_code(self):
        response = get_show_episodes("2i93Ub9rGWTNVyEg0rsxPb", "2", "1", "PPI")
        assert response.status_code == 400

    def test_get_show_episodes_invalid_market_response_time(self):
        response = get_show_episodes("2i93Ub9rGWTNVyEg0rsxPb", "2", "1", "PPI")
        assert response.response_time < 500

    def test_get_show_episodes_invalid_market_json(self):
        response = get_show_episodes("2i93Ub9rGWTNVyEg0rsxPb", "2", "1", "PPI")
        assert response.json() == {"error": {"status": 400, "message": "Invalid market code"}}



#Get Show Episodes invalid id

    def test_get_show_episodes_invalid_ids_status_code(self):
        response = get_show_episodes("2I93Ub9rGWTNVyEg0rsxPb", "2", "1", "RO")
        assert response.status_code == 404

    def test_get_show_episodes_invalid_ids_content_type(self):
        response = get_show_episodes("2I93Ub9rGWTNVyEg0rsxPb", "2", "1", "RO")
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8'

    def test_get_show_episodes_invalid_ids_body_contains_error(self):
        response = get_show_episodes("2I93Ub9rGWTNVyEg0rsxPb", "2", "1", "RO")
        assert 'error' in response.json()

    def test_get_show_episodes_invalid_ids_body_contains_message(self):
        response = get_show_episodes("2I93Ub9rGWTNVyEg0rsxPb", "2", "1", "RO")
        assert 'message' in response.json()['error']

    def test_get_show_episodes_invalid_ids_error_status(self):
        response = get_show_episodes("2I93Ub9rGWTNVyEg0rsxPb", "2", "1", "RO")
        assert response.json()['error']['status'] == 404

    def test_get_show_episodes_invalid_ids_error_message(self):
        response = get_show_episodes("2I93Ub9rGWTNVyEg0rsxPb", "2", "1", "RO")
        assert response.json()['error']['message'] == 'non existing id'



#Get Show Episodes invalid limit

    def test_get_show_episodes_invalid_limit_status_code(self):
        response = get_show_episodes("2i93Ub9rGWTNVyEg0rsxPb", "1+7", "1", "RO")
        assert response.status_code == 400

    def test_get_show_episodes_invalid_limit_contains_error_message(self):
        response = get_show_episodes("2i93Ub9rGWTNVyEg0rsxPb", "1+7", "1", "RO")
        assert 'Invalid limit, must be a number between 1 and 50' in response.text()

    def test_get_show_episodes_invalid_limit_error_message_minimum_limit(self):
        response = get_show_episodes("2i93Ub9rGWTNVyEg0rsxPb", "1+7", "1", "RO")
        assert 'number between 1 and 50' in response.text()

    def test_get_show_episodes_invalid_limit_error_message_maximum_limit(self):
        response = get_show_episodes("2i93Ub9rGWTNVyEg0rsxPb", "1+7", "1", "RO")
        assert 'number between 1 and 50' in response.text()

    def test_get_show_episodes_invalid_limit_error_message_specific(self):
        response = get_show_episodes("2i93Ub9rGWTNVyEg0rsxPb", "1+7", "1", "RO")
        assert 'Invalid limit' in response.text()
