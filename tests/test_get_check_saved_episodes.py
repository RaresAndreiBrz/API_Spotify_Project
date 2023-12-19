from requests_folder.episodes.get_check_saved_episodes import get_check_saved_episodes


class TestGetCheckSavedEpisodes:


#Get Check Saved Episodes valid ids

    def test_get_check_saved_episodes_status_code_is_200(self):
        response = get_check_saved_episodes(["260q7fUJAdR8S88JqG9slG", "4P8dAqlFxm88Y9VVEZhriy"])
        assert response.status_code == 200

    def test_get_check_saved_episodes_response_time_is_less_than_200ms(self):
        response = get_check_saved_episodes(["260q7fUJAdR8S88JqG9slG", "4P8dAqlFxm88Y9VVEZhriy"])
        assert response.responseTime < 200

        #Get Check Saved Episodes using album id instead of episode id
    def test_get_check_saved_episodes_using_album_id_status_code_is_200(self):
        response = get_check_saved_episodes(["7qNY7C7rkJwioya4lKLrJt"])
        assert response.status_code == 200
    
    def test_get_check_saved_episodes_using_album_id_response_time_is_less_than_200ms(self):
        response = get_check_saved_episodes(["7qNY7C7rkJwioya4lKLrJt"])
        assert response.responseTime < 200
    
    def test_get_check_saved_episodes_using_album_id_no_error_in_response(self):
        response = get_check_saved_episodes(["7qNY7C7rkJwioya4lKLrJt"])
        assert "error" not in response.text()
    
    def test_get_check_saved_episodes_using_album_id_has_header(self):
        response = get_check_saved_episodes(["7qNY7C7rkJwioya4lKLrJt"])
        assert response.headers is not None
    
    def test_get_check_saved_episodes_using_album_id_correct_header(self):
        response = get_check_saved_episodes(["7qNY7C7rkJwioya4lKLrJt"])
        assert "x-robots-tag" in response.headers
    

    
#Get Check Saved Episodes invalid id
    
    def test_get_check_saved_episodes_invalid_id_status_code_is_400(self):
        response = get_check_saved_episodes(["07TNGl4VKA4UfM4wFehiGDaa"])
        assert response.status_code == 400
    
    def test_get_check_saved_episodes_invalid_id_response_content_type_is_json(self):
        response = get_check_saved_episodes(["07TNGl4VKA4UfM4wFehiGDaa"])
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8'
    
    def test_get_check_saved_episodes_invalid_id_response_body_contains_error(self):
        response = get_check_saved_episodes(["07TNGl4VKA4UfM4wFehiGDaa"])
        assert "error" in response.text()
    
    def test_get_check_saved_episodes_invalid_id_response_body_contains_message(self):
        response = get_check_saved_episodes(["07TNGl4VKA4UfM4wFehiGDaa"])
        assert "message" in response.text()
    
    def test_get_check_saved_episodes_invalid_id_error_message_is_bad_request(self):
        response = get_check_saved_episodes(["07TNGl4VKA4UfM4wFehiGDaa"])
        assert response.json()["error"]["message"] == "Bad request."
    
    def test_get_check_saved_episodes_invalid_id_response_is_not_null(self):
        response = get_check_saved_episodes(["07TNGl4VKA4UfM4wFehiGDaa"])
        assert response.text() is not None
    
    def test_get_check_saved_episodes_invalid_id_response_is_not_an_empty_object(self):
        response = get_check_saved_episodes(["07TNGl4VKA4UfM4wFehiGDaa"])
        assert response.json() != {}
