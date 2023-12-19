import time

from requests_folder.albums.check_saved_albums import check_saved_albums


class TestGetCheckSavedAlbums:


#CHECK SAVED ALBUMS valid ids

    def test_get_check_saved_albums_valid_id_status_code(self):
        response = check_saved_albums("7qNY7C7rkJwioya4lKLrJt")
        time.sleep(4)
        assert response.status_code == 200

    def test_get_check_saved_albums_valid_id_response_time(self):
        response = check_saved_albums("7qNY7C7rkJwioya4lKLrJt")
        assert response.elapsed.total_seconds() * 1000 < 200

    def test_get_check_saved_albums_valid_id_contains_true(self):
        response = check_saved_albums("7qNY7C7rkJwioya4lKLrJt")
        assert "true" in response.text

    def test_get_check_saved_albums_valid_id_http_method(self):
        response = check_saved_albums("7qNY7C7rkJwioya4lKLrJt")
        assert response.request.method == "GET"

    def test_get_check_saved_albums_valid_id_no_error(self):
        response = check_saved_albums("7qNY7C7rkJwioya4lKLrJt")
        assert "error" not in response.text


    def test_get_check_saved_albums_valid_id_body_length(self):
        response = check_saved_albums("7qNY7C7rkJwioya4lKLrJt")
        assert len(response.json()) == 1



#CHECK SAVED ALBUMS invalid ids

    def test_get_check_saved_albums_invalid_id_error_message(self):
        response = check_saved_albums("7qNY7C7rkJwioya4lKLrJtt")
        assert response.json()["error"]["message"] == "Bad request."

    def test_get_check_saved_albums_invalid_id_error_message_not_empty(self):
        response = check_saved_albums(["7qNY7C7rkJwioya4lKLrJtt"])
        assert response.json()["error"]["message"] != ""

    def test_get_check_saved_albums_invalid_id_error_message_type_string(self):
        response = check_saved_albums(["7qNY7C7rkJwioya4lKLrJtt"])
        assert isinstance(response.json()["error"]["message"], str)

    def test_get_check_saved_albums_invalid_id_error_message_contains_bad_request(self):
        response = check_saved_albums(["7qNY7C7rkJwioya4lKLrJtt"])
        assert "Bad request." in response.json()["error"]["message"]

    def test_get_check_saved_albums_invalid_id_error_status_code(self):
        response = check_saved_albums(["7qNY7C7rkJwioya4lKLrJtt"])
        assert response.json()["error"]["status"] == 400

    def test_get_check_saved_albums_invalid_id_response_body_not_empty(self):
        response = check_saved_albums(["7qNY7C7rkJwioya4lKLrJtt"])
        assert response.text != ""

    def test_get_check_saved_albums_invalid_id_response_content_type_json(self):
        response = check_saved_albums(["7qNY7C7rkJwioya4lKLrJtt"])
        assert response.headers["Content-Type"] == "application/json; charset=utf-8"

    def test_get_check_saved_albums_invalid_id_response_time_positive(self):
        response = check_saved_albums(["7qNY7C7rkJwioya4lKLrJtt"])
        assert response.elapsed.total_seconds() * 1000 > 0

    def test_get_check_saved_albums_invalid_id_response_status_code_400(self):
        response = check_saved_albums(["7qNY7C7rkJwioya4lKLrJtt"])
        assert response.status_code == 400



#CHECK SAVED ALBUMS inexistent id

    def test_get_check_saved_albums_inexistent_id_response_has_one_element(self):
        response = check_saved_albums("01u9MdrytYwPidRT0uoCXr")
        print(response)
        assert len(response.json()) == 1

    def test_get_check_saved_albums_inexistent_id_element_at_index_0_is_boolean(self):
        response = check_saved_albums("01u9MdrytYwPidRT0uoCXr")
        assert isinstance(response.json()[0], bool)

    def test_get_check_saved_albums_inexistent_id_element_at_index_0_is_false(self):
        response = check_saved_albums("01u9MdrytYwPidRT0uoCXr")
        assert response.json()[0] is False

    def test_get_check_saved_albums_inexistent_id_response_time_positive(self):
        response = check_saved_albums("01u9MdrytYwPidRT0uoCXr")
        assert response.elapsed.total_seconds() * 1000 > 0

    def test_get_check_saved_albums_inexistent_id_response_status_code_200(self):
        response = check_saved_albums("01u9MdrytYwPidRT0uoCXr")
        assert response.status_code == 200

    def test_get_check_saved_albums_inexistent_response_body_not_empty(self):
        response = check_saved_albums("01u9MdrytYwPidRT0uoCXr")
        assert response.text != ""
