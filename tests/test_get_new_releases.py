from requests_folder.releases.get_new_releases import get_new_releases


class TestGetNewReleases:


#GET NEW RELEASES valid params

    def test_get_new_releases_status_code(self):
        response = get_new_releases("2", "2", "RO")
        assert response.status_code == 200
    
    def test_get_new_releases_response_time(self):
        response = get_new_releases("2", "2", "RO")
        assert response.elapsed.total_seconds() * 1000 < 3000
    
    def test_get_new_releases_no_error_in_response(self):
        response = get_new_releases("2", "2", "RO")
        assert "error" not in response.text.lower()
    
    def test_get_new_releases_has_header(self):
        response = get_new_releases("2", "2", "RO")
        assert response.headers
    
    def test_get_new_releases_http_method_is_get(self):
        response = get_new_releases("2", "2", "RO")
        assert response.request.method == "GET"
    
    def test_get_new_releases_response_contains_parameters(self):
        response = get_new_releases("2", "2", "RO")
        assert "limit" in response.text
        assert "href" in response.text
        assert "next" in response.text
        assert "offset" in response.text
    
    def test_get_new_releases_response_has_correct_offset(self):
        response = get_new_releases("2", "2", "RO")
        data = response.json()
        assert data["albums"]["offset"] == 2
    
    def test_get_new_releases_response_has_correct_limit(self):
        response = get_new_releases("2", "2", "RO")
        data = response.json()
        assert data["albums"]["limit"] == 2
    
    def test_get_new_releases_response_has_correct_country_parameter(self):
        response = get_new_releases("2", "2", "RO")
        data = response.json()
        assert "RO" in data["albums"]["items"][0]["available_markets"]



#GET NEW RELEASES invalid params(country)

    def test_get_new_releases_response_is_object(self):
        response = get_new_releases("2", "2", "ZZZ")
        assert isinstance(response.json(), dict)

    def test_get_new_releases_response_contains_error_property(self):
        response = get_new_releases("2", "2", "ZZZ")
        assert "error" in response.json()

    def test_get_new_releases_error_object_has_status_property(self):
        response = get_new_releases("2", "2", "ZZZ")
        assert "status" in response.json()["error"]

    def test_get_new_releases_error_object_has_message_property(self):
        response = get_new_releases("2", "2", "ZZZ")
        assert "message" in response.json()["error"]

    def test_get_new_releases_error_status_is_400(self):
        response = get_new_releases("2", "2", "ZZZ")
        assert response.json()["error"]["status"] == 400

    def test_get_new_releases_error_message_is_invalid_country_code(self):
        response = get_new_releases("2", "2", "ZZZ")
        assert response.json()["error"]["message"] == "Invalid country code"
