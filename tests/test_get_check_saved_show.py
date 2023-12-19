from requests_folder.shows.get_check_saved_show import get_check_saved_show


class TestGetCheckSavedShow:


#GET Check Saved Show valid ids

    def test_get_check_saved_show_valid_id_status_code(self):
        response = get_check_saved_show(["5eodRZd3qR9VT1ip1wI7xQ"])
        assert response.status_code == 200

    def test_get_check_saved_show_valid_id_response_time(self):
        response = get_check_saved_show(["5eodRZd3qR9VT1ip1wI7xQ"])
        assert response.responseTime < 3000



#GET Check Saved Show invalid ids

    def test_get_check_saved_show_multiple_invalid_ids_first_element(self):
        response = get_check_saved_show(["5eodRZd3qR9VT1ip1wI7xQ", "5EqqB52m2bsr4k1Ii7sStc", "7EKD1qYk2tkRHY6u6jpmNS", "2i93Ub9rGWTNVyEg0rsxPb"])
        assert response.json()[0] is True

    def test_get_check_saved_show_multiple_invalid_ids_second_element(self):
        response = get_check_saved_show(["5eodRZd3qR9VT1ip1wI7xQ", "5EqqB52m2bsr4k1Ii7sStc", "7EKD1qYk2tkRHY6u6jpmNS", "2i93Ub9rGWTNVyEg0rsxPb"])
        assert response.json()[1] is True

    def test_get_check_saved_show_multiple_invalid_ids_third_element(self):
        response = get_check_saved_show(["5eodRZd3qR9VT1ip1wI7xQ", "5EqqB52m2bsr4k1Ii7sStc", "7EKD1qYk2tkRHY6u6jpmNS", "2i93Ub9rGWTNVyEg0rsxPb"])
        assert response.json()[2] is False

    def test_get_check_saved_show_multiple_invalid_ids_fourth_element(self):
        response = get_check_saved_show(["5eodRZd3qR9VT1ip1wI7xQ", "5EqqB52m2bsr4k1Ii7sStc", "7EKD1qYk2tkRHY6u6jpmNS", "2i93Ub9rGWTNVyEg0rsxPb"])
        assert response.json()[3] is False

    def test_get_check_saved_show_multiple_invalid_ids_all_elements_boolean(self):
        response = get_check_saved_show(["5eodRZd3qR9VT1ip1wI7xQ", "5EqqB52m2bsr4k1Ii7sStc", "7EKD1qYk2tkRHY6u6jpmNS", "2i93Ub9rGWTNVyEg0rsxPb"])
        elements = response.json()
        for element in elements:
            assert type(element) == bool

    def test_get_check_saved_show_multiple_invalid_ids_array_length(self):
        response = get_check_saved_show(["5eodRZd3qR9VT1ip1wI7xQ", "5EqqB52m2bsr4k1Ii7sStc", "7EKD1qYk2tkRHY6u6jpmNS", "2i93Ub9rGWTNVyEg0rsxPb"])
        elements = response.json()
        assert type(elements) == list
        assert len(elements) == 4

    def test_get_check_saved_show_multiple_invalid_ids_no_null_elements(self):
        response = get_check_saved_show(["5eodRZd3qR9VT1ip1wI7xQ", "5EqqB52m2bsr4k1Ii7sStc", "7EKD1qYk2tkRHY6u6jpmNS", "2i93Ub9rGWTNVyEg0rsxPb"])
        elements = response.json()
        for element in elements:
            assert element is not None



#GET Check Saved Show invalid shows

    def test_get_check_saved_show_multiple_invalid_shows_first_element(self):
        response = get_check_saved_show(["5eodRZd3qR9VT1ip1wI7xQ", "5EqqB52m2bsr4k1Ii7sStc", "7EKD1qYk2tkRHY6u6jpmNS", "2i93Ub9rGWTNVyEg0rsxPb"])
        assert response.json()[0] is True

    def test_get_check_saved_show_multiple_invalid_shows_second_element(self):
        response = get_check_saved_show(["5eodRZd3qR9VT1ip1wI7xQ", "5EqqB52m2bsr4k1Ii7sStc", "7EKD1qYk2tkRHY6u6jpmNS", "2i93Ub9rGWTNVyEg0rsxPb"])
        assert response.json()[1] is True

    def test_get_check_saved_show_multiple_invalid_shows_third_element(self):
        response = get_check_saved_show(["5eodRZd3qR9VT1ip1wI7xQ", "5EqqB52m2bsr4k1Ii7sStc", "7EKD1qYk2tkRHY6u6jpmNS", "2i93Ub9rGWTNVyEg0rsxPb"])
        assert response.json()[2] is False

    def test_get_check_saved_show_multiple_invalid_shows_fourth_element(self):
        response = get_check_saved_show(["5eodRZd3qR9VT1ip1wI7xQ", "5EqqB52m2bsr4k1Ii7sStc", "7EKD1qYk2tkRHY6u6jpmNS", "2i93Ub9rGWTNVyEg0rsxPb"])
        assert response.json()[3] is False

    def test_get_check_saved_show_multiple_invalid_shows_all_elements_boolean(self):
        response = get_check_saved_show(["5eodRZd3qR9VT1ip1wI7xQ", "5EqqB52m2bsr4k1Ii7sStc", "7EKD1qYk2tkRHY6u6jpmNS", "2i93Ub9rGWTNVyEg0rsxPb"])
        elements = response.json()
        for element in elements:
            assert type(element) == bool

    def test_get_check_saved_show_multiple_invalid_shows_array_length(self):
        response = get_check_saved_show(["5eodRZd3qR9VT1ip1wI7xQ", "5EqqB52m2bsr4k1Ii7sStc", "7EKD1qYk2tkRHY6u6jpmNS", "2i93Ub9rGWTNVyEg0rsxPb"])
        elements = response.json()
        assert type(elements) == list
        assert len(elements) == 4

    def test_get_check_saved_show_multiple_invalid_shows_no_null_elements(self):
        response = get_check_saved_show(["5eodRZd3qR9VT1ip1wI7xQ", "5EqqB52m2bsr4k1Ii7sStc", "7EKD1qYk2tkRHY6u6jpmNS", "2i93Ub9rGWTNVyEg0rsxPb"])
        elements = response.json()
        for element in elements:
            assert element is not None
