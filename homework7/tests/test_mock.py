def test_mock_add(mock_client):
    res = mock_client.add_surname('test_mock', 'mock_surname')
    assert res == 'success'
    res = mock_client.get_surname('test_mock')
    assert res == 'mock_surname'


def test_mock_delete(mock_client):
    res = mock_client.add_surname('test_delete', 'mock_surname')
    assert res == 'success'
    res = mock_client.get_surname('test_delete')
    assert res == 'mock_surname'
    res = mock_client.delete_surname('test_delete')
    assert res == 'success'
    res = mock_client.get_surname('test_delete')
    assert res != 'mock_surname'


def test_delete_nonexistent(mock_client):
    res = mock_client.delete_surname('nonexistent')
    assert res == 'surname doesnt exist'
