from requests_folder.episodes.get_episode import get_episode


class TestGetEpisode:


#Get Episode valid params

    def test_get_episode_status_code_is_200(self):
        response = get_episode("6fppkhPnw5PCspRVGhZhOG", "RO")
        assert response.status_code == 200
    
    def test_get_episode_response_time_is_less_than_200ms(self):
        response = get_episode("6fppkhPnw5PCspRVGhZhOG", "RO")
        assert response.elapsed.total_seconds() * 1000 < 200
    
    def test_get_episode_check_if_the_response_is_valid_JSON(self):
        response = get_episode("6fppkhPnw5PCspRVGhZhOG", "RO")
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8'
    
    def test_get_episode_check_if_audio_preview_url_exists(self):
        response = get_episode("6fppkhPnw5PCspRVGhZhOG", "RO")
        assert 'audio_preview_url' in response.json()
    
    def test_get_episode_check_if_error_shows_up_in_response(self):
        response = get_episode("6fppkhPnw5PCspRVGhZhOG", "RO")
        assert 'error' not in response.text()
    
    def test_get_episode_check_if_explicit_is_a_boolean(self):
        response = get_episode("6fppkhPnw5PCspRVGhZhOG", "RO")
        assert isinstance(response.json()['explicit'], bool)
    
    def test_get_episode_check_if_images_array_has_at_least_one_item(self):
        response = get_episode("6fppkhPnw5PCspRVGhZhOG", "RO")
        assert isinstance(response.json()['images'], list) and len(response.json()['images']) >= 1
    
    def test_get_episode_check_if_language_is_en_US(self):
        response = get_episode("6fppkhPnw5PCspRVGhZhOG", "RO")
        assert response.json()['language'] == "en-US"
    
    def test_get_episode_check_if_external_urls_has_a_Spotify_URL(self):
        response = get_episode("6fppkhPnw5PCspRVGhZhOG", "RO")
        external_urls = response.json()['external_urls']
        assert 'spotify' in external_urls



#Get Episode invalid market, valid id

    def test_get_episode_response_has_a_400_status_code(self):
        response = get_episode("6fppkhPnw5PCspRVGhZhOG", "ZZ")
        assert response.status_code == 400

    def test_get_episode_response_is_JSON(self):
        response = get_episode("6fppkhPnw5PCspRVGhZhOG", "ZZ")
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8'

    def test_get_episode_response_is_an_object(self):
        response = get_episode("6fppkhPnw5PCspRVGhZhOG", "ZZ")
        assert isinstance(response.json(), dict)

    def test_get_episode_error_object_exists(self):
        response = get_episode("6fppkhPnw5PCspRVGhZhOG", "ZZ")
        assert 'error' in response.json()

    def test_get_episode_error_message_is_Invalid_market_code(self):
        response = get_episode("6fppkhPnw5PCspRVGhZhOG", "ZZ")
        assert response.json().get('error', {}).get('message') == 'Invalid market code'

    def test_get_episode_error_status_code_is_400(self):
        response = get_episode("6fppkhPnw5PCspRVGhZhOG", "ZZ")
        assert response.json().get('error', {}).get('status') == 400

    def test_get_episode_error_object_contains_message_key(self):
        response = get_episode("6fppkhPnw5PCspRVGhZhOG", "ZZ")
        assert 'message' in response.json().get('error', {})

    def test_get_episode_error_object_contains_status_key(self):
        response = get_episode("6fppkhPnw5PCspRVGhZhOG", "ZZ")
        assert 'status' in response.json().get('error', {})



#Get Episode valid market, invalid id

    def test_get_episode_invalid_id_response_has_a_404_status_code(self):
        response = get_episode("5fppkhPnw5PCspRVGhZhOG", "RO")
        assert response.status_code == 404

    def test_get_episode_invalid_id_response_is_JSON(self):
        response = get_episode("5fppkhPnw5PCspRVGhZhOG", "RO")
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8'

    def test_get_episode_invalid_id_response_is_an_object(self):
        response = get_episode("5fppkhPnw5PCspRVGhZhOG", "RO")
        assert isinstance(response.json(), dict)

    def test_get_episode_invalid_id_error_message_is_Non_existing_id(self):
        response = get_episode("5fppkhPnw5PCspRVGhZhOG", "RO")
        expected_message = "Non existing id: 'spotify:episode:5fppkhPnw5PCspRVGhZhOG'"
        assert response.json().get('error', {}).get('message') == expected_message

    def test_get_episode_invalid_id_error_status_code_is_404(self):
        response = get_episode("5fppkhPnw5PCspRVGhZhOG", "RO")
        assert response.json().get('error', {}).get('status') == 404

    def test_get_episode_invalid_id_error_object_contains_message_key(self):
        response = get_episode("5fppkhPnw5PCspRVGhZhOG", "RO")
        assert 'message' in response.json().get('error', {})
