from requests_folder.episodes.get_users_saved_episodes import get_users_saved_episodes


class TestGetUsersSavedEpisodes:


#Get Users Saved Episodes valid params

    def test_get_users_saved_episodes_valid_params_response_has_a_200_status_code(self):
        response = get_users_saved_episodes("50", "0", "RO")
        assert response.status_code == 200

    def test_get_users_saved_episodes_valid_params_response_time_is_less_than_200ms(self):
        response = get_users_saved_episodes("50", "0", "RO")
        assert response.elapsed.total_seconds() * 1000 < 200



#Get Users Saved Episodes valid params

    def test_get_users_saved_episodes_valid_data_response_has_a_200_status_code(self):
        response = get_users_saved_episodes("25", "2", "GB")
        assert response.status_code == 200

    def test_get_users_saved_episodes_valid_data_response_time_is_less_than_200ms(self):
        response = get_users_saved_episodes("25", "2", "GB")
        assert response.elapsed.total_seconds() * 1000 < 200



#Get Users Saved Episodes invalid market

    def test_get_users_saved_episodes_invalid_market_response_has_a_400_status_code(self):
        response = get_users_saved_episodes("25", "2", "OO")
        assert response.status_code == 400

    def test_get_users_saved_episodes_invalid_market_response_is_JSON(self):
        response = get_users_saved_episodes("25", "2", "OO")
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8'

    def test_get_users_saved_episodes_invalid_market_response_is_an_object(self):
        response = get_users_saved_episodes("25", "2", "OO")
        assert isinstance(response.json(), dict)

    def test_get_users_saved_episodes_invalid_market_error_object_exists(self):
        response = get_users_saved_episodes("25", "2", "OO")
        assert 'error' in response.json()

    def test_get_users_saved_episodes_invalid_market_error_status_is_400(self):
        response = get_users_saved_episodes("25", "2", "OO")
        assert response.json().get('error', {}).get('status') == 400

    def test_get_users_saved_episodes_invalid_market_error_message_is_invalid_market_code(self):
        response = get_users_saved_episodes("25", "2", "OO")
        assert response.json().get('error', {}).get('message') == 'Invalid market code'

    def test_get_users_saved_episodes_invalid_market_response_time_is_less_than_500ms(self):
        response = get_users_saved_episodes("25", "2", "OO")
        assert response.elapsed.total_seconds() * 1000 < 500



#Get Users Saved Episodes invalid limit

    def test_get_users_saved_episodes_invalid_params_response_has_a_400_status_code(self):
        response = get_users_saved_episodes("\\", "2", "RO")
        assert response.status_code == 400

    def test_get_users_saved_episodes_invalid_params_response_body_is_not_existent(self):
        response = get_users_saved_episodes("\\", "2", "RO")
        assert response.text == ""

    def test_get_users_saved_episodes_invalid_params_response_does_not_contain_error(self):
        response = get_users_saved_episodes("\\", "2", "RO")
        assert "error" not in response.text

    def test_get_users_saved_episodes_invalid_params_response_body_is_empty(self):
        response = get_users_saved_episodes("\\", "2", "RO")
        assert response.text == ""

    def test_get_users_saved_episodes_invalid_params_response_body_length_is_0(self):
        response = get_users_saved_episodes("\\", "2", "RO")
        assert len(response.text) == 0

    def test_get_users_saved_episodes_invalid_params_response_is_not_null(self):
        response = get_users_saved_episodes("\\", "2", "RO")
        assert response.text is not None

    def test_get_users_saved_episodes_invalid_params_response_does_not_contain_message(self):
        response = get_users_saved_episodes("\\", "2", "RO")
        assert "message" not in response.text
