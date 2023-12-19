
from requests_folder.episodes.put_save_episode import put_save_episode


class TestPutSaveEpisodes:


#Put Save Episode valid params

    def test_test_put_save_episode_valid_id_status_code_is_200(self):
        response = put_save_episode(["07TNGl4VKA4UfM4wFehiGD"])
        assert response.status_code == 200

    def test_test_put_save_episode_valid_id_response_time_is_less_than_200ms(self):
        response = put_save_episode(["07TNGl4VKA4UfM4wFehiGD"])
        assert response.elapsed.total_seconds() * 1000 < 200


    def test_test_put_save_episode_id_status_code_is_200(self):
        response = put_save_episode(["427jwbmn8JDzFbFKRxfrWC", "4P8dAqlFxm88Y9VVEZhriy", "3EWIFUOpaM9s7Pmei0r2C3", "0uXxESjlzZ5VfvdA2nXe1t", "3woccDLWFU1cvOcQ5Oflue", "4pVQq3r2eBDxMNsDSr3Tqu"])
        assert response.status_code == 200

    def test_test_put_save_episode_id_response_time_is_less_than_200ms(self):
        response = put_save_episode(["427jwbmn8JDzFbFKRxrWC", "4P8dAqlFxm88Y9VVEZhriy", "3EWIFUOpaM9s7Pmei0r2C3", "0uXxESjlzZ5VfvdA2nXe1t", "3woccDLWFU1cvOcQ5Oflue", "4pVQq3r2eBDxMNsDSr3Tqu"])
        assert response.elapsed.total_seconds() * 1000 < 200



#Put Save Episodes invalid id

    def test_test_put_save_episode_invalid_id_status_code_is_400(self):
        response = put_save_episode("(4pVQQ3r2eBDxMNsDSr3Tqwu")
        assert response.status_code == 400
    
    def test_test_put_save_episode_invalid_id_response_content_type_is_json(self):
        response = put_save_episode("(4pVQQ3r2eBDxMNsDSr3Tqwu")
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8'
    
    def test_test_put_save_episode_invalid_id_response_body_contains_error(self):
        response = put_save_episode("(4pVQQ3r2eBDxMNsDSr3Tqwu")
        assert 'error' in response.json()
    
    def test_put_save_episode_invalid_id_response_body_contains_message(self):
        response = put_save_episode("(4pVQQ3r2eBDxMNsDSr3Tqwu")
        assert 'message' in response.json()
    
    def test_put_save_episode_invalid_id_error_status_is_400(self):
        response = put_save_episode("(4pVQQ3r2eBDxMNsDSr3Tqwu")
        assert response.json().get('error', {}).get('status') == 400
    
    def test_put_save_episode_invalid_id_error_message_is_bad_request(self):
        response = put_save_episode("(4pVQQ3r2eBDxMNsDSr3Tqwu")
        assert response.json().get('error', {}).get('message') == 'Bad request.'
    
    def test_put_save_episode_invalid_id_response_body_is_not_empty(self):
        response = put_save_episode("(4pVQQ3r2eBDxMNsDSr3Tqwu")
        assert response.text != ""
    
    def test_put_save_episode_invalid_id_response_body_length_is_greater_than_0(self):
        response = put_save_episode("(4pVQQ3r2eBDxMNsDSr3Tqwu")
        assert len(response.text) > 0
    
    def test_put_save_episode_invalid_id_response_is_not_null(self):
        response = put_save_episode("(4pVQQ3r2eBDxMNsDSr3Tqwu")
        assert response.text is not None
    
    def test_put_save_episode_invalid_id_response_is_not_empty_object(self):
        response = put_save_episode("(4pVQQ3r2eBDxMNsDSr3Tqwu")
        assert response.json() != {}



#Put Save Episodes without body
    
    def test_put_save_episode_invalid_id_status_code_is_400(self):
        response = put_save_episode([""])
        assert response.status_code == 400
    
    def test_put_save_episode_invalid_id_response_content_type_is_json(self):
        response = put_save_episode([""])
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8'
    
    def test_put_save_episode_invalid_id_response_body_contains_error(self):
        response = put_save_episode([""])
        assert 'error' in response.json()
    
    def test_put_save_episodes_invalid_id_response_body_contains_message(self):
        response = put_save_episode([""])
        assert 'message' in response.json()
    
    def test_put_save_episodes_invalid_id_error_status_is_400(self):
        response = put_save_episode([""])
        assert response.json().get('error', {}).get('status') == 400
    
    def test_put_save_episodes_invalid_id_error_message_is_bad_request(self):
        response = put_save_episode([""])
        assert response.json().get('error', {}).get('message') == 'Bad request.'
    
    def test_put_save_episodes_invalid_id_response_body_is_not_empty(self):
        response = put_save_episode([""])
        assert response.text != ""
    
    def test_put_save_episodes_invalid_id_response_body_length_is_greater_than_0(self):
        response = put_save_episode([""])
        assert len(response.text) > 0
    
    def test_put_save_episodes_invalid_id_response_is_not_null(self):
        response = put_save_episode([""])
        assert response.text is not None
    
    def test_put_save_episodes_invalid_id_response_is_not_empty_object(self):
        response = put_save_episode([""])
        assert response.json() != {}
