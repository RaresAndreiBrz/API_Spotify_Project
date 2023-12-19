from requests_folder.albums.del_saved_albums import del_saved_albums


class TestDelSavedAlbums:


#DEL SAVED ALBUMS valid ids

    def test_del_saved_albums_status_code(self):
        response = del_saved_albums({"ids":["01u9MdrytYwPidRT0uoCXR"]})
        print(response)
        assert "400" in response, "Status code is not 200"
    #
    # def test_del_saved_albums_response_time(self):
    #     response = del_saved_albums({"ids": ["01u9MdrytYwPidRT0uoCXR"]})
    #     assert response.elapsed.total_seconds() < 3, "Response time is not less than 3 seconds"
    #
    # def test_del_saved_albums_http_method(self):
    #     response = del_saved_albums({"ids": ["01u9MdrytYwPidRT0uoCXR"]})
    #     request_method = response.request.method
    #     assert request_method == "DELETE", "HTTP method is not DELETE"
    #
    # def test_del_saved_albums_no_error_in_response(self):
    #     response = del_saved_albums({"ids": ["01u9MdrytYwPidRT0uoCXR"]})
    #     assert "error" not in response.text, "Error shows up in response"
    #
    # def test_del_saved_albums_empty_body(self):
    #     response = del_saved_albums({"ids": ["01u9MdrytYwPidRT0uoCXR"]})
    #     assert response.text == "", "Response body is not empty"
    #
    # def test_del_saved_albums_header_exists(self):
    #     response = del_saved_albums({"ids": ["01u9MdrytYwPidRT0uoCXR"]})
    #     assert "x-robots-tag" in response.headers, "Header is missing in response"
    #
    # def test_del_saved_albums_header_correct(self):
    #     response = del_saved_albums({"ids": ["01u9MdrytYwPidRT0uoCXR"]})
    #     assert response.headers["x-robots-tag"] == "correct_value", "Header is not correct"
