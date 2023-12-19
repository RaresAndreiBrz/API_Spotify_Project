from requests_folder.albums.get_several_albums import get_several_valid_albums, get_several_albums_invalid_range


class TestGetSeveralAlbums:


#SEVERAL ALBUMS Min. Value

    def test_get_several_albums_minRange_status_code(self):
        response = get_several_valid_albums(["2DQhAbIgZG4QRy4mmQsFE0", "4DZHSpFEwfDphP87KSH3jk"])
        assert response.status_code == 200

    def test_get_several_albums_minRange_response_time(self):
        response = get_several_valid_albums(["2DQhAbIgZG4QRy4mmQsFE0", "4DZHSpFEwfDphP87KSH3jk"])
        assert response.responseTime < 3000

    def test_get_several_albums_minRange_check_json_structure(self):
        response = get_several_valid_albums(["2DQhAbIgZG4QRy4mmQsFE0", "4DZHSpFEwfDphP87KSH3jk"])
        assert response.to_be_json
        assert "albums" in response.json()

    def test_get_several_albums_minRange_check_response_contains_header(self):
        response = get_several_valid_albums(["2DQhAbIgZG4QRy4mmQsFE0", "4DZHSpFEwfDphP87KSH3jk"])
        assert "albums" in response.json()

    def test_get_several_albums_minRange_response_contains_album_type(self):
        response = get_several_valid_albums(["2DQhAbIgZG4QRy4mmQsFE0", "4DZHSpFEwfDphP87KSH3jk"])
        assert "album_type" in response.text()

    def test_get_several_albums_minRange_response_contains_requested_ids(self):
        response = get_several_valid_albums(["2DQhAbIgZG4QRy4mmQsFE0", "4DZHSpFEwfDphP87KSH3jk"])
        assert "4DZHSpFEwfDphP87KSH3jk" in response.text()
        assert "2DQhAbIgZG4QRy4mmQsFE0" in response.text()

    def test_get_several_albums_minRange_response_contains_not_requested_ids(self):
        response = get_several_valid_albums(["2DQhAbIgZG4QRy4mmQsFE0", "4DZHSpFEwfDphP87KSH3jk"])
        assert "478ajJKKosauiuiiu5454" not in response.text()



#SEVERAL ALBUMS Max. Value

    def test_get_several_albums_rangeMax_status_code(self):
        response = get_several_valid_albums(["K7m1TRRzyfQ3dav2JVgdj,3aTuW4BtsyyyyQa9LKqj8n,0NZQTozgPtlt5iN3hmANhy,5lf8VH2121Ngg7AD3Ps8Ch,0bhYU6Jz7XaXw9x67pSWTc,01u9MdrytYwPidRT0uoCXR,1cIdztckCGQOeGrou4xOG4,4JTFvbBdQuXIafNDMuezO0,679ytQ4HN7FspEGibjecXj,1t3Z2hSfT1fm5iHHWC65xd,128oy4BxWb3Tk4jsdwRdBq,3HNnxK7NgLXbDoxRZxNWiR,7MZzYkbHL9Tk3O6WeD4Z0Z,4otkd9As6YaxxEkIjXPiZ6,2DQhAbIgZG4QRy4mmQsFE0,47BiFcV59TQi2s9SkBo2pb,1kTlYbs28MXw7hwO0NLYif,2cWBwpqMsDJC1ZUwz813lo,4DZHSpFEwfDphP87KSH3jk,3nTMdaxlWKNs9TPL64pNDr"])
        assert response.status_code == 200

    def test_get_several_albums_rangeMax_response_time(self):
        response = get_several_valid_albums(["K7m1TRRzyfQ3dav2JVgdj,3aTuW4BtsyyyyQa9LKqj8n,0NZQTozgPtlt5iN3hmANhy,5lf8VH2121Ngg7AD3Ps8Ch,0bhYU6Jz7XaXw9x67pSWTc,01u9MdrytYwPidRT0uoCXR,1cIdztckCGQOeGrou4xOG4,4JTFvbBdQuXIafNDMuezO0,679ytQ4HN7FspEGibjecXj,1t3Z2hSfT1fm5iHHWC65xd,128oy4BxWb3Tk4jsdwRdBq,3HNnxK7NgLXbDoxRZxNWiR,7MZzYkbHL9Tk3O6WeD4Z0Z,4otkd9As6YaxxEkIjXPiZ6,2DQhAbIgZG4QRy4mmQsFE0,47BiFcV59TQi2s9SkBo2pb,1kTlYbs28MXw7hwO0NLYif,2cWBwpqMsDJC1ZUwz813lo,4DZHSpFEwfDphP87KSH3jk,3nTMdaxlWKNs9TPL64pNDr"])
        assert response.responseTime < 3000

    def test_get_several_albums_rangeMax_response_contains_part_of_requested_ids(self):
        response = get_several_valid_albums(["K7m1TRRzyfQ3dav2JVgdj,3aTuW4BtsyyyyQa9LKqj8n,0NZQTozgPtlt5iN3hmANhy,5lf8VH2121Ngg7AD3Ps8Ch,0bhYU6Jz7XaXw9x67pSWTc,01u9MdrytYwPidRT0uoCXR,1cIdztckCGQOeGrou4xOG4,4JTFvbBdQuXIafNDMuezO0,679ytQ4HN7FspEGibjecXj,1t3Z2hSfT1fm5iHHWC65xd,128oy4BxWb3Tk4jsdwRdBq,3HNnxK7NgLXbDoxRZxNWiR,7MZzYkbHL9Tk3O6WeD4Z0Z,4otkd9As6YaxxEkIjXPiZ6,2DQhAbIgZG4QRy4mmQsFE0,47BiFcV59TQi2s9SkBo2pb,1kTlYbs28MXw7hwO0NLYif,2cWBwpqMsDJC1ZUwz813lo,4DZHSpFEwfDphP87KSH3jk,3nTMdaxlWKNs9TPL64pNDr"])
        assert "1kTlYbs28MXw7hwO0NLYif" in response.text()
        assert "4DZHSpFEwfDphP87KSH3jk" in response.text()
        assert "2cWBwpqMsDJC1ZUwz813lo" in response.text()
        assert "0NZQTozgPtlt5iN3hmANhy" in response.text()
        assert "3nTMdaxlWKNs9TPL64pNDr" in response.text()



    def test_get_several_albums_rangeMax_first_object_received_from_request_as_expected(self):
        data = get_several_valid_albums(["K7m1TRRzyfQ3dav2JVgdj,3aTuW4BtsyyyyQa9LKqj8n,0NZQTozgPtlt5iN3hmANhy,5lf8VH2121Ngg7AD3Ps8Ch,0bhYU6Jz7XaXw9x67pSWTc,01u9MdrytYwPidRT0uoCXR,1cIdztckCGQOeGrou4xOG4,4JTFvbBdQuXIafNDMuezO0,679ytQ4HN7FspEGibjecXj,1t3Z2hSfT1fm5iHHWC65xd,128oy4BxWb3Tk4jsdwRdBq,3HNnxK7NgLXbDoxRZxNWiR,7MZzYkbHL9Tk3O6WeD4Z0Z,4otkd9As6YaxxEkIjXPiZ6,2DQhAbIgZG4QRy4mmQsFE0,47BiFcV59TQi2s9SkBo2pb,1kTlYbs28MXw7hwO0NLYif,2cWBwpqMsDJC1ZUwz813lo,4DZHSpFEwfDphP87KSH3jk,3nTMdaxlWKNs9TPL64pNDr"]).json()
        assert data["albums"][0]["album_type"] == "album"

    def test_get_several_albums_rangeMax_all_albums_returned(self):
        data = get_several_valid_albums(["K7m1TRRzyfQ3dav2JVgdj,3aTuW4BtsyyyyQa9LKqj8n,0NZQTozgPtlt5iN3hmANhy,5lf8VH2121Ngg7AD3Ps8Ch,0bhYU6Jz7XaXw9x67pSWTc,01u9MdrytYwPidRT0uoCXR,1cIdztckCGQOeGrou4xOG4,4JTFvbBdQuXIafNDMuezO0,679ytQ4HN7FspEGibjecXj,1t3Z2hSfT1fm5iHHWC65xd,128oy4BxWb3Tk4jsdwRdBq,3HNnxK7NgLXbDoxRZxNWiR,7MZzYkbHL9Tk3O6WeD4Z0Z,4otkd9As6YaxxEkIjXPiZ6,2DQhAbIgZG4QRy4mmQsFE0,47BiFcV59TQi2s9SkBo2pb,1kTlYbs28MXw7hwO0NLYif,2cWBwpqMsDJC1ZUwz813lo,4DZHSpFEwfDphP87KSH3jk,3nTMdaxlWKNs9TPL64pNDr"]).json()
        assert len(data["albums"]) == 20



#SEVERAL ALBUMS Invalid range ids

    def test_get_several_albums_rangeMaxInvalid_status_code(self):
        response = get_several_albums_invalid_range([
            '7qNY7C7rkJwioya4lKLrJt', '3K7m1TRRzyfQ3dav2JVgdj', '3aTuW4BtsyyyyQa9LKqj8n',
            '0NZQTozgPtlt5iN3hmANhy', '5lf8VH2121Ngg7AD3Ps8Ch', '0bhYU6Jz7XaXw9x67pSWTc',
            '01u9MdrytYwPidRT0uoCXR', '1cIdztckCGQOeGrou4xOG4', '4JTFvbBdQuXIafNDMuezO0',
            '679ytQ4HN7FspEGibjecXj', '1t3Z2hSfT1fm5iHHWC65xd', '128oy4BxWb3Tk4jsdwRdBq',
            '3HNnxK7NgLXbDoxRZxNWiR', '7MZzYkbHL9Tk3O6WeD4Z0Z', '4otkd9As6YaxxEkIjXPiZ6',
            '2DQhAbIgZG4QRy4mmQsFE0', '47BiFcV59TQi2s9SkBo2pb', '1kTlYbs28MXw7hwO0NLYif',
            '2cWBwpqMsDJC1ZUwz813lo', '4DZHSpFEwfDphP87KSH3jk', '3nTMdaxlWKNs9TPL64pNDr'
        ])
        assert response.status_code == 400

    def test_get_several_albums_rangeMaxInvalid_response_time(self):
        response = get_several_albums_invalid_range([
            '7qNY7C7rkJwioya4lKLrJt', '3K7m1TRRzyfQ3dav2JVgdj', '3aTuW4BtsyyyyQa9LKqj8n',
            '0NZQTozgPtlt5iN3hmANhy', '5lf8VH2121Ngg7AD3Ps8Ch', '0bhYU6Jz7XaXw9x67pSWTc',
            '01u9MdrytYwPidRT0uoCXR', '1cIdztckCGQOeGrou4xOG4', '4JTFvbBdQuXIafNDMuezO0',
            '679ytQ4HN7FspEGibjecXj', '1t3Z2hSfT1fm5iHHWC65xd', '128oy4BxWb3Tk4jsdwRdBq',
            '3HNnxK7NgLXbDoxRZxNWiR', '7MZzYkbHL9Tk3O6WeD4Z0Z', '4otkd9As6YaxxEkIjXPiZ6',
            '2DQhAbIgZG4QRy4mmQsFE0', '47BiFcV59TQi2s9SkBo2pb', '1kTlYbs28MXw7hwO0NLYif',
            '2cWBwpqMsDJC1ZUwz813lo', '4DZHSpFEwfDphP87KSH3jk', '3nTMdaxlWKNs9TPL64pNDr'
        ])
        assert response.responseTime < 3000

    def test_get_several_albums_rangeMaxInvalid_check_error_object_exists(self):
        response = get_several_albums_invalid_range([
            '7qNY7C7rkJwioya4lKLrJt', '3K7m1TRRzyfQ3dav2JVgdj', '3aTuW4BtsyyyyQa9LKqj8n',
            '0NZQTozgPtlt5iN3hmANhy', '5lf8VH2121Ngg7AD3Ps8Ch', '0bhYU6Jz7XaXw9x67pSWTc',
            '01u9MdrytYwPidRT0uoCXR', '1cIdztckCGQOeGrou4xOG4', '4JTFvbBdQuXIafNDMuezO0',
            '679ytQ4HN7FspEGibjecXj', '1t3Z2hSfT1fm5iHHWC65xd', '128oy4BxWb3Tk4jsdwRdBq',
            '3HNnxK7NgLXbDoxRZxNWiR', '7MZzYkbHL9Tk3O6WeD4Z0Z', '4otkd9As6YaxxEkIjXPiZ6',
            '2DQhAbIgZG4QRy4mmQsFE0', '47BiFcV59TQi2s9SkBo2pb', '1kTlYbs28MXw7hwO0NLYif',
            '2cWBwpqMsDJC1ZUwz813lo', '4DZHSpFEwfDphP87KSH3jk', '3nTMdaxlWKNs9TPL64pNDr'
        ])
        assert "error" in response.json()

    def test_get_several_albums_rangeMaxInvalid_check_response_is_valid_json(self):
        response = get_several_albums_invalid_range([
            '7qNY7C7rkJwioya4lKLrJt', '3K7m1TRRzyfQ3dav2JVgdj', '3aTuW4BtsyyyyQa9LKqj8n',
            '0NZQTozgPtlt5iN3hmANhy', '5lf8VH2121Ngg7AD3Ps8Ch', '0bhYU6Jz7XaXw9x67pSWTc',
            '01u9MdrytYwPidRT0uoCXR', '1cIdztckCGQOeGrou4xOG4', '4JTFvbBdQuXIafNDMuezO0',
            '679ytQ4HN7FspEGibjecXj', '1t3Z2hSfT1fm5iHHWC65xd', '128oy4BxWb3Tk4jsdwRdBq',
            '3HNnxK7NgLXbDox', '7MZzYkbHL9Tk3O6WeD4Z0Z', '4otkd9As6YaxxEkIjXPiZ6',
            '2DQhAbIgZG4QRy4mmQsFE0', '47BiFcV59TQi2s9SkBo2pb', '1kTlYbs28MXw7hwO0NLYif',
            '2cWBwpqMsDJC1ZUwz813lo', '4DZHSpFEwfDphP87KSH3jk', '3nTMdaxlWKNs9TPL64pNDr'])

        assert "invalid id" in response.json()["error"]["message"]

    def test_get_several_albums_rangeMaxInvalid_response_time_is_less_than_200ms(self):
        response = get_several_albums_invalid_range([
            '7qNY7C7rkJwioya4lKLrJt', '3K7m1TRRzyfQ3dav2JVgdj', '3aTuW4BtsyyyyQa9LKqj8n',
            '0NZQTozgPtlt5iN3hmANhy', '5lf8VH2121Ngg7AD3Ps8Ch', '0bhYU6Jz7XaXw9x67pSWTc',
            '01u9MdrytYwPidRT0uoCXR', '1cIdztckCGQOeGrou4xOG4', '4JTFvbBdQuXIafNDMuezO0',
            '679ytQ4HN7FspEGibjecXj', '1t3Z2hSfT1fm5iHHWC65xd', '128oy4BxWb3Tk4jsdwRdBq',
            '3HNnxK7NgLXbDoxRZxNWiR', '7MZzYkbHL9Tk3O6WeD4Z0Z', '4otkd9As6YaxxEkIjXPiZ6',
            '2DQhAbIgZG4QRy4mmQsFE0', '47BiFcV59TQi2s9SkBo2pb', '1kTlYbs28MXw7hwO0NLYif',
            '2cWBwpqMsDJC1ZUwz813lo', '4DZHSpFEwfDphP87KSH3jk', '3nTMdaxlWKNs9TPL64pNDr'
        ])

        assert response.responseTime < 200



#SEVERAL ALBUMS Invalid range min. ids

    def test_get_several_albums_rangeMinInvalid_response_status_code_is_400(self):
        response = get_several_albums_invalid_range([""])
        assert response.status_code == 400

    def test_get_several_albums_rangeMinInvalid_response_contains_error_object(self):
        response = get_several_albums_invalid_range([""])
        assert "error" in response.json()

    def test_get_several_albums_rangeMinInvalid_error_message_is_invalid_id(self):
        response = get_several_albums_invalid_range([""])
        assert response.json() == {"error": {"message": "invalid id"}}

    def test_get_several_albums_rangeMinInvalid_error_status_is_400(self):
        response = get_several_albums_invalid_range([""])
        assert response.json()["error"]["status"] == 400

    def test_get_several_albums_rangeMinInvalid_error_message_exists(self):
        response = get_several_albums_invalid_range([""])
        assert response.json()["error"]["message"]

    def test_get_several_albums_rangeMinInvalid_error_message_is_a_string(self):
        response = get_several_albums_invalid_range([""])
        assert type(response.json()["error"]["message"]) == str

    def test_get_several_albums_rangeMinInvalid_error_contains_invalid_id(self):
        response = get_several_albums_invalid_range([""])
        assert "invalid id" in response.json()["error"]["message"]

    def test_get_several_albums_rangeMinInvalid_response_time_is_less_than_200ms(self):
        response = get_several_albums_invalid_range([""])
        assert response.responseTime < 500

    def test_get_several_albums_rangeMinInvalid_response_content_type_is_json(self):
        response = get_several_albums_invalid_range([""])
        assert response.headers["Content-Type"] == "application/json; charset=utf-8"
