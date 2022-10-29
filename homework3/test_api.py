import pytest


@pytest.mark.API
def test_campaign(client):
    result, campaign_name = client.create_campaign()
    assert isinstance(result, dict)
    assert result.get('id')
    campaign_id = client.get_campaign(campaign_name)[0]
    client.delete_campaign(campaign_id)
    assert not client.get_campaign(campaign_name)  # check is list empty and we deleted campaign


@pytest.mark.API
def test_segment_games(client):
    result, segment_name = client.create_segment()
    assert isinstance(result, dict)
    assert result.get('id')
    segment_id = client.get_segment(segment_name)[0]
    client.delete_segment(segment_id)
    assert not client.get_segment(segment_name)


@pytest.mark.API
def test_segment_vk_ok(client):
    client.create_audience_vk()
    vkgroup_id, object_id = client.get_audience_vk()[0]
    result, segment_name = client.create_segment_vkgorup(object_id)
    assert isinstance(result, dict)
    assert result.get('id')
    segment_id = client.get_segment(segment_name)[0]
    client.delete_segment(segment_id)
    client.delete_audience_vk(vkgroup_id)
    assert not client.get_segment(segment_name)
    assert not client.get_audience_vk()
