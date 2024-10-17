from face_det import df
from bokeh.plotting import figure, output_file, show
from bokeh.models import HoverTool, ColumnDataSource

df["Start_string"] = df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["End_string"] = df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")

cds = ColumnDataSource(df)

f = figure(width = 500, height = 100, x_axis_type = 'datetime', sizing_mode = "scale_both", title = "Motion Graph")
f.yaxis.minor_tick_line_color = "pink"
f.yaxis[0].ticker.desired_num_ticks = 1

hover = HoverTool(tooltips = [("Start", "@Start_string"), ("End", "@End_string")])
f.add_tools(hover)

f.quad(left = "Start", right = "End", bottom = 0, top = 1, color = "green", source = cds)

output_file("Graph.html")
show(f)