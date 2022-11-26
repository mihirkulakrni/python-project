import bokeh
E:\ɱĨɧĨ₨folder$$¥₨😎😎😈\python\programsE:\ɱĨɧĨ₨folder$$¥₨😎😎😈\python\programsfrom bokeh.plotting import figure, output_file, show

x = [10,20,30,40,50,60,70,80,90]
y = [11,12,13,14,15,16,17,18,19]
output_file('line.html')
p = figure(title = "basic line plots", x_axis_label = 'X axis',y_axis_label = 'Y axis')
p.line(x, y, legend = "Price", line_width = 3)
show(p)
