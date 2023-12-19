from requests_folder.shows.del_saved_show import del_saved_show_user


class TestDelSavedShowsUser:


#Del Saved Show for User valid id

    def test_del_saved_show_user_valid_id(self):
        response = del_saved_show_user(["7EKD1qYk2tkRHY6u6jpmNS"])
        assert response.status_code == 200

    def test_del_saved_show_user_response_time(self):
        response = del_saved_show_user(["7EKD1qYk2tkRHY6u6jpmNS"])
        assert response.elapsed.total_seconds() * 1000 < 200



#Del Saved Show for User invalid id

    def test_del_saved_show_user_invalid_id_status_code(self):
        response = del_saved_show_user(["[{{7EKD1qYk2tkRHY6u6jpmNss546666654545465454}}]"])
        assert response.status_code == 400

    def test_del_saved_show_user_invalid_id_empty_body(self):
        response = del_saved_show_user(["[{{7EKD1qYk2tkRHY6u6jpmNss546666654545465454}}]"])
        assert response.text == ""

    def test_del_saved_show_user_invalid_id_body_length(self):
        response = del_saved_show_user(["[{{7EKD1qYk2tkRHY6u6jpmNss546666654545465454}}]"])
        assert len(response.text) == 0

    def test_del_saved_show_user_invalid_id_not_empty_object(self):
        response = del_saved_show_user(["[{{7EKD1qYk2tkRHY6u6jpmNss546666654545465454}}]"])
        assert response.text != "{}"

    def test_del_saved_show_user_invalid_id_not_null(self):
        response = del_saved_show_user(["[{{7EKD1qYk2tkRHY6u6jpmNss546666654545465454}}]"])
        assert response.text is not None



#Del Saved Show for User inexistent id

    def test_del_saved_show_user_status_code(self):
        response = del_saved_show_user(["7EKD1qYk2tkRHY6u6jpmNS"])
        assert response.status_code == 200

    def test_del_saved_show_user_empty_body(self):
        response = del_saved_show_user(["7EKD1qYk2tkRHY6u6jpmNS"])
        assert response.text == ""

    def test_del_saved_show_user_content_type(self):
        response = del_saved_show_user(["7EKD1qYk2tkRHY6u6jpmNS"])
        assert response.headers.get("Content-Type") == "application/json; charset=utf-8"

    def test_del_saved_show_user_content_length(self):
        response = del_saved_show_user(["7EKD1qYk2tkRHY6u6jpmNS"])
        assert int(response.headers.get("Content-Length", 0)) == 0
