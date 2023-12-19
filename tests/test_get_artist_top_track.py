from requests_folder.artists.get_artist_top_tracks import get_artist_top_track


class TestGetArtistTopTrack:


#GET ARTIST TOP TRACK valid id and country

    def test_get_artist_top_track_valid_id_response_status_code_is_200(self):
        response = get_artist_top_track("2w9zwq3AktTeYYMuhMjju8", "RO")
        assert response.status_code == 200
    
    def test_get_artist_top_track_valid_id_response_time_is_less_than_200ms(self):
        response = get_artist_top_track("2w9zwq3AktTeYYMuhMjju8", "RO")
        assert response.elapsed.total_seconds() * 1000 < 200
    
    def test_get_artist_top_track_valid_id_response_contains_expected_parameters(self):
        response = get_artist_top_track("2w9zwq3AktTeYYMuhMjju8", "RO")
        data = response.json()
    
        expected_parameters = [
            "tracks", "album", "artists", "disc_number", "duration_ms",
            "external_ids", "external_urls", "href", "id", "is_playable",
            "name", "popularity", "preview_url", "track_number", "is_local", "uri"
        ]
    
        for parameter in expected_parameters:
            assert parameter in data
    
    def test_get_artist_top_track_valid_id_response_does_not_contain_unexpected_parameters(self):
        response = get_artist_top_track("2w9zwq3AktTeYYMuhMjju8", "RO")
    
        unexpected_parameters = ["restrictions", "linked_from"]
    
        for parameter in unexpected_parameters:
            assert parameter not in response.text
    
    def test_get_artist_top_track_valid_id_response_does_not_contain_error(self):
        response = get_artist_top_track("2w9zwq3AktTeYYMuhMjju8", "RO")
        assert "error" not in response.text
    
    def test_get_artist_top_track_valid_id_request_method_is_get(self):
        response = get_artist_top_track("2w9zwq3AktTeYYMuhMjju8", "RO")
        assert response.request.method == "GET"
    
    def test_get_artist_top_track_valid_id_response_length_of_tracks_is_10(self):
        response = get_artist_top_track("2w9zwq3AktTeYYMuhMjju8", "RO")
        data = response.json()
        assert len(data.get("tracks", [])) == 10
    


#GET ARTIST TOP TRACK valid id, invalid country
    
    def test_get_artist_top_track_invalid_country_response_status_code_is_400(self):
        response = get_artist_top_track("4RAbHb0oHO62If4S7h18L0", "ZZ")
        assert response.status_code == 400
    
    def test_get_artist_top_track_invalid_country_response_is_json(self):
        response = get_artist_top_track("4RAbHb0oHO62If4S7h18L0", "ZZ")
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8'
    
    def test_get_artist_top_track_invalid_country_response_is_an_object(self):
        response = get_artist_top_track("4RabHb0oHO62If4S7h18L0", "ZZ")
        assert isinstance(response.json(), dict)
    
    def test_get_artist_top_track_invalid_country_error_object_exists(self):
        response = get_artist_top_track("4RAbHb0oHO62If4S7h18L0", "ZZ")
        assert 'error' in response.json()
    
    def test_get_artist_top_track_invalid_country_error_status_is_400(self):
        response = get_artist_top_track("4RAbHb0oHO62If4S7h18L0", "ZZ")
        assert response.json().get('error', {}).get('status') == 400
    
    def test_get_artist_top_track_invalid_country_error_message_is_invalid_market_code(self):
        response = get_artist_top_track("4RAbHb0oHO62If4S7h18L0", "ZZ")
        assert response.json().get('error', {}).get('message') == 'Invalid market code'
    
    def test_get_artist_top_track_invalid_country_response_time_is_less_than_500ms(self):
        response = get_artist_top_track("4RAbHb0oHO62If4S7h18L0", "ZZ")
        assert response.elapsed.total_seconds() * 1000 < 500


#GET ARTIST TOP TRACK invalid id , valid country

    def test_get_artist_top_track_invalid_id_response_status_code_is_404(self):
        response = get_artist_top_track("4RabHb0oHO62If4S7h18L0", "RO")
        assert response.status_code == 404

    def test_get_artist_top_track_invalid_id_response_is_json(self):
        response = get_artist_top_track("4RabHb0oHO62If4S7h18L0", "RO")
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8'

    def test_get_artist_top_track_invalid_id_response_is_an_object(self):
        response = get_artist_top_track("4RabHb0oHO62If4S7h18L0", "RO")
        assert isinstance(response.json(), dict)

    def test_get_artist_top_track_invalid_id_error_object_exists(self):
        response = get_artist_top_track("4RabHb0oHO62If4S7h18L0", "RO")
        assert 'error' in response.json()

    def test_get_artist_top_track_invalid_id_error_status_is_404(self):
        response = get_artist_top_track("4RabHb0oHO62If4S7h18L0", "RO")
        assert response.json().get('error', {}).get('status') == 404

    def test_get_artist_top_track_invalid_id_error_message_is_not_found(self):
        response = get_artist_top_track("4RabHb0oHO62If4S7h18L0", "RO")
        assert response.json().get('error', {}).get('message') == 'Not found.'
