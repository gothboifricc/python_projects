from pandas_datareader import data
import datetime
from bokeh.plotting import output_file, show, figure
#to generate the html and script of bokeh chart
from bokeh.embed import components
#to generate the css and jscript of bokeh chart
from bokeh.resources import CDN #CDn stands for Content Delivery Network

#setting the start date and the end date using the datetime module
start = datetime.datetime(2019, 11, 2)
end = datetime.datetime(2020, 11, 13)
#accessing the data reader method/class of the data library
df = data.DataReader(name = "AAPL", data_source = "yahoo", start = start, end = end)
#just change the stock symbol to access other stock data
df.to_csv("apple.csv")
#print(df)

#grabbing the bullish/ bearish candles
df.index[df.Close > df.Open]

#assigning the bokeh figure and title to the plot
p = figure(x_axis_type = 'datetime', width = 1000, height = 300, sizing_mode = 'stretch_both')
p.title.text = "Candlestick Chart"

#Plotting the wicks of the candles
p.segment(df.index, df.High, df.index, df.Low, color = "Black")

#watch lecture 258 for a more detailed explanation
def inc_dec(c, o):
    if c > o:
        value = "increase"
    elif c < o:
        value = "decrease"
    else:
        value = "equal"
    return value

df["Middle"] = (df.Open + df.Close)/2
df["Status"] = [inc_dec(c, o) for c, o in zip(df.Close, df.Open)]
df["Height"] = abs(df.Open - df.Close)

#p.rect(xaxis coord, yaxis coord, width, height etc.)
hour_12 = 12*60*60*1000
p.rect(df.index[df["Status"] == "increase"], df.Middle[df.Status == "increase"], hour_12,
 df.Height[df.Status == "increase"], fill_color = "#00FF7F", line_color = "black")
p.rect(df.index[df["Status"] == "decrease"], df.Middle[df.Status == "decrease"], hour_12,
 df.Height[df.Status == "decrease"], fill_color = "#DC143C", line_color = "black")

#setting the transparency of the background gridlines
p.grid.grid_line_alpha = 0.3

#print(df)
output_file("CS.html")
show(p)
#script1, div1 = components(p)
#cdn_js = CDN.js_files

#As of Bokeh 1.3.4, you are no longer required to get the CSS files from bokeh.resources.
#cdn_css = CDN.css_files

#print(cdn_js[0])