from itertools import groupby
import json

from aliyun import desc_it, result_mapper

from aliyunsdkcms.request.v20190101.AddTagsRequest import AddTagsRequest
from aliyunsdkcms.request.v20190101.ApplyMetricRuleTemplateRequest import ApplyMetricRuleTemplateRequest
from aliyunsdkcms.request.v20190101.CreateDynamicTagGroupRequest import CreateDynamicTagGroupRequest
from aliyunsdkcms.request.v20190101.CreateGroupMetricRulesRequest import CreateGroupMetricRulesRequest
from aliyunsdkcms.request.v20190101.CreateGroupMonitoringAgentProcessRequest import CreateGroupMonitoringAgentProcessRequest
from aliyunsdkcms.request.v20190101.CreateHostAvailabilityRequest import CreateHostAvailabilityRequest
from aliyunsdkcms.request.v20190101.CreateMetricRuleResourcesRequest import CreateMetricRuleResourcesRequest
from aliyunsdkcms.request.v20190101.CreateMetricRuleTemplateRequest import CreateMetricRuleTemplateRequest
from aliyunsdkcms.request.v20190101.CreateMonitorAgentProcessRequest import CreateMonitorAgentProcessRequest
from aliyunsdkcms.request.v20190101.CreateMonitorGroupInstancesRequest import CreateMonitorGroupInstancesRequest
from aliyunsdkcms.request.v20190101.CreateMonitorGroupNotifyPolicyRequest import CreateMonitorGroupNotifyPolicyRequest
from aliyunsdkcms.request.v20190101.CreateMonitorGroupRequest import CreateMonitorGroupRequest
from aliyunsdkcms.request.v20190101.CreateMonitoringAgentProcessRequest import CreateMonitoringAgentProcessRequest
from aliyunsdkcms.request.v20190101.CreateSiteMonitorRequest import CreateSiteMonitorRequest
from aliyunsdkcms.request.v20190101.DeleteContactGroupRequest import DeleteContactGroupRequest
from aliyunsdkcms.request.v20190101.DeleteContactRequest import DeleteContactRequest
from aliyunsdkcms.request.v20190101.DeleteCustomMetricRequest import DeleteCustomMetricRequest
from aliyunsdkcms.request.v20190101.DeleteDynamicTagGroupRequest import DeleteDynamicTagGroupRequest
from aliyunsdkcms.request.v20190101.DeleteEventRuleTargetsRequest import DeleteEventRuleTargetsRequest
from aliyunsdkcms.request.v20190101.DeleteEventRulesRequest import DeleteEventRulesRequest
from aliyunsdkcms.request.v20190101.DeleteGroupMonitoringAgentProcessRequest import DeleteGroupMonitoringAgentProcessRequest
from aliyunsdkcms.request.v20190101.DeleteHostAvailabilityRequest import DeleteHostAvailabilityRequest
from aliyunsdkcms.request.v20190101.DeleteMetricRuleResourcesRequest import DeleteMetricRuleResourcesRequest
from aliyunsdkcms.request.v20190101.DeleteMetricRuleTargetsRequest import DeleteMetricRuleTargetsRequest
from aliyunsdkcms.request.v20190101.DeleteMetricRuleTemplateRequest import DeleteMetricRuleTemplateRequest
from aliyunsdkcms.request.v20190101.DeleteMetricRulesRequest import DeleteMetricRulesRequest
from aliyunsdkcms.request.v20190101.DeleteMonitorGroupDynamicRuleRequest import DeleteMonitorGroupDynamicRuleRequest
from aliyunsdkcms.request.v20190101.DeleteMonitorGroupInstancesRequest import DeleteMonitorGroupInstancesRequest
from aliyunsdkcms.request.v20190101.DeleteMonitorGroupNotifyPolicyRequest import DeleteMonitorGroupNotifyPolicyRequest
from aliyunsdkcms.request.v20190101.DeleteMonitorGroupRequest import DeleteMonitorGroupRequest
from aliyunsdkcms.request.v20190101.DeleteMonitoringAgentProcessRequest import DeleteMonitoringAgentProcessRequest
from aliyunsdkcms.request.v20190101.DeleteSiteMonitorsRequest import DeleteSiteMonitorsRequest
from aliyunsdkcms.request.v20190101.DescribeActiveMetricRuleListRequest import DescribeActiveMetricRuleListRequest
from aliyunsdkcms.request.v20190101.DescribeAlertHistoryListRequest import DescribeAlertHistoryListRequest
from aliyunsdkcms.request.v20190101.DescribeAlertingMetricRuleResourcesRequest import DescribeAlertingMetricRuleResourcesRequest
from aliyunsdkcms.request.v20190101.DescribeContactGroupListRequest import DescribeContactGroupListRequest
from aliyunsdkcms.request.v20190101.DescribeContactListByContactGroupRequest import DescribeContactListByContactGroupRequest
from aliyunsdkcms.request.v20190101.DescribeContactListRequest import DescribeContactListRequest
from aliyunsdkcms.request.v20190101.DescribeCustomEventAttributeRequest import DescribeCustomEventAttributeRequest
from aliyunsdkcms.request.v20190101.DescribeCustomEventCountRequest import DescribeCustomEventCountRequest
from aliyunsdkcms.request.v20190101.DescribeCustomEventHistogramRequest import DescribeCustomEventHistogramRequest
from aliyunsdkcms.request.v20190101.DescribeCustomMetricListRequest import DescribeCustomMetricListRequest
from aliyunsdkcms.request.v20190101.DescribeDynamicTagRuleListRequest import DescribeDynamicTagRuleListRequest
from aliyunsdkcms.request.v20190101.DescribeEventRuleAttributeRequest import DescribeEventRuleAttributeRequest
from aliyunsdkcms.request.v20190101.DescribeEventRuleListRequest import DescribeEventRuleListRequest
from aliyunsdkcms.request.v20190101.DescribeEventRuleTargetListRequest import DescribeEventRuleTargetListRequest
from aliyunsdkcms.request.v20190101.DescribeGroupMonitoringAgentProcessRequest import DescribeGroupMonitoringAgentProcessRequest
from aliyunsdkcms.request.v20190101.DescribeHostAvailabilityListRequest import DescribeHostAvailabilityListRequest
from aliyunsdkcms.request.v20190101.DescribeMetricDataRequest import DescribeMetricDataRequest
from aliyunsdkcms.request.v20190101.DescribeMetricLastRequest import DescribeMetricLastRequest
from aliyunsdkcms.request.v20190101.DescribeMetricListRequest import DescribeMetricListRequest
from aliyunsdkcms.request.v20190101.DescribeMetricMetaListRequest import DescribeMetricMetaListRequest
from aliyunsdkcms.request.v20190101.DescribeMetricRuleCountRequest import DescribeMetricRuleCountRequest
from aliyunsdkcms.request.v20190101.DescribeMetricRuleListRequest import DescribeMetricRuleListRequest
from aliyunsdkcms.request.v20190101.DescribeMetricRuleTargetsRequest import DescribeMetricRuleTargetsRequest
from aliyunsdkcms.request.v20190101.DescribeMetricRuleTemplateAttributeRequest import DescribeMetricRuleTemplateAttributeRequest
from aliyunsdkcms.request.v20190101.DescribeMetricRuleTemplateListRequest import DescribeMetricRuleTemplateListRequest
from aliyunsdkcms.request.v20190101.DescribeMetricTopRequest import DescribeMetricTopRequest
from aliyunsdkcms.request.v20190101.DescribeMonitorGroupCategoriesRequest import DescribeMonitorGroupCategoriesRequest
from aliyunsdkcms.request.v20190101.DescribeMonitorGroupDynamicRulesRequest import DescribeMonitorGroupDynamicRulesRequest
from aliyunsdkcms.request.v20190101.DescribeMonitorGroupInstanceAttributeRequest import DescribeMonitorGroupInstanceAttributeRequest
from aliyunsdkcms.request.v20190101.DescribeMonitorGroupInstancesRequest import DescribeMonitorGroupInstancesRequest
from aliyunsdkcms.request.v20190101.DescribeMonitorGroupNotifyPolicyListRequest import DescribeMonitorGroupNotifyPolicyListRequest
from aliyunsdkcms.request.v20190101.DescribeMonitorGroupsRequest import DescribeMonitorGroupsRequest
from aliyunsdkcms.request.v20190101.DescribeMonitoringAgentAccessKeyRequest import DescribeMonitoringAgentAccessKeyRequest
from aliyunsdkcms.request.v20190101.DescribeMonitoringAgentConfigRequest import DescribeMonitoringAgentConfigRequest
from aliyunsdkcms.request.v20190101.DescribeMonitoringAgentHostsRequest import DescribeMonitoringAgentHostsRequest
from aliyunsdkcms.request.v20190101.DescribeMonitoringAgentProcessesRequest import DescribeMonitoringAgentProcessesRequest
from aliyunsdkcms.request.v20190101.DescribeMonitoringAgentStatusesRequest import DescribeMonitoringAgentStatusesRequest
from aliyunsdkcms.request.v20190101.DescribeMonitoringConfigRequest import DescribeMonitoringConfigRequest
from aliyunsdkcms.request.v20190101.DescribeProductResourceTagKeyListRequest import DescribeProductResourceTagKeyListRequest
from aliyunsdkcms.request.v20190101.DescribeProductsOfActiveMetricRuleRequest import DescribeProductsOfActiveMetricRuleRequest
from aliyunsdkcms.request.v20190101.DescribeProjectMetaRequest import DescribeProjectMetaRequest
from aliyunsdkcms.request.v20190101.DescribeSiteMonitorAttributeRequest import DescribeSiteMonitorAttributeRequest
from aliyunsdkcms.request.v20190101.DescribeSiteMonitorDataRequest import DescribeSiteMonitorDataRequest
from aliyunsdkcms.request.v20190101.DescribeSiteMonitorISPCityListRequest import DescribeSiteMonitorISPCityListRequest
from aliyunsdkcms.request.v20190101.DescribeSiteMonitorListRequest import DescribeSiteMonitorListRequest
from aliyunsdkcms.request.v20190101.DescribeSiteMonitorQuotaRequest import DescribeSiteMonitorQuotaRequest
from aliyunsdkcms.request.v20190101.DescribeSiteMonitorStatisticsRequest import DescribeSiteMonitorStatisticsRequest
from aliyunsdkcms.request.v20190101.DescribeSystemEventAttributeRequest import DescribeSystemEventAttributeRequest
from aliyunsdkcms.request.v20190101.DescribeSystemEventCountRequest import DescribeSystemEventCountRequest
from aliyunsdkcms.request.v20190101.DescribeSystemEventHistogramRequest import DescribeSystemEventHistogramRequest
from aliyunsdkcms.request.v20190101.DescribeSystemEventMetaListRequest import DescribeSystemEventMetaListRequest
from aliyunsdkcms.request.v20190101.DescribeTagKeyListRequest import DescribeTagKeyListRequest
from aliyunsdkcms.request.v20190101.DescribeTagValueListRequest import DescribeTagValueListRequest
from aliyunsdkcms.request.v20190101.DescribeUnhealthyHostAvailabilityRequest import DescribeUnhealthyHostAvailabilityRequest
from aliyunsdkcms.request.v20190101.DisableActiveMetricRuleRequest import DisableActiveMetricRuleRequest
from aliyunsdkcms.request.v20190101.DisableEventRulesRequest import DisableEventRulesRequest
from aliyunsdkcms.request.v20190101.DisableHostAvailabilityRequest import DisableHostAvailabilityRequest
from aliyunsdkcms.request.v20190101.DisableMetricRulesRequest import DisableMetricRulesRequest
from aliyunsdkcms.request.v20190101.DisableSiteMonitorsRequest import DisableSiteMonitorsRequest
from aliyunsdkcms.request.v20190101.EnableActiveMetricRuleRequest import EnableActiveMetricRuleRequest
from aliyunsdkcms.request.v20190101.EnableEventRulesRequest import EnableEventRulesRequest
from aliyunsdkcms.request.v20190101.EnableHostAvailabilityRequest import EnableHostAvailabilityRequest
from aliyunsdkcms.request.v20190101.EnableMetricRulesRequest import EnableMetricRulesRequest
from aliyunsdkcms.request.v20190101.EnableSiteMonitorsRequest import EnableSiteMonitorsRequest
from aliyunsdkcms.request.v20190101.InstallMonitoringAgentRequest import InstallMonitoringAgentRequest
from aliyunsdkcms.request.v20190101.ModifyGroupMonitoringAgentProcessRequest import ModifyGroupMonitoringAgentProcessRequest
from aliyunsdkcms.request.v20190101.ModifyHostAvailabilityRequest import ModifyHostAvailabilityRequest
from aliyunsdkcms.request.v20190101.ModifyMetricRuleTemplateRequest import ModifyMetricRuleTemplateRequest
from aliyunsdkcms.request.v20190101.ModifyMonitorGroupInstancesRequest import ModifyMonitorGroupInstancesRequest
from aliyunsdkcms.request.v20190101.ModifyMonitorGroupRequest import ModifyMonitorGroupRequest
from aliyunsdkcms.request.v20190101.ModifySiteMonitorRequest import ModifySiteMonitorRequest
from aliyunsdkcms.request.v20190101.PutContactGroupRequest import PutContactGroupRequest
from aliyunsdkcms.request.v20190101.PutContactRequest import PutContactRequest
from aliyunsdkcms.request.v20190101.PutCustomEventRequest import PutCustomEventRequest
from aliyunsdkcms.request.v20190101.PutCustomMetricRequest import PutCustomMetricRequest
from aliyunsdkcms.request.v20190101.PutEventRuleRequest import PutEventRuleRequest
from aliyunsdkcms.request.v20190101.PutEventRuleTargetsRequest import PutEventRuleTargetsRequest
from aliyunsdkcms.request.v20190101.PutGroupMetricRuleRequest import PutGroupMetricRuleRequest
from aliyunsdkcms.request.v20190101.PutMetricRuleTargetsRequest import PutMetricRuleTargetsRequest
from aliyunsdkcms.request.v20190101.PutMonitorGroupDynamicRuleRequest import PutMonitorGroupDynamicRuleRequest
from aliyunsdkcms.request.v20190101.PutMonitoringConfigRequest import PutMonitoringConfigRequest
from aliyunsdkcms.request.v20190101.PutResourceMetricRuleRequest import PutResourceMetricRuleRequest
from aliyunsdkcms.request.v20190101.PutResourceMetricRulesRequest import PutResourceMetricRulesRequest
from aliyunsdkcms.request.v20190101.RemoveTagsRequest import RemoveTagsRequest
from aliyunsdkcms.request.v20190101.SendDryRunSystemEventRequest import SendDryRunSystemEventRequest
from aliyunsdkcms.request.v20190101.UninstallMonitoringAgentRequest import UninstallMonitoringAgentRequest


@desc_it
def metric(instance_ids, period=300, name="CPUUtilization"):
    r =  DescribeMetricListRequest()
    r.set_Namespace('acs_ecs_dashboard')
    r.set_MetricName(name)
    r.set_Dimensions([{"instanceId": iid} for iid in instance_ids])
    r.set_Period(period)
    return r

def get_metric_infos(instance_ids, name='CPUUtilization', top_n=1, period=60):
    ds = map(
            lambda x: _get_metric_infos(instance_ids[x[0]*50:x[1]*50], top_n=top_n, period=period, name=name),
            zip(
                range(len(instance_ids)//50 + 1),
                range(1, len(instance_ids)//50 + 2)))

    res = {}
    for d in ds:
        res.update(d)

    return res


def _get_metric_infos(instance_ids, name='memory_usedutilization', top_n=1, period=60):
    # dp = metric(instance_ids=instance_ids, period=period)
    # import pdb; pdb.set_trace()
    datapoints = json.loads(
        metric(instance_ids=instance_ids, name=name, period=period)["Datapoints"]
    )

    key = lambda x: x['instanceId']
    def handle_one_instance_metric(x):
        iid, xs = x
        return (iid, sorted(list(xs), key=lambda x: x['Maximum'])[-top_n:])

    return dict(
        map(
            handle_one_instance_metric, 
            groupby(
                sorted(datapoints, key=key),
                key=key,
            )))


if __name__ == '__main__':
    import sys
    instance_id = sys.argv[1]
    metric_name = sys.argv[2]
    # print(get_metric_infos([instance_id], name='memory_usedutilization')[instance_id][0]['Maximum'])
    res = get_metric_infos([instance_id], name=metric_name)

    value = -1 if len(res) == 0 else res[instance_id][0]['Maximum']

    print(value)

    print(get_metric_infos([instance_id], name='memory_usedutilization'))
    print(get_metric_infos([instance_id], name='cpu_idle'))
    print(get_metric_infos([instance_id], name='CPUUtilization'))
