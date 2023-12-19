from requests_folder.categories.get_several_categories import get_several_categories


class TestGetSeveralCategories:


#Get Several Categories valid params
   
    def test_get_several_categories_status_code_200(self):
        response = get_several_categories("ro_RO", "1", "10", "RO")
        assert response.status_code == 200

    def test_get_several_categories_response_time_is_less_than_200ms(self):
        response = get_several_categories("ro_RO", "1", "10", "RO")
        assert response.elapsed.total_seconds() * 1000 < 200

    def test_get_several_categories_category_names_as_many_as_limit_value_is_specified(self):
        response = get_several_categories("ro_RO", "1", "10", "RO")
        response_body = response.json()
        limit = response_body['categories']['limit']
        name_count = sum('name' in item for item in response_body.get('categories', {}).get('items', []))
        assert name_count == limit

    def test_get_several_categories_check_if_error_shows_up_in_response(self):
        response = get_several_categories("ro_RO", "1", "10", "RO")
        assert "error" not in response.text()

    def test_get_several_categories_checking_of_HTTP_method_Get(self):
        response = get_several_categories("ro_RO", "1", "10", "RO")
        assert response.request.method == "GET"

    def test_get_several_categories_check_if_Party_category_shows_up(self):
        response = get_several_categories("ro_RO", "1", "10", "RO")
        categories = response.json()['categories']['items']
        category_exists = any(category['name'] == "Party" for category in categories)
        assert category_exists

    def test_get_several_categories_first_category_is_Romantica(self):
        response = get_several_categories("ro_RO", "1", "10", "RO")
        first_category_name = response.json()['categories']['items'][0]['name']
        assert first_category_name == "Romantică"
