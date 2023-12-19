from requests_folder.albums.put_save_albums import put_save_albums


class TestPutSaveAlbums:


#SAVE ALBUMS valid ids
    
    def test_put_save_albums_status_code(self):
        response = put_save_albums({"ids": ["7qNY7C7rkJwioya4lKLrJt", "01u9MdrytYwPidRT0uoCXR"]})
        assert response.status_code == 200, "Status code is not 200"

    def test_put_save_albums_response_time(self):
        response = put_save_albums({"ids": ["7qNY7C7rkJwioya4lKLrJt", "01u9MdrytYwPidRT0uoCXR"]})
        assert response.elapsed.total_seconds() < 3, "Response time is not below 3 seconds"

    def test_put_save_albums_http_method(self):
        response = put_save_albums({"ids": ["7qNY7C7rkJwioya4lKLrJt", "01u9MdrytYwPidRT0uoCXR"]})
        assert response.request.method == "PUT", "HTTP method is not PUT"

    def test_put_save_albums_empty_body(self):
        response = put_save_albums({"ids": ["7qNY7C7rkJwioya4lKLrJt", "01u9MdrytYwPidRT0uoCXR"]})
        assert len(response.text) == 0, "Body is not empty as specified"

    def test_put_save_albums_no_error_in_response(self):
        response = put_save_albums({"ids": ["7qNY7C7rkJwioya4lKLrJt", "01u9MdrytYwPidRT0uoCXR"]})
        assert "error" not in response.text, "'error' is present in the response"



#SAVE ALBUMS invalid ids

    def test_put_save_albums_invalid_id_error_message(self):
        response = put_save_albums({"ids": ["01u9MdrytYwPidRT0uoCXRRR"]})
        assert response.json()["error"]["message"] == "Bad request.", "Error message is not 'Bad request.'"

    def test_put_save_albums_invalid_id_not_empty_error_message(self):
        response = put_save_albums({"ids": ["01u9MdrytYwPidRT0uoCXRRR"]})
        assert response.json()["error"]["message"] != "", "Error message is empty"

    def test_put_save_albums_invalid_id_error_message_type(self):
        response = put_save_albums({"ids": ["01u9MdrytYwPidRT0uoCXRRR"]})
        assert isinstance(response.json()["error"]["message"], str), "Error message is not of string type"

    def test_put_save_albums_invalid_id_error_message_contains_bad_request(self):
        response = put_save_albums({"ids": ["01u9MdrytYwPidRT0uoCXRRR"]})
        assert "Bad request." in response.json()["error"]["message"], "Error message does not contain 'Bad request.'"

    def test_put_save_albums_invalid_id_error_status(self):
        response = put_save_albums({"ids": ["01u9MdrytYwPidRT0uoCXRRR"]})
        assert response.json()["error"]["status"] == 400, "Error status is not 400"

    def test_put_save_albums_invalid_id_response_not_empty(self):
        response = put_save_albums({"ids": ["01u9MdrytYwPidRT0uoCXRRR"]})
        assert response.text != "", "Response body is empty"

    def test_put_save_albums_invalid_id_response_content_type(self):
        response = put_save_albums({"ids": ["01u9MdrytYwPidRT0uoCXRRR"]})
        assert response.headers["Content-Type"] == "application/json; charset=utf-8", "Response content type is not JSON"

    def test_put_save_albums_invalid_id_response_time_positive(self):
        response = put_save_albums({"ids": ["01u9MdrytYwPidRT0uoCXRRR"]})
        assert response.elapsed.total_seconds() > 0, "Response time is not a positive number"

    def test_put_save_albums_invalid_id_status_code(self):
        response = put_save_albums({"ids": ["01u9MdrytYwPidRT0uoCXRRR"]})
        assert response.status_code == 400, "Status code is not 400"
