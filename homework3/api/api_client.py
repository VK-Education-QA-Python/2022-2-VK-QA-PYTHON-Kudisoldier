from api.base_api import BaseApi
import uuid


class ApiClient(BaseApi):
    def login(self, email, password):
        data = {
            'email': email,
            'password': password,
            'continue': 'https://target-sandbox.my.com/auth/mycom?'
                        'state=target_login=1&ignore_opener=1#email',
            'failure': 'https://account.my.com/login/'
        }
        response = self._request('post', 'https://auth-ac.my.com/auth?lang=en&nosavelogin=0',
                                 data=data, headers={'referer': 'https://target-sandbox.my.com'})

        self._request('get', response.url)

    def get_csrf_token(self):
        return self.get_cookies('get', 'https://target-sandbox.my.com/csrf')['csrftoken']

    def get_client_id(self):
        response = self._request('get', 'https://target-sandbox.my.com/api/v2/user/session.json?fields=sudoers__id')
        client_id = response.json['sudoers'][0]['id']
        return client_id

    def get_packageid_pads(self):
        fields = 'fields=id,name,description,options'
        client_id = self.get_client_id()
        project_name = 'spec_specprojects'
        response = self._request('get', f'https://target-sandbox.my.com/api/v2/packages.json'
                                        f'?user_id={client_id}&{fields}')
        package = [i for i in response.json['items'] if i['name'] == project_name]  # find special projects
        pads = package[0]['options']['targetings'][1]['values']
        packageid = package[0]['id']
        return packageid, pads

    def get_url_id(self):
        url = 'https://vk.ru/testers'
        response = self._request('get', f'https://target-sandbox.my.com/api/v1/urls/?url={url}')

        return response.json['id']

    def create_campaign(self):
        packageid, pads = self.get_packageid_pads()
        url_id = self.get_url_id()
        campaing_name = str(uuid.uuid4())
        data = {"name": campaing_name, "read_only": False, "conversion_funnel_id": None, "objective": "special",
                "targetings": {"sex": ["male", "female"],
                               "age": {"age_list": list(range(20, 75)), "expand": True}, "pads": pads},
                "age_restrictions": None, "date_start": None, "date_end": None, "budget_limit_day": None,
                "budget_limit": None, "mixing": "fastest", "price": "0.01", "max_price": "0", "package_id": packageid,
                "banners": [{"textblocks": {"billboard_video": {"text": "F"}}, "urls": {"primary": {"id": url_id}},
                             "name": ""}]}
        response = self._request('post', 'https://target-sandbox.my.com/api/v2/campaigns.json',
                                 json=data, headers={'x-csrftoken': self.get_csrf_token()})

        return response.json, campaing_name

    def get_campaign(self, campaign_name):
        fields = 'id,name,delivery,price,budget_limit,budget_limit_day,pads_ots_limits,created,issues,' \
                 'prices,status,package_id,interface_read_only,read_only,objective,user_id,' \
                 'targetings__split_audience,targetings__pads,enable_utm,utm,age_restrictions,' \
                 'package_priced_event_type,autobidding_mode,pricelist_id&sorting=-id&limit=100&offset=0' \
                 '&_status__in=active&_user_id__in=' + str(self.get_client_id())
        response = self._request('get', f'https://target-sandbox.my.com/api/v2/campaigns.json?fields={fields}')

        return [i['id'] for i in response.json['items'] if i['name'] == campaign_name]

    def delete_campaign(self, campaign_id):
        data = [{"id": campaign_id, "status": "deleted"}]
        self._request('post', f'https://target-sandbox.my.com/api/v2/campaigns/mass_action.json',
                      json=data, headers={'x-csrftoken': self.get_csrf_token()})

    def create_segment(self):
        fields = 'relations__object_type,relations__object_id,relations__params,relations__params__score,' \
                 'relations__id,relations_count,id,name,pass_condition,created,campaign_ids,users,flags'
        segment_name = str(uuid.uuid4())
        data = {"name": segment_name, "pass_condition": 1, "relations": [
            {"object_type": "remarketing_player", "params": {"type": "positive", "left": 365, "right": 0}}],
                "logicType": "or"}
        response = self._request('post', f'https://target-sandbox.my.com/api/v2/remarketing/segments.json'
                                         f'?fields={fields}', json=data, headers={'x-csrftoken': self.get_csrf_token()})
        return response.json, segment_name

    def get_segment(self, segment_name):
        fields = 'relations__object_type,relations__object_id,relations__params,relations__params__score,' \
                 'relations__id,relations_count,id,name,pass_condition,created,campaign_ids,users,' \
                 'flags&limit=500'
        response = self._request('get', f'https://target-sandbox.my.com/api/v2/remarketing/segments.json'
                                        f'?fields={fields}')
        return [i['id'] for i in response.json['items'] if i['name'] == segment_name]

    def delete_segment(self, segment_id):
        data = [{"source_id": segment_id, "source_type": "segment"}]
        self._request('post', 'https://target-sandbox.my.com/api/v1/remarketing/mass_action/delete.json',
                      json=data, headers={'x-csrftoken': self.get_csrf_token()})

    def create_audience_vk(self):
        vkgroup = 'https://vk.ru/vkedu'
        response = self._request('get', f'https://target-sandbox.my.com/api/v2/vk_groups.json?_q={vkgroup}')
        group_id = response.json['items'][0]['id']

        data = {"items": [{"object_id": group_id}]}
        self._request('post', 'https://target-sandbox.my.com/api/v2/remarketing/vk_groups/bulk.json'
                              '?fields=id,object_id,name,users_count,url', json=data,
                      headers={'x-csrftoken': self.get_csrf_token()})

    def get_audience_vk(self):
        vkgroup_name = 'VK Образование'
        response = self._request('get', 'https://target-sandbox.my.com/api/v2/remarketing/vk_groups.json'
                                        '?fields=id,object_id,name,users_count,url&limit=50')
        return [[i['id'], i['object_id']] for i in response.json['items'] if i['name'] == vkgroup_name]

    def delete_audience_vk(self, vkgroup_id):
        self._request('delete', f'https://target-sandbox.my.com/api/v2/remarketing/vk_groups/{vkgroup_id}.json',
                      headers={'x-csrftoken': self.get_csrf_token()})

    def create_segment_vkgorup(self, object_id):
        segment_name = str(uuid.uuid4())
        data = {"name": segment_name, "pass_condition": 1, "relations": [
            {"object_type": "remarketing_vk_group", "params": {"source_id": object_id, "type": "positive"}}],
                "logicType": "or"}
        fields = 'relations__object_type,relations__object_id,relations__params,relations__params__score,' \
                 'relations__id,relations_count,id,name,pass_condition,created,campaign_ids,users,flags'
        response = self._request('post', f'https://target-sandbox.my.com/api/v2/remarketing/segments.json'
                                         f'?fields={fields}', json=data, headers={'x-csrftoken': self.get_csrf_token()})
        return response.json, segment_name
