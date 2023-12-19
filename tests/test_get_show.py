from requests_folder.shows.get_shows import get_show



class TestGetShow:


#Get Show valid ids

    def test_get_show_valid_id_status_code_is_200(self):
        response = get_show("4rOoJ6Egrf8K2IrywzwOMk", "RO")
        assert response.status_code == 200

    def test_get_show_valid_id_response_time_valid(self):
        response = get_show("4rOoJ6Egrf8K2IrywzwOMk", "RO")
        assert response.elapsed.total_seconds() * 1000 < 3000



#Get Show invalid ids

    def test_get_show_invalid_id_status_code(self):
        response = get_show("4rOoJ6Egrf8K2IrywzwoMk", "RO")
        assert response.status_code == 404

    def test_get_show_invalid_id_content_type(self):
        response = get_show("4rOoJ6Egrf8K2IrywzwoMk", "RO")
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8'

    def test_get_show_invalid_id_body_contains_error(self):
        response = get_show("4rOoJ6Egrf8K2IrywzwoMk", "RO")
        assert 'error' in response.text.lower()

    def test_get_show_invalid_id_body_contains_message(self):
        response = get_show("4rOoJ6Egrf8K2IrywzwoMk", "RO")
        assert 'message' in response.text.lower()

    def test_get_show_invalid_id_error_status(self):
        response = get_show("4rOoJ6Egrf8K2IrywzwoMk", "RO")
        assert response.json()['error']['status'] == 404

    def test_get_show_invalid_id_error_message(self):
        response = get_show("4rOoJ6Egrf8K2IrywzwoMk", "RO")
        assert response.json()['error']['message'] == 'non existing id'
