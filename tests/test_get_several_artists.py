from requests_folder.artists.get_several_artists import get_several_artists


class TestGetSeveralArtists:


#GET SEVERAL ARTISTS valid ids

    def test_get_several_artists_status_code_is_200(self):
        response = get_several_artists(["0NZQTozgPtlt5iN3hmANhy", "1u7VoUsRoA8TwydQXPLseH"])
        assert response.status_code == 200

    def test_get_several_artists_response_time_is_less_than_200ms(self):
        response = get_several_artists(["0NZQTozgPtlt5iN3hmANhy", "1u7VoUsRoA8TwydQXPLseH"])
        assert response.elapsed.total_seconds() * 1000 < 200

    def test_get_several_artists_check_types_of_artists_requested(self):
        data = get_several_artists(["0NZQTozgPtlt5iN3hmANhy", "1u7VoUsRoA8TwydQXPLseH"]).json()
        assert data["artists"][0]["type"] == "artist"
        assert data["artists"][1]["type"] == "artist"

    def test_get_several_artists_check_names_of_artists_requested(self):
        data = get_several_artists(["0NZQTozgPtlt5iN3hmANhy", "1u7VoUsRoA8TwydQXPLseH"]).json()
        assert "Queen Omega" in data["artists"][0]["name"]
        assert "Uzzi" in data["artists"][1]["name"]

    def test_get_several_artists_check_ids_of_artists_requested(self):
        data = get_several_artists(["0NZQTozgPtlt5iN3hmANhy", "1u7VoUsRoA8TwydQXPLseH"]).json()
        assert data["artists"][0]["id"] == "0NZQTozgPtlt5iN3hmANhy"
        assert data["artists"][1]["id"] == "1u7VoUsRoA8TwydQXPLseH"

    def test_get_several_artists_empty_body_as_specified(self):
        data = get_several_artists(["0NZQTozgPtlt5iN3hmANhy", "1u7VoUsRoA8TwydQXPLseH"]).json()
        assert len(data.get("artists", [])) == 2

    def test_get_several_artists_check_if_header_is_in_response(self):
        response = get_several_artists(["0NZQTozgPtlt5iN3hmANhy", "1u7VoUsRoA8TwydQXPLseH"])
        assert "header" in response.headers



#GET SEVERAL ARTISTS invalid ids

    def test_get_several_artists_invalid_ids_response_is_an_object(self):
        response = get_several_artists(["572uUqNnEoaTeR0PuZHtyLLLk", "DDDDDDDDDDDDDDDDDDDS"])
        assert response.json() == {}

    def test_get_several_artists_invalid_ids_response_contains_artists_property(self):
        response = get_several_artists(["572uUqNnEoaTeR0PuZHtyLLLk", "DDDDDDDDDDDDDDDDDDDS"])
        assert "artists" in response.json()

    def test_get_several_artists_invalid_ids_artists_property_is_an_array(self):
        response = get_several_artists(["572uUqNnEoaTeR0PuZHtyLLLk", "DDDDDDDDDDDDDDDDDDDS"])
        assert isinstance(response.json().get("artists"), list)

    def test_get_several_artists_invalid_ids_artists_array_has_length_of_2(self):
        response = get_several_artists(["572uUqNnEoaTeR0PuZHtyLLLk", "DDDDDDDDDDDDDDDDDDDS"])
        assert len(response.json().get("artists", [])) == 2

    def test_get_several_artists_invalid_ids_both_elements_in_artists_array_are_null(self):
        response = get_several_artists(["572uUqNnEoaTeR0PuZHtyLLLk", "DDDDDDDDDDDDDDDDDDDS"])
        assert response.json().get("artists", []) == [None, None]

    def test_get_several_artists_invalid_ids_both_elements_in_artists_array_are_of_type_null(self):
        response = get_several_artists(["572uUqNnEoaTeR0PuZHtyLLLk", "DDDDDDDDDDDDDDDDDDDS"])
        artists = response.json().get("artists", [])
        assert all(artist is None for artist in artists)



#GET SEVERAL ARTISTS invalid and valid ids

    def test_get_several_artists_valid_and_invalid_ids_response_is_an_object(self):
        response = get_several_artists(["572uUqNnEoaTeR0PuZHtyk", "DDDDDDDDDDDDDDDDDDDS"])
        assert isinstance(response.json(), dict)

    def test_get_several_artists_valid_and_invalid_ids_response_contains_artists_property(self):
        response = get_several_artists(["572uUqNnEoaTeR0PuZHtyk", "DDDDDDDDDDDDDDDDDDDS"])
        assert "artists" in response.json()

    def test_get_several_artists_valid_and_invalid_ids_artists_property_is_an_array(self):
        response = get_several_artists(["572uUqNnEoaTeR0PuZHtyk", "DDDDDDDDDDDDDDDDDDDS"])
        assert isinstance(response.json().get("artists"), list)

    def test_get_several_artists_valid_and_invalid_ids_artists_array_has_length_of_2(self):
        response = get_several_artists(["572uUqNnEoaTeR0PuZHtyk", "DDDDDDDDDDDDDDDDDDDS"])
        assert len(response.json().get("artists", [])) == 2

    def test_get_several_artists_valid_and_invalid_ids_first_artist_object_is_not_null(self):
        response = get_several_artists(["572uUqNnEoaTeR0PuZHtyk", "DDDDDDDDDDDDDDDDDDDS"])
        assert response.json().get("artists", [])[0] is not None

    def test_get_several_artists_valid_and_invalid_ids_second_artist_object_is_null(self):
        response = get_several_artists(["572uUqNnEoaTeR0PuZHtyk", "DDDDDDDDDDDDDDDDDDDS"])
        assert response.json().get("artists", [])[1] is None

    def test_get_several_artists_valid_and_invalid_ids_first_artist_has_name_property(self):
        response = get_several_artists(["572uUqNnEoaTeR0PuZHtyk", "DDDDDDDDDDDDDDDDDDDS"])
        first_artist = response.json().get("artists", [])[0]
        assert "name" in first_artist

    def test_get_several_artists_valid_and_invalid_ids_second_artist_is_null(self):
        response = get_several_artists(["572uUqNnEoaTeR0PuZHtyk", "DDDDDDDDDDDDDDDDDDDS"])
        assert response.json().get("artists", [])[1] is None
