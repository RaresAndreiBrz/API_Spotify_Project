from requests_folder.episodes.del_saved_episode import del_saved_episode


class TestDelSavedEpisodes:


#Del Saved Episodes valid id

    def test_del_saved_episode_status_code_is_200(self):
        response = del_saved_episode(["4P8dAqlFxm88Y9VVEZhriy", "0Pc7cY4izGWS1RmaTfN93B"])
        assert response["status_code"] == 200

    def test_del_saved_episode_response_time_is_less_than_200ms(self):
        response = del_saved_episode(["4P8dAqlFxm88Y9VVEZhriy", "0Pc7cY4izGWS1RmaTfN93B"])
        assert response.elapsed.total_seconds() * 1000 < 200



#Del Saved Episodes invalid ids
    
    def test_del_saved_episode_invalid_id_status_code_is_400(self):
        response = del_saved_episode(["ssssssssssssss"])
        assert response.status_code == 400
    
    def test_del_saved_episode_invalid_id_content_type_is_json(self):
        response = del_saved_episode(["ssssssssssssss"])
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8'
    
    def test_del_saved_episode_invalid_id_body_contains_error(self):
        response = del_saved_episode(["ssssssssssssss"])
        assert 'error' in response.text()
    
    def test_del_saved_episode_invalid_id_body_contains_message(self):
        response = del_saved_episode(["ssssssssssssss"])
        assert 'message' in response.text()
    
    def test_del_saved_episode_invalid_id_error_message_is_bad_request(self):
        response = del_saved_episode(["ssssssssssssss"])
        data_json = response.json()
        assert data_json['error']['message'] == 'Bad request'
    
    def test_del_saved_episode_invalid_id_response_is_not_null(self):
        response = del_saved_episode(["ssssssssssssss"])
        assert response.text() is not None
    
    def test_del_saved_episode_invalid_id_response_is_not_empty_object(self):
        response = del_saved_episode(["ssssssssssssss"])
        assert response.json() != {}
    
    
    
#Del Saved Episodes duplicated id
    
    def test_del_saved_episode_duplicated_ids_status_code_is_200(self):
        response = del_saved_episode(["6fppkhPnw5PCspRVGhZhOG", "6fppkhPnw5PCspRVGhZhOG"])
        assert response.status_code == 200
    
    def test_del_saved_episode_duplicated_ids_body_exists(self):
        response = del_saved_episode(["6fppkhPnw5PCspRVGhZhOG", "6fppkhPnw5PCspRVGhZhOG"])
        assert response.text() != ""
    
    def test_del_saved_episode_duplicated_ids_body_is_not_null(self):
        response = del_saved_episode(["6fppkhPnw5PCspRVGhZhOG", "6fppkhPnw5PCspRVGhZhOG"])
        assert response.text() is not None
    
    def test_del_saved_episode_duplicated_ids_body_is_not_undefined(self):
        response = del_saved_episode(["6fppkhPnw5PCspRVGhZhOG", "6fppkhPnw5PCspRVGhZhOG"])
        assert response.text() is not None
    
    def test_del_saved_episode_duplicated_ids_body_is_empty(self):
        response = del_saved_episode(["6fppkhPnw5PCspRVGhZhOG", "6fppkhPnw5PCspRVGhZhOG"])
        assert response.text() == ""
