from flask import Flask, render_template

app = Flask(__name__)

@app.route('/plot')
def plot():
    from pandas_datareader import data
    import datetime
    from bokeh.plotting import output_file, show, figure
    from bokeh.embed import components
    from bokeh.resources import CDN

    start = datetime.datetime(2019, 11, 2)
    end = datetime.datetime(2020, 11, 13)
    df = data.DataReader(name = "AAPL", data_source = "yahoo", start = start, end = end)

    df.index[df.Close > df.Open]

    #assigning the bokeh figure and title to the plot
    p = figure(x_axis_type = 'datetime', width = 1000, height = 300, sizing_mode = 'stretch_both')
    p.title.text = "Candlestick Chart"

    p.segment(df.index, df.High, df.index, df.Low, color = "Black")

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

    hour_12 = 12*60*60*1000
    p.rect(df.index[df["Status"] == "increase"], df.Middle[df.Status == "increase"], hour_12,
    df.Height[df.Status == "increase"], fill_color = "#00FF7F", line_color = "black")
    p.rect(df.index[df["Status"] == "decrease"], df.Middle[df.Status == "decrease"], hour_12,
    df.Height[df.Status == "decrease"], fill_color = "#DC143C", line_color = "black")

    p.grid.grid_line_alpha = 0.3

    script1, div1 = components(p)
    cdn_js = CDN.js_files[0]
    return render_template("plot.html",
    script1 = script1,
    div1 = div1,
    cdn_js = cdn_js)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about/')
def about():
    return render_template("about.html")
if __name__ =="__main__":
    app.run(debug=False)
