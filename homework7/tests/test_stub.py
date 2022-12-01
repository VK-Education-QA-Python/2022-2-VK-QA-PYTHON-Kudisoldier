def test_age(stub_client):
    age = stub_client.get_age('test')

    assert isinstance(age, int)
    assert 18 <= age <= 105
