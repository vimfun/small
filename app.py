from random import randrange

from flask.json import jsonify
from flask import Flask, render_template, request
from jinja2 import Markup, Environment, FileSystemLoader

from pyecharts import options as opts
from pyecharts.charts import Bar, Line
from pyecharts.globals import CurrentConfig


CurrentConfig.GLOBAL_ENV = Environment(loader=FileSystemLoader("./templates"))

app = Flask(__name__, static_folder="templates")


def line_base(): # -> Line:
    line = (
        Line()
        .add_xaxis(["{}".format(i) for i in range(10)])
        .add_yaxis(
            series_name="",
            y_axis=[randrange(50, 80) for _ in range(10)],
            is_smooth=True,
            label_opts=opts.LabelOpts(is_show=False),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="动态数据"),
            xaxis_opts=opts.AxisOpts(type_="value"),
            yaxis_opts=opts.AxisOpts(type_="value"),
        )
    )
    return line


@app.route("/")
def index():
    return render_template("index.html")
    # from charts import build_cpu_chart
    # c = build_cpu_chart('i-2ze99ni7tsf7pgz6y62e', period=120)
    # return Markup(c.render_embed())


# @app.route("/lineChart")
@app.route("/instanceChart")
def get_line_chart():
    c = line_base()
    return c.dump_options_with_quotes()

# @app.route("/instanceChart")
@app.route("/lineChart")
def get_instance_chart():
    from charts import build_cpu_chart
    instanceId = request.args['machineIdOrIp']
    instanceName = request.args['instanceName']
    c = build_cpu_chart(instanceId, instanceName, period=300)
    return c.dump_options_with_quotes()


@app.route("/aliyun/ecs/instances")
def get_aliyun_ecs_instances():
    import ecs
    return jsonify(ecs.get_instances())

if __name__ == "__main__":
    app.run()
