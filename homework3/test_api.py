import pytest


@pytest.mark.API
def test_api(client):
    result, campaign_name = client.create_campaign()
    assert isinstance(result, dict)
    assert result.get('id')
    campaign_id = client.get_campaign(campaign_name)[0]
    client.delete_campaign(campaign_id)
    assert not client.get_campaign(campaign_name)  # check is list empty and we deleted campaign



