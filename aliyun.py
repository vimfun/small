from aliyunsdkcore.client import AcsClient
import json

from config import ACS_KEY, ACS_SECRET, REGION_ID

client = AcsClient(ACS_KEY, ACS_SECRET, REGION_ID)

def desc_it(func):
    from functools import wraps

    @wraps(func)
    def _(*args, **kwargs):
        request = func(*args, **kwargs)
        response = client.do_action_with_exception(request)
        # print(str(response, encoding='utf-8'))
        return json.loads(response)
    return _
