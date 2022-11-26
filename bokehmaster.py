import numpy as np
from bokeh.plotting import figure,show,output_file
from bokeh.simpledata.stocks import AAPL,GOOG,IBM,MSFT
def datetimex():
    return np.array(x,datatype = np.datetime64)
p = figure(x_axis_type = "Datatypes",title = "Stocks Prices Of Multi National Comapany")
p.gid.grid_line_alpha = 0.3
p.xaxis.axis_label = 'Date'
p.yaxis.axis_label = 'Price'

p.line(datetime(AAPL['Date']),AAPL['adj.close'], color = '#AGCEE3',legend = 'AAPL' )
p.line(datetime(GOOG['Date']),GOOG['adj.close'], color = '#A52A2A',legend = 'GOOG' )
p.line(datetime(IBM['Date']),IBM['adj.close'], color = '#FF83FA',legend = 'IBM' )
p.line(datetime(MSFT['Date']),MSFT['adj.close'], color = '#CDCD00',legend = 'MSFT' )

P.legend.location = 'top_left'

output_file("Stocks.html",title = "Stocks Compasrison")
show(p)