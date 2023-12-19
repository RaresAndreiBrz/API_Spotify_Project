from requests_folder.shows.put_save_show_user import put_save_show_user


class TestPutSaveShowUser:


#Put Save Show for User valid id

    def test_put_save_show_for_user_valid_id_status_code(self):
        response = put_save_show_user("5EqqB52m2bsr4k1Ii7sStc")
        assert response.status_code == 200

    def test_put_save_show_for_user_valid_id_response_time(self):
        response = put_save_show_user("5EqqB52m2bsr4k1Ii7sStc")
        assert response.elapsed.total_seconds() * 1000 < 3000



#Put Save Show for User invalid id

    def test_put_save_show_for_user_invalid_id_status_code(self):
        response = put_save_show_user("101112131415161718192021")
        assert response.status_code == 400

    def test_put_save_show_for_user_invalid_id_content_type(self):
        response = put_save_show_user("101112131415161718192021")
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8'

    def test_put_save_show_for_user_invalid_id_body_contains_error(self):
        response = put_save_show_user("101112131415161718192021")
        assert 'error' in response.json()

    def test_put_save_show_for_user_invalid_id_body_contains_message(self):
        response = put_save_show_user("101112131415161718192021")
        assert 'message' in response.json()['error']

    def test_put_save_show_for_user_invalid_id_error_status(self):
        response = put_save_show_user("101112131415161718192021")
        assert response.json()['error']['status'] == 400

    def test_put_save_show_for_user_invalid_id_error_message(self):
        response = put_save_show_user("101112131415161718192021")
        assert response.json()['error']['message'] == "Bad request."

    def test_put_save_show_for_user_invalid_id_body_not_empty(self):
        response = put_save_show_user("101112131415161718192021")
        assert response.text != ""

    def test_put_save_show_for_user_invalid_id_body_length_greater_than_0(self):
        response = put_save_show_user("101112131415161718192021")
        assert len(response.text) > 0

    def test_put_save_show_for_user_invalid_id_response_not_null(self):
        response = put_save_show_user("101112131415161718192021")
        assert response.text is not None

    def test_put_save_show_for_user_invalid_id_response_not_empty_object(self):
        response = put_save_show_user("101112131415161718192021")
        assert response.json() != {}
