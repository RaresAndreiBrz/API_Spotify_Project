from requests_folder.categories.get_single_category import get_single_category


class TestGetSingleCategory:


#Get Single Category valid params

    def test_get_single_category_status_code_is_200(self):
        response = get_single_category("dinner", "ro_RO", "RO")
        assert response.status_code == 200

    def test_get_single_category_response_time_is_less_than_200ms(self):
        response = get_single_category("dinner", "ro_RO", "RO")
        assert response.elapsed.total_seconds() * 1000 < 200

    def test_get_single_category_checking_of_HTTP_method_Get(self):
        response = get_single_category("dinner", "ro_RO", "RO")
        assert response.request.method == "GET"

    def test_get_single_category_check_the_total_number_of_categories(self):
        response = get_single_category("dinner", "ro_RO", "RO")
        categories = response.json().get('categories', {})
        assert 'total' in categories and categories['total'] == 47

    def test_get_single_category_check_if_the_categories_field_exists(self):
        response = get_single_category("dinner", "ro_RO", "RO")
        assert 'categories' in response.json()

    def test_get_single_category_check_if_the_response_is_valid_JSON(self):
        response = get_single_category("dinner", "ro_RO", "RO")
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8'

    def test_get_single_category_check_if_error_shows_up_in_response(self):
        response = get_single_category("dinner", "ro_RO", "RO")
        assert 'error' not in response.text()



#Get Several Categories invalid id and valid params

    def test_get_single_category_invalid_id_categories_exist(self):
        response = get_single_category("bzzzzzzzzzzzzzzzzzz", "ro_RO", "RO")
        assert 'categories' in response.json()
    
    def test_get_single_category_invalid_id_categories_object_has_items_property(self):
        response = get_single_category("bzzzzzzzzzzzzzzzzzz", "ro_RO", "RO")
        assert 'items' in response.json()['categories']
    
    def test_get_single_category_invalid_id_at_least_5_items_in_items_array(self):
        response = get_single_category("bzzzzzzzzzzzzzzzzzz", "ro_RO", "RO")
        items_array = response.json()['categories']['items']
        assert isinstance(items_array, list) and len(items_array) >= 5
    
    def test_get_single_category_invalid_id_first_category_has_id_and_name_properties(self):
        response = get_single_category("bzzzzzzzzzzzzzzzzzz", "ro_RO", "RO")
        first_category = response.json()['categories']['items'][0]
        assert 'id' in first_category and 'name' in first_category
    
    def test_get_single_category_invalid_id_icons_exist_for_all_categories(self):
        response = get_single_category("bzzzzzzzzzzzzzzzzzz", "ro_RO", "RO")
        categories = response.json()['categories']['items']
        for category in categories:
            assert 'icons' in category
    
    def test_get_single_category_invalid_id_categories_have_valid_URLs_for_icons(self):
        response = get_single_category("bzzzzzzzzzzzzzzzzzz", "ro_RO", "RO")
        categories = response.json()['categories']['items']
        for category in categories:
            assert 'url' in category['icons'][0]
    
    def test_get_single_category_invalid_id_all_categories_have_id_and_name(self):
        response = get_single_category("bzzzzzzzzzzzzzzzzzz", "ro_RO", "RO")
        categories = response.json()['categories']['items']
        for category in categories:
            assert 'id' in category and 'name' in category
    
    def test_get_single_category_invalid_id_check_if_limit_is_20(self):
        response = get_single_category("bzzzzzzzzzzzzzzzzzz", "ro_RO", "RO")
        assert response.json()['categories']['limit'] == 20
    
    def test_get_single_category_invalid_id_next_page_URL_exists(self):
        response = get_single_category("bzzzzzzzzzzzzzzzzzz", "ro_RO", "RO")
        assert 'next' in response.json()['categories']
    
    def test_get_single_category_invalid_id_offset_is_0(self):
        response = get_single_category("bzzzzzzzzzzzzzzzzzz", "ro_RO", "RO")
        assert response.json()['categories']['offset'] == 0
    
    def test_get_single_category_invalid_id_total_categories_is_a_number(self):
        response = get_single_category("bzzzzzzzzzzzzzzzzzz", "ro_RO", "RO")
        assert isinstance(response.json()['categories']['total'], int)
    
    def test_get_single_category_invalid_id_first_category_has_name_of_Top_liste(self):
        response = get_single_category("bzzzzzzzzzzzzzzzzzz", "ro_RO", "RO")
        assert response.json()['categories']['items'][0]['name'] == "Top liste"
    
    def test_get_single_category_invalid_id_category_with_ID_0JQ5DAqbMKFAUsdyVjCQuL_exists(self):
        response = get_single_category("bzzzzzzzzzzzzzzzzzz", "ro_RO", "RO")
        categories = response.json()['categories']['items']
        assert any(category['id'] == "0JQ5DAqbMKFAUsdyVjCQuL" for category in categories)
    
    def test_get_single_category_invalid_id_category_with_ID_0JQ5DAqbMKFF9bY76LXmfI_exists(self):
        response = get_single_category("bzzzzzzzzzzzzzzzzzz", "ro_RO", "RO")
        categories = response.json()['categories']['items']
        assert any(category['id'] == "0JQ5DAqbMKFF9bY76LXmfI" for category in categories)
    
    def test_get_single_category_invalid_id_last_category_has_name_of_Jazz(self):
        response = get_single_category("bzzzzzzzzzzzzzzzzzz", "ro_RO", "RO")
        categories = response.json()['categories']['items']
        last_category = categories[-1]
        assert last_category['name'] == "Jazz"
