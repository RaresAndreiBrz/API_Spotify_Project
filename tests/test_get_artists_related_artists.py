from requests_folder.artists.get_artists_related_artist import get_artist_related_artists


class TestGetArtistsRelatedArtist:


#Artists Related Artist valid id

    def test_get_artist_related_artists_valid_id_response_status_code_is_200(self):
        response = get_artist_related_artists("4RAbHb0oHO62If4S7h18L0")
        assert response.status_code == 200

    def test_get_artist_related_artists_valid_id_response_time_is_less_than_200ms(self):
        response = get_artist_related_artists("4RAbHb0oHO62If4S7h18L0")
        assert response.elapsed.total_seconds() < 0.2

    def test_get_artist_related_artists_valid_id_no_error_in_response(self):
        response = get_artist_related_artists("4RAbHb0oHO62If4S7h18L0")
        assert 'error' not in response.text.lower()

    def test_get_artist_related_artists_valid_id_http_method_is_get(self):
        response = get_artist_related_artists("4RAbHb0oHO62If4S7h18L0")
        assert response.request.method == 'GET'

    def test_get_artist_related_artists_valid_id_body_contains_related_artist_id(self):
        response = get_artist_related_artists("4RAbHb0oHO62If4S7h18L0")
        assert "0MBEd6qd0GmDdDW8Pyftuv" in response.text

    def test_get_artist_related_artists_valid_id_received_artist_type_as_requested(self):
        response = get_artist_related_artists("4RAbHb0oHO62If4S7h18L0")
        data = response.json()
        assert data['artists'][0]['type'] == "artist"

    def test_get_artist_related_artists_valid_id_response_contains_specified_parameters(self):
        response = get_artist_related_artists("4RAbHb0oHO62If4S7h18L0")
        assert "followers" in response.text
        assert "genres" in response.text
        assert "external_urls" in response.text
        assert "href" in response.text
        assert "id" in response.text
        assert "images" in response.text
        assert "name" in response.text
        assert "popularity" in response.text
        assert "type" in response.text
        assert "uri" in response.text
