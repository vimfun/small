from aliyun import client

from aliyunsdkecs.request.v20140526.DescribeInstancesRequest import DescribeInstancesRequest

def desc_ECS_insts():
    request = DescribeInstancesRequest()
    request.set_accept_format('json')

    response = client.do_action_with_exception(request)
    print(str(response, encoding='utf-8'))
