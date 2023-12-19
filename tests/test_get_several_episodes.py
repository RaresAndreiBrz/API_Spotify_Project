from requests_folder.episodes.get_several_episodes import get_several_episodes, get_several_episodes_with_market


class TestGetSeveralEpisodes:


#Get Several Episodes valid params

    def test_get_several_episodes_status_code_is_200(self):
        response = get_several_episodes(["2SydVEJ8apGliqKX1W2SWS"])
        assert response.status_code == 200

    def test_get_several_episodes_response_time_is_less_than_200ms(self):
        response = get_several_episodes(["2SydVEJ8apGliqKX1W2SWS"])
        assert response.elapsed.total_seconds() * 1000 < 200



#Get Several Episodes invalid ids

    def test_get_several_episodes_response_has_a_200_status_code(self):
        response = get_several_episodes(["2sydVEJ8apGliqKX1W2SWS", "6eY2ryN7khNgIZSv9MrpOL", "26oq7fUJAdR8S88JqG9slG"])
        assert response.status_code == 200

    def test_get_several_episodes_response_is_JSON(self):
        response = get_several_episodes(["2sydVEJ8apGliqKX1W2SWS", "6eY2ryN7khNgIZSv9MrpOL", "26oq7fUJAdR8S88JqG9slG"])
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8'

    def test_get_several_episodes_response_is_an_object(self):
        response = get_several_episodes(["2sydVEJ8apGliqKX1W2SWS", "6eY2ryN7khNgIZSv9MrpOL", "26oq7fUJAdR8S88JqG9slG"])
        assert isinstance(response.json(), dict)

    def test_get_several_episodes_episode_object_exists(self):
        response = get_several_episodes(["2sydVEJ8apGliqKX1W2SWS", "6eY2ryN7khNgIZSv9MrpOL", "26oq7fUJAdR8S88JqG9slG"])
        assert isinstance(response.json().get('episodes', [])[1], dict)

    def test_get_several_episodes_episode_has_id_property(self):
        response = get_several_episodes(["2sydVEJ8apGliqKX1W2SWS", "6eY2ryN7khNgIZSv9MrpOL", "26oq7fUJAdR8S88JqG9slG"])
        assert 'id' in response.json().get('episodes', [])[1]

    def test_get_several_episodes_episode_has_name_property(self):
        response = get_several_episodes(["2sydVEJ8apGliqKX1W2SWS", "6eY2ryN7khNgIZSv9MrpOL", "26oq7fUJAdR8S88JqG9slG"])
        assert 'name' in response.json().get('episodes', [])[1]

    def test_get_several_episodes_episode_has_description_property(self):
        response = get_several_episodes(["2sydVEJ8apGliqKX1W2SWS", "6eY2ryN7khNgIZSv9MrpOL", "26oq7fUJAdR8S88JqG9slG"])
        assert 'description' in response.json().get('episodes', [])[1]

    def test_get_several_episodes_episode_has_duration_ms_property(self):
        response = get_several_episodes(["2sydVEJ8apGliqKX1W2SWS", "6eY2ryN7khNgIZSv9MrpOL", "26oq7fUJAdR8S88JqG9slG"])
        assert 'duration_ms' in response.json().get('episodes', [])[1]

    def test_get_several_episodes_episode_has_explicit_property(self):
        response = get_several_episodes(["2sydVEJ8apGliqKX1W2SWS", "6eY2ryN7khNgIZSv9MrpOL", "26oq7fUJAdR8S88JqG9slG"])
        assert 'explicit' in response.json().get('episodes', [])[1]

    def test_get_several_episodes_episode_has_release_date_property(self):
        response = get_several_episodes(["2sydVEJ8apGliqKX1W2SWS", "6eY2ryN7khNgIZSv9MrpOL", "26oq7fUJAdR8S88JqG9slG"])
        assert 'release_date' in response.json().get('episodes', [])[1]



#Get Several Episodes invalid ids and valid market
    
    def test_get_several_episodes_invalid_ids_valid_market_response_has_a_200_status_code(self):
        response = get_several_episodes_with_market(["*/888**/..::PPP0"], "RO")
        assert response.status_code == 200

    def test_get_several_episodes_invalid_ids_valid_market_response_is_JSON(self):
        response = get_several_episodes_with_market(["*/888**/..::PPP0"], "RO")
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8'

    def test_get_several_episodes_invalid_ids_valid_market_response_is_an_object(self):
        response = get_several_episodes_with_market(["*/888**/..::PPP0"], "RO")
        assert isinstance(response.json(), dict)

    def test_get_several_episodes_invalid_ids_valid_market_episodes_array_contains_one_null_value(self):
        response = get_several_episodes_with_market(["*/888**/..::PPP0"], "RO")
        assert response.json().get('episodes') == [None]

    def test_get_several_episodes_invalid_ids_valid_market_episodes_array_length_is_1(self):
        response = get_several_episodes_with_market(["*/888**/..::PPP0"], "RO")
        assert len(response.json().get('episodes', [])) == 1
