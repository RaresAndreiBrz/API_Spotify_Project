from requests_folder.albums.get_album_tracks import get_albums_tracks, get_albums_tracks_withParams_Limit, \
    get_albums_tracks_withParams_Limit_Offset, get_albums_tracks_withParams_Limit_Offset_Market


class TestGetAlbumsTracks:


#ALBUMS TRACKS valid album

    def test_get_albums_tracks_status_code_is_200(self):
        response = get_albums_tracks("2DQhAbIgZG4QRy4mmQsFE0")
        assert response.status_code == 200

    def test_get_albums_tracks_response_time_is_less_than_200ms(self):
        response = get_albums_tracks("2DQhAbIgZG4QRy4mmQsFE0")
        assert response.responseTime < 3000

    def test_get_albums_tracks_album_tracks_contains_artist_id_4RAbHb0oHO62If4S7h18L0(self):
        data = get_albums_tracks("2DQhAbIgZG4QRy4mmQsFE0").json()
        assert data["items"][0]["artists"][0]["id"] == "4RAbHb0oHO62If4S7h18L0"

    def test_get_albums_tracks_album_tracks_contains_artist_named_Magic_Touch(self):
        data = get_albums_tracks("2DQhAbIgZG4QRy4mmQsFE0").json()
        assert data["items"][0]["artists"][1]["name"] == "Magic Touch"

    def test_get_albums_tracks_limit_parameter_as_requested(self):
        data = get_albums_tracks("2DQhAbIgZG4QRy4mmQsFE0").json()
        assert data["limit"] == 1



#ALBUMS TRACKS in range limit value

    def test_get_albums_tracks_inRangeLimit_status_code_is_200(self):
        response = get_albums_tracks_withParams_Limit("2DQhAbIgZG4QRy4mmQsFE0", "4")
        assert response.status_code == 200

    def test_get_albums_tracks_inRangeLimit_response_time_is_less_than_2000ms(self):
        response = get_albums_tracks_withParams_Limit("2DQhAbIgZG4QRy4mmQsFE0", "4")
        assert response.responseTime < 2000

    def test_get_albums_tracks_inRangeLimit_response_with_limit_parameter_as_requested(self):
        data = get_albums_tracks_withParams_Limit("2DQhAbIgZG4QRy4mmQsFE0", "4").json()
        assert data["limit"] == 4

    def test_get_albums_tracks_inRangeLimit_response_contains_part_of_parameters_specified_in_API(self):
        response_text = get_albums_tracks_withParams_Limit("2DQhAbIgZG4QRy4mmQsFE0", "4").text()
        assert "href" in response_text
        assert "next" in response_text
        assert "offset" in response_text
        assert "previous" in response_text
        assert "items" in response_text



#ALBUMS TRACKS valid limit / offset

    def test_get_albums_tracks_inRangeLimit_offsetValid_status_code_is_200(self):
        response = get_albums_tracks_withParams_Limit_Offset("1t3Z2hSfT1fm5iHHWC65xd", "1", "3")
        assert response.status_code == 200

    def test_get_albums_tracks_inRangeLimit_offsetValid_response_time_is_less_than_200ms(self):
        response = get_albums_tracks_withParams_Limit_Offset("1t3Z2hSfT1fm5iHHWC65xd", "1", "3")
        assert response.responseTime < 200

    def test_get_albums_tracks_inRangeLimit_offsetValid_response_with_limit_parameter_as_requested(self):
        data = get_albums_tracks_withParams_Limit_Offset("1t3Z2hSfT1fm5iHHWC65xd", "1", "3").json()
        assert data["limit"] == 1

    def test_get_albums_tracks_inRangeLimit_offsetValid_response_with_offset_parameter_as_requested(self):
        data = get_albums_tracks_withParams_Limit_Offset("1t3Z2hSfT1fm5iHHWC65xd", "1", "3").json()
        assert data["offset"] == 3



#ALBUMS TRACKS valid limit / offset / market

    def test_get_albums_tracks_validLimit_validOffset_validMarket_status_code_is_200(self):
        response = get_albums_tracks_withParams_Limit_Offset_Market("2DQhAbIgZG4QRy4mmQsFE0", "RO", "2", "2")
        assert response.status_code == 200

    def test_get_albums_tracks_validLimit_validOffset_validMarket_response_time_is_less_than_200ms(self):
        response = get_albums_tracks_withParams_Limit_Offset_Market("2DQhAbIgZG4QRy4mmQsFE0", "RO", "2", "2")
        assert response.responseTime < 200

    def test_get_albums_tracks_validLimit_validOffset_validMarket_response_with_limit_parameter_as_requested(self):
        data = get_albums_tracks_withParams_Limit_Offset_Market("2DQhAbIgZG4QRy4mmQsFE0", "RO", "2", "2").json()
        assert data["limit"] == 2

    def test_get_albums_tracks_validLimit_validOffset_validMarket_response_with_offset_parameter_as_requested(self):
        data = get_albums_tracks_withParams_Limit_Offset_Market("2DQhAbIgZG4QRy4mmQsFE0", "RO", "2", "2").json()
        assert data["offset"] == 2

    def test_get_albums_tracks_validLimit_validOffset_validMarket_response_contains_part_of_parameters_specified_in_API(self):
        response_text = get_albums_tracks_withParams_Limit_Offset_Market("2DQhAbIgZG4QRy4mmQsFE0", "RO", "2", "2").text()
        assert "RO" in response_text

    def test_get_albums_tracks_validLimit_validOffset_validMarket_body_contains_album_id_2DQhAbIgZG4QRy4mmQsFE0(self):
        response_text = get_albums_tracks_withParams_Limit_Offset_Market("2DQhAbIgZG4QRy4mmQsFE0", "RO", "2", "2").text()
        assert "2DQhAbIgZG4QRy4mmQsFE0" in response_text



#ALBUMS TRACKS invalid limit + valid offset / market

    def test_get_albums_tracks_withParams_invalidLimit_validOffset_validMarket_status_code_is_400(self):
        response = get_albums_tracks_withParams_Limit_Offset_Market("2DQhAbIgZG4QRy4mmQsFE0", "RO", "-2", "2")
        assert response.status_code == 400

    def test_get_albums_tracks_withParams_invalidLimit_validOffset_validMarket_response_time_is_less_than_200ms(self):
        response = get_albums_tracks_withParams_Limit_Offset_Market("2DQhAbIgZG4QRy4mmQsFE0", "RO", "-2", "2")
        assert response.responseTime < 200

    def test_get_albums_tracks_withParams_invalidLimit_validOffset_validMarket_response_status_code_is_400(self):
        response = get_albums_tracks_withParams_Limit_Offset_Market("2DQhAbIgZG4QRy4mmQsFE0", "RO", "-2", "2")
        assert response.status_code == 400

    def test_get_albums_tracks_withParams_invalidLimit_validOffset_validMarket_response_contains_an_error_object(self):
        response = get_albums_tracks_withParams_Limit_Offset_Market("2DQhAbIgZG4QRy4mmQsFE0", "RO", "-2", "2")
        assert response.json().error

    def test_get_albums_tracks_withParams_invalidLimit_validOffset_validMarket_error_message_is_Bad_limit_limit_must_be_larger_than_0(self):
        response = get_albums_tracks_withParams_Limit_Offset_Market("2DQhAbIgZG4QRy4mmQsFE0", "RO", "-2", "2")
        assert response.json().error.message == "Bad limit, limit must be larger than 0"

    def test_get_albums_tracks_withParams_invalidLimit_validOffset_validMarket_error_message_is_not_empty(self):
        response = get_albums_tracks_withParams_Limit_Offset_Market("2DQhAbIgZG4QRy4mmQsFE0", "RO", "-2", "2")
        assert response.json().error.message

    def test_get_albums_tracks_withParams_invalidLimit_validOffset_validMarket_error_message_is_a_string(self):
        response = get_albums_tracks_withParams_Limit_Offset_Market("2DQhAbIgZG4QRy4mmQsFE0", "RO", "-2", "2")
        assert isinstance(response.json().error.message, str)

    def test_get_albums_tracks_withParams_invalidLimit_validOffset_validMarket_error_message_contains_Bad_limit_limit_must_be_larger_than_0(self):
        response = get_albums_tracks_withParams_Limit_Offset_Market("2DQhAbIgZG4QRy4mmQsFE0", "RO", "-2", "2")
        assert "Bad limit, limit must be larger than 0" in response.json().error.message

    def test_get_albums_tracks_withParams_invalidLimit_validOffset_validMarket_response_content_type_is_JSON(self):
        response = get_albums_tracks_withParams_Limit_Offset_Market("2DQhAbIgZG4QRy4mmQsFE0", "RO", "-2", "2")
        assert response.headers["Content-Type"] == "application/json; charset=utf-8"



#ALBUMS TRACKS invalid limit

    def test_get_albums_tracks_withParams_Limit_status_code_is_400(self):
        response = get_albums_tracks_withParams_Limit("2zIFsf5FefGkMPWS9fqg42", "0")
        assert response.status_code == 400

    def test_get_albums_tracks_withParams_Limit_response_time_is_less_than_2000ms(self):
        response = get_albums_tracks_withParams_Limit("2zIFsf5FefGkMPWS9fqg42", "0")
        assert response.responseTime < 2000

    def test_get_albums_tracks_withParams_Limit_error_message_is_Bad_limit_limit_must_be_larger_than_0(self):
        response = get_albums_tracks_withParams_Limit("2zIFsf5FefGkMPWS9fqg42", "0")
        assert response.json().error.message == "Bad limit, limit must be larger than 0"

    def test_get_albums_tracks_withParams_Limit_error_message_is_not_empty(self):
        response = get_albums_tracks_withParams_Limit("2zIFsf5FefGkMPWS9fqg42", "0")
        assert response.json().error.message

    def test_get_albums_tracks_withParams_Limit_error_message_is_of_string_type(self):
        response = get_albums_tracks_withParams_Limit("2zIFsf5FefGkMPWS9fqg42", "0")
        assert isinstance(response.json().error.message, str)

    def test_get_albums_tracks_withParams_Limit_error_message_contains_Bad_limit_limit_must_be_larger_than_0(self):
        response = get_albums_tracks_withParams_Limit("2zIFsf5FefGkMPWS9fqg42", "0")
        assert "Bad limit, limit must be larger than 0" in response.json().error.message

    def test_get_albums_tracks_withParams_Limit_response_content_type_is_JSON(self):
        response = get_albums_tracks_withParams_Limit("2zIFsf5FefGkMPWS9fqg42", "0")
        assert response.headers["Content-Type"] == "application/json; charset=utf-8"

    def test_get_albums_tracks_withParams_invLimit_status_code_is_400(self):
        response = get_albums_tracks_withParams_Limit("2zIFsf5FefGkMPWS9fqg42", "1563")
        assert response.status_code == 400

    def test_get_albums_tracks_withParams_invLimit_response_time_is_less_than_2000ms(self):
        response = get_albums_tracks_withParams_Limit("2zIFsf5FefGkMPWS9fqg42", "1563")
        assert response.responseTime < 2000

    def test_get_albums_tracks_withParams_invLimit_error_message_is_Invalid_limit_cannot_be_greater_than_50(self):
        response = get_albums_tracks_withParams_Limit("2zIFsf5FefGkMPWS9fqg42", "1563")
        assert response.json().error.message == "Invalid limit, cannot be greater than 50"

    def test_get_albums_tracks_withParams_invLimit_error_status_is_400(self):
        response = get_albums_tracks_withParams_Limit("2zIFsf5FefGkMPWS9fqg42", "1563")
        assert response.json().error.status == 400

    def test_get_albums_tracks_withParams_invLimit_error_message_is_not_empty(self):
        response = get_albums_tracks_withParams_Limit("2zIFsf5FefGkMPWS9fqg42", "1563")
        assert response.json().error.message

    def test_get_albums_tracks_withParams_invLimit_error_message_is_of_string_type(self):
        response = get_albums_tracks_withParams_Limit("2zIFsf5FefGkMPWS9fqg42", "1563")
        assert isinstance(response.json().error.message, str)

    def test_get_albums_tracks_withParams_invLimit_error_message_contains_Invalid_limit_cannot_be_greater_than_50(self):
        response = get_albums_tracks_withParams_Limit("2zIFsf5FefGkMPWS9fqg42", "1563")
        assert "Invalid limit, cannot be greater than 50" in response.json().error.message

    def test_get_albums_tracks_withParams_invLimit_response_time_is_less_than_500ms(self):
        response = get_albums_tracks_withParams_Limit("2zIFsf5FefGkMPWS9fqg42", "1563")
        assert response.responseTime < 500

    def test_get_albums_tracks_withParams_invLimit_response_content_type_is_JSON(self):
        response = get_albums_tracks_withParams_Limit("2zIFsf5FefGkMPWS9fqg42", "1563")
        assert response.headers["Content-Type"] == "application/json; charset=utf-8"
