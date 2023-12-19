from requests_folder.albums.get_saved_albums import get_saved_albums, get_saved_albums_with_market


class TestGetSavedAlbums:


#SAVED ALBUMS valid params
    def test_get_saved_albums_status_code_is_200(self):
        response = get_saved_albums("2", "0")
        assert response.status_code == 200

    def test_get_saved_albums_response_time_is_less_than_3000ms(self):
        response = get_saved_albums("2", "0")
        assert response.responseTime < 3000

    def test_get_saved_albums_body_contains_album_id_7qNY7C7rkJwioya4lKLrJt(self):
        response = get_saved_albums("2", "0")
        assert "7qNY7C7rkJwioya4lKLrJt" in response.text()

    def test_get_saved_albums_response_with_limit_parameter_as_requested(self):
        response = get_saved_albums("2", "0")
        data = response.json()
        assert data.limit == 2

    def test_get_saved_albums_response_with_offset_parameter_as_requested(self):
        response = get_saved_albums("2", "0")
        data = response.json()
        assert data.offset == 0

    def test_get_saved_albums_attribute_album_type_in_body_of_requested_album(self):
        response = get_saved_albums("2", "0")
        data = response.json()
        assert data.items[0].album.album_type == "album"



#SAVED ALBUMS invalid offset

    def test_get_saved_albums_invalidOffset_error_message_is_Bad_request(self):
        response = get_saved_albums("1", "J")
        assert response.json().error.message == "Bad request."

    def test_get_saved_albums_invalidOffset_error_message_is_not_empty(self):
        response = get_saved_albums("1", "J")
        assert response.json().error.message

    def test_get_saved_albums_invalidOffset_error_message_is_of_string_type(self):
        response = get_saved_albums("1", "J")
        assert isinstance(response.json().error.message, str)

    def test_get_saved_albums_invalidOffset_error_message_contains_Bad_request(self):
        response = get_saved_albums("1", "J")
        assert "Bad request." in response.json().error.message

    def test_get_saved_albums_invalidOffset_error_status_is_400(self):
        response = get_saved_albums("1", "J")
        assert response.json().error.status == 400

    def test_get_saved_albums_invalidOffset_response_body_is_not_empty(self):
        response = get_saved_albums("1", "J")
        assert response.text()

    def test_get_saved_albums_invalidOffset_response_content_type_is_JSON(self):
        response = get_saved_albums("1", "J")
        assert response.headers["Content-Type"] == "application/json; charset=utf-8"

    def test_get_saved_albums_invalidOffset_response_time_is_a_positive_number(self):
        response = get_saved_albums("1", "J")
        assert response.responseTime > 0

    def test_get_saved_albums_invalidOffset_response_status_code_is_400(self):
        response = get_saved_albums("1", "J")
        assert response.status_code == 400



#SAVED ALBUMS invalid offset and valid market / limit

    def test_get_saved_albums_with_invalid_offset_error_message_is_Bad_request(self):
        response = get_saved_albums_with_market("1", "-2", "RO")
        assert response.json().error.message == "Bad request."

    def test_get_saved_albums_with_invalid_offset_error_message_is_not_empty(self):
        response = get_saved_albums_with_market("1", "-2", "RO")
        assert response.json().error.message

    def test_get_saved_albums_with_invalid_offset_error_message_is_of_string_type(self):
        response = get_saved_albums_with_market("1", "-2", "RO")
        assert isinstance(response.json().error.message, str)

    def test_get_saved_albums_with_invalid_offset_error_message_contains_Bad_request(self):
        response = get_saved_albums_with_market("1", "-2", "RO")
        assert "Bad request." in response.json().error.message

    def test_get_saved_albums_with_invalid_offset_error_status_is_400(self):
        response = get_saved_albums_with_market("1", "-2", "RO")
        assert response.json().error.status == 400

    def test_get_saved_albums_with_invalid_offset_response_body_is_not_empty(self):
        response = get_saved_albums_with_market("1", "-2", "RO")
        assert response.text()

    def test_get_saved_albums_with_invalid_offset_response_content_type_is_JSON(self):
        response = get_saved_albums_with_market("1", "-2", "RO")
        assert response.headers["Content-Type"] == "application/json; charset=utf-8"

    def test_get_saved_albums_with_invalid_offset_response_time_is_a_positive_number(self):
        response = get_saved_albums_with_market("1", "-2", "RO")
        assert response.responseTime > 0

    def test_get_saved_albums_with_invalid_offset_response_status_code_is_400(self):
        response = get_saved_albums_with_market("1", "-2", "RO")
        assert response.status_code == 400



#SAVED ALBUMS invalid limit and valid market / offset

    def test_error_message_is_bad_request(self):
        response = get_saved_albums_with_market("ASC", "2", "RO")
        assert response.json().error.message == "Bad request."

    def test_error_message_is_not_empty(self):
        response = get_saved_albums_with_market("ASC", "2", "RO")
        assert response.json().error.message

    def test_error_message_is_of_string_type(self):
        response = get_saved_albums_with_market("ASC", "2", "RO")
        assert isinstance(response.json().error.message, str)

    def test_error_message_contains_bad_request(self):
        response = get_saved_albums_with_market("ASC", "2", "RO")
        assert "Bad request." in response.json().error.message

    def test_error_status_is_400(self):
        response = get_saved_albums_with_market("ASC", "2", "RO")
        assert response.json().error.status == 400

    def test_response_body_is_not_empty(self):
        response = get_saved_albums_with_market("ASC", "2", "RO")
        assert response.text()

    def test_response_content_type_is_JSON(self):
        response = get_saved_albums_with_market("ASC", "2", "RO")
        assert response.headers["Content-Type"] == "application/json; charset=utf-8"

    def test_response_time_is_a_positive_number(self):
        response = get_saved_albums_with_market("ASC", "2", "RO")
        assert response.responseTime > 0

    def test_response_status_code_is_400(self):
        response = get_saved_albums_with_market("ASC", "2", "RO")
        assert response.status_code == 400
