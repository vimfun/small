import json
from functools import wraps

from aliyunsdkcore.client import AcsClient
from config import ACS_KEY, ACS_SECRET, REGION_ID

client = AcsClient(ACS_KEY, ACS_SECRET, REGION_ID)


def desc_it(func):
    @wraps(func)
    def _(*args, **kwargs):
        request = func(*args, **kwargs)
        response = client.do_action_with_exception(request)
        # print(str(response, encoding='utf-8'))
        return json.loads(response)
    return _


def result_keys(ksxs):
    def dec(func):
        @wraps(func)
        def _(*args, **kwargs):
            resp = func(*args, **kwargs)

            resxs = []
            for i, _ks in enumerate(ksxs):
                tmp_resp = resp
                ks, default = _ks
                for k in ks:
                    tmp_resp = tmp_resp.get(k, default)
                    if tmp_resp is default:
                        break
                resxs[i] = tmp_resp
            return resxs
        return _
    return dec


def result_mapper(mapper_func):
    def dec(func):
        @wraps(func)
        def _(*args, **kwargs):
            resp = func(*args, **kwargs)
            return mapper_func(resp)
        return _
    return dec
