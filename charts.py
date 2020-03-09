from datetime import datetime, timedelta

from pyecharts import options as opts
from pyecharts.charts import Bar, Line


def build_line_chart(title="Line-Chart",
                    xaxis=list(map(lambda x: datetime.now() + timedelta(x), range(0, 7))),
                    yaxis=[
                        ("商家A", [114, 55, 27, 101, 125, 27, 105]),
                        ("商家B", [57, 134, 137, 129, 145, 60, 49])],
                    position="right"
                   ):
    l = Line()
    l.add_xaxis(xaxis)
    for y in yaxis:
        l.add_yaxis(*y, markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max")]),)
    l.set_series_opts(label_opts=opts.LabelOpts(position=position))
    l.set_global_opts(title_opts=opts.TitleOpts(title=title))
    
    return l

def draw_line_chart(title="Line-Chart",
                    xaxis=list(map(lambda x: datetime.now() + timedelta(x), range(0, 7))),
                    yaxis=[
                        ("商家A", [114, 55, 27, 101, 125, 27, 105]),
                        ("商家B", [57, 134, 137, 129, 145, 60, 49])],
                    position="right"
                   ):
    return build_line_chart(title, xaxis, yaxis, position).render_notebook()


from aliyun import desc_it, result_mapper

@desc_it
def metric(instanceId, period=300, mname="CPUUtilization"):
    import cms as m
    r =  m.DescribeMetricListRequest()
    r.set_Namespace('acs_ecs_dashboard')
    r.set_MetricName(mname)
    r.set_Dimensions([{"instanceId": instanceId},])
    r.set_Period(period)
    return r


def build_cpu_chart(instance_id, period):
    # {'timestamp': 1583448900000,
    #  'userId': '1844184023992394',
    #  'instanceId': 'i-2zeblswgio3fz18ssvs7',
    #  'Minimum': 2.35,
    #  'Maximum': 2.46,
    #  'Average': 2.38}
    # dict_keys(['RequestId', 'Period', 'Datapoints', 'Code', 'Success'])
    # list(
    #                 map(
    #                     lambda x: (
    #                         x['Maximum'],
    #                         x['Average'],
    #                         x['Minimum'],
    #                         x['timestamp'],
    #                         x['instanceId']),
    #                     json.loads(metric(instanceId=x['InstanceId'])["Datapoints"])))
    import json
    xs = json.loads(
        metric(
            instance_id,
            period=period,
            mname="CPUUtilization"
        )['Datapoints']
    )

    a, x, y, z = list(
        map(lambda k: (k, list(map(lambda x: x[k], xs))),
            ['timestamp', 'Maximum', 'Average', 'Minimum']))
    return build_line_chart(
        title= 'CPU chart %s' % instance_id,
        xaxis=list(map(lambda x: datetime.fromtimestamp(x/1000), a[1])),
        yaxis=[x, y, z])

# show_cpu_chart('i-2ze99ni7tsf7pgz6y62e', period=120)
