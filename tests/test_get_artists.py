from requests_folder.artists.get_artist import get_artists


class TestGetArtists:
    

#GET ARTISTS valid id

    def test_get_artists_status_code_is_200(self):
        response = get_artists("0NZQTozgPtlt5iN3hmANhy")
        assert response.status_code == 200

    def test_get_artists_response_time_is_less_than_200ms(self):
        response = get_artists("0NZQTozgPtlt5iN3hmANhy")
        assert response.elapsed.total_seconds() * 1000 < 200

    def test_get_artists_no_error_in_response(self):
        response = get_artists("0NZQTozgPtlt5iN3hmANhy")
        assert "error" not in response.text

    def test_get_artists_header_exists(self):
        response = get_artists("0NZQTozgPtlt5iN3hmANhy")
        assert "header" in response.text  # Modify this line based on the actual header check

    def test_get_artists_http_method_is_get(self):
        response = get_artists("0NZQTozgPtlt5iN3hmANhy")
        assert response.request.method == "GET"

    def test_get_artists_check_name_of_requested_artist(self):
        response = get_artists("0NZQTozgPtlt5iN3hmANhy")
        data = response.json()
        assert data["name"] == "Queen Omega"

    def test_get_artists_check_type_of_requested_artist(self):
        response = get_artists("0NZQTozgPtlt5iN3hmANhy")
        data = response.json()
        assert data["type"] == "artist"

    def test_get_artists_check_id_of_requested_artist(self):
        response = get_artists("0NZQTozgPtlt5iN3hmANhy")
        data = response.json()
        assert data["id"] == "0NZQTozgPtlt5iN3hmANhy"



#GET ARTISTS invalid id

    def test_get_artists_invalid_id_response_is_an_object(self):
        response = get_artists("4RAbHb0oHO62If4S7h18LO")
        assert response.json() == {}
    
    def test_get_artists_invalid_id_response_contains_error_property(self):
        response = get_artists("4RAbHb0oHO62If4S7h18LO")
        assert "error" in response.json()
    
    def test_get_artists_invalid_id_error_object_has_status_property(self):
        response = get_artists("4RAbHb0oHO62If4S7h18LO")
        error = response.json().get("error", {})
        assert "status" in error
    
    def test_get_artists_invalid_id_error_object_has_message_property(self):
        response = get_artists("4RAbHb0oHO62If4S7h18LO")
        error = response.json().get("error", {})
        assert "message" in error
    
    def test_get_artists_invalid_id_error_status_is_404(self):
        response = get_artists("4RAbHb0oHO62If4S7h18LO")
        error = response.json().get("error", {})
        assert error.get("status", 0) == 404
    
    def test_get_artists_invalid_id_error_message_contains_non_existing_id(self):
        response = get_artists("4RAbHb0oHO62If4S7h18LO")
        error = response.json().get("error", {})
        assert "Non existing id" in error.get("message", "")
    
    def test_get_artists_invalid_id_error_message_contains_artist_id(self):
        response = get_artists("4RAbHb0oHO62If4S7h18LO")
        error = response.json().get("error", {})
        assert "'spotify:artist:4RAbHb0oHO62If4S7h18LO'" in error.get("message", "")
    
    def test_get_artists_invalid_id_error_message_is_not_empty(self):
        response = get_artists("4RAbHb0oHO62If4S7h18LO")
        error = response.json().get("error", {})
        assert error.get("message", "") != ""
    
    def test_get_artists_invalid_id_error_message_is_a_string(self):
        response = get_artists("4RAbHb0oHO62If4S7h18LO")
        error = response.json().get("error", {})
        assert isinstance(error.get("message", ""), str)
    
