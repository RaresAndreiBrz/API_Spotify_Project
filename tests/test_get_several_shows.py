from requests_folder.shows.get_several_shows import get_several_shows


class TestGetSeveralShows:


#Get Several Shows valid params

    def test_get_several_shows_valid_ids_status_code(self):
        response = get_several_shows(["4rOoJ6Egrf8K2IrywzwOMk", "2i93Ub9rGWTNVyEg0rsxPb"], "RO")
        assert response.status_code == 200
    
    def test_get_several_shows_valid_ids_response_time(self):
        response = get_several_shows(["4rOoJ6Egrf8K2IrywzwOMk", "2i93Ub9rGWTNVyEg0rsxPb"], "RO")
        assert response.response_time < 3000
    


#Get Several Shows invalid ids and invalid market
    
    def test_get_several_shows_invalid_ids_invalid_market_status_code(self):
        response = get_several_shows(["4rOoJ6Egrf8K2IrywzwoMKK", "2i93Ub9rGWTNVyEg0rsxPb5555", "K2Irywzw93Ub87sad", "uyqh7bcbbna9HHasyn"], "YYU")
        assert response.status_code == 400
    
    def test_get_several_shows_invalid_ids_invalid_market_content_type(self):
        response = get_several_shows(["4rOoJ6Egrf8K2IrywzwoMKK", "2i93Ub9rGWTNVyEg0rsxPb5555", "K2Irywzw93Ub87sad", "uyqh7bcbbna9HHasyn"], "YYU")
        assert 'application/json; charset=utf-8' in response.headers['Content-Type']
    
    def test_get_several_shows_invalid_ids_invalid_market_response_body_is_object(self):
        response = get_several_shows(["4rOoJ6Egrf8K2IrywzwoMKK", "2i93Ub9rGWTNVyEg0rsxPb5555", "K2Irywzw93Ub87sad", "uyqh7bcbbna9HHasyn"], "YYU")
        assert isinstance(response.json(), dict)
    
    def test_get_several_shows_invalid_ids_invalid_market_error_object_exists(self):
        response = get_several_shows(["4rOoJ6Egrf8K2IrywzwoMKK", "2i93Ub9rGWTNVyEg0rsxPb5555", "K2Irywzw93Ub87sad", "uyqh7bcbbna9HHasyn"], "YYU")
        assert 'error' in response.json()
    
    def test_get_several_shows_invalid_ids_invalid_market_error_status(self):
        response = get_several_shows(["4rOoJ6Egrf8K2IrywzwoMKK", "2i93Ub9rGWTNVyEg0rsxPb5555", "K2Irywzw93Ub87sad", "uyqh7bcbbna9HHasyn"], "YYU")
        assert response.json()['error']['status'] == 400
    
    def test_get_several_shows_invalid_ids_invalid_market_error_message(self):
        response = get_several_shows(["4rOoJ6Egrf8K2IrywzwoMKK", "2i93Ub9rGWTNVyEg0rsxPb5555", "K2Irywzw93Ub87sad", "uyqh7bcbbna9HHasyn"], "YYU")
        assert response.json()['error']['message'] == 'Invalid market code'
    
    def test_get_several_shows_invalid_ids_invalid_market_response_time(self):
        response = get_several_shows(["4rOoJ6Egrf8K2IrywzwoMKK", "2i93Ub9rGWTNVyEg0rsxPb5555", "K2Irywzw93Ub87sad", "uyqh7bcbbna9HHasyn"], "YYU")
        assert response.response_time < 500
    


#Get Several Shows invalid ids

    def test_get_several_shows_invalid_ids_status_code(self):
        response = get_several_shows(["4rOoJ6Egrf8K2IrywzwoMk", "2i93Ub9rGWTNVyEg0rsxPb"], "RO")
        assert response.status_code == 200
    
    def test_get_several_shows_invalid_ids_body_contains_shows(self):
        response = get_several_shows(["4rOoJ6Egrf8K2IrywzwoMk", "2i93Ub9rGWTNVyEg0rsxPb"], "RO")
        assert 'shows' in response.text.lower()
    
    def test_get_several_shows_invalid_ids_language(self):
        response = get_several_shows(["4rOoJ6Egrf8K2IrywzwoMk", "2i93Ub9rGWTNVyEg0rsxPb"], "RO")
        shows = response.json()['shows']
        for show in shows:
            assert show['languages'][0] == "ro-RO"
    
    def test_get_several_shows_invalid_ids_media_type(self):
        response = get_several_shows(["4rOoJ6Egrf8K2IrywzwoMk", "2i93Ub9rGWTNVyEg0rsxPb"], "RO")
        shows = response.json()['shows']
        for show in shows:
            assert show['media_type'] == "audio"
    
    def test_get_several_shows_invalid_ids_total_episodes(self):
        response = get_several_shows(["4rOoJ6Egrf8K2IrywzwoMk", "2i93Ub9rGWTNVyEg0rsxPb"], "RO")
        shows = response.json()['shows']
        for show in shows:
            assert show['total_episodes'] >= 100
    
    def test_get_several_shows_invalid_ids_explicit(self):
        response = get_several_shows(["4rOoJ6Egrf8K2IrywzwoMk", "2i93Ub9rGWTNVyEg0rsxPb"], "RO")
        shows = response.json()['shows']
        for show in shows:
            assert not show['explicit']
    
    def test_get_several_shows_invalid_ids_is_externally_hosted(self):
        response = get_several_shows(["4rOoJ6Egrf8K2IrywzwoMk", "2i93Ub9rGWTNVyEg0rsxPb"], "RO")
        shows = response.json()['shows']
        for show in shows:
            assert not show['is_externally_hosted']
    
    def test_get_several_shows_invalid_ids_description_in_romanian(self):
        response = get_several_shows(["4rOoJ6Egrf8K2IrywzwoMk", "2i93Ub9rGWTNVyEg0rsxPb"], "RO")
        shows = response.json()['shows']
        for show in shows:
            assert 'cunoaștere de sine și dezvoltare personală' in show['description'].lower()
    
    def test_get_several_shows_invalid_ids_external_url_to_spotify(self):
        response = get_several_shows(["4rOoJ6Egrf8K2IrywzwoMk", "2i93Ub9rGWTNVyEg0rsxPb"], "RO")
        shows = response.json()['shows']
        for show in shows:
            assert 'https://open.spotify.com/show/' in show['external_urls']['spotify'].lower()
    
    def test_get_several_shows_invalid_ids_length(self):
        response = get_several_shows(["4rOoJ6Egrf8K2IrywzwoMk", "2i93Ub9rGWTNVyEg0rsxPb"], "RO")
        shows = response.json()['shows']
        assert len(shows) == 1
