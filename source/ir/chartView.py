#!/usr/bin/python
# -*- coding: utf-8 -*-
#this function use pyChart package for creating charts of program
# This line imports all the chart modules.
#from numarray import *
def createChart():
#    import sys
#    sys.path.append('g:\\pychart-1.33')
    from pychart import *
    #theme.get_options()
    theme.output_format='pdf'
    theme.output_file='g:\\waq.pdf'
    theme.default_font_family='Times'

    # We have 10 sample points total.  The first value in each tuple is
    # the X value, and subsequent values are Y values for different lines.
    '''
    data = [(10, 20, 30), (20, 65, 33),
            (30, 55, 30), (40, 45, 51),
            (50, 25, 27), (60, 75, 30),
            (70, 80, 42), (80, 62, 32),
            (90, 42, 39), (100, 32, 39)]
    '''
    data = [(0.1, .20, .30), (.20, .65, .33),
            (.30, .55, .30), (.40, .45, .51),
            (.50, .25, .27), (.60, .75, .30),
            (.70, .80, .42), (.80, .62, .32),
            (.90, .42, .39), (1, .32, .39)]

    # The format attribute specifies the text to be drawn at each tick mark.
    # Here, texts are rotated -60 degrees ("/a-60"), left-aligned ("/hL"),
    # and numbers are printed as integers ("%d"). 
    xaxis = axis.X(format="/a-60/hL%1.2f", tic_interval = .1, label="Sthhuff")
    yaxis = axis.Y(tic_interval = .1, label="Valuehh")

    # Define the drawing area. "y_range=(0,None)" tells that the Y minimum
    # is 0, but the Y maximum is to be computed automatically. Without
    # y_ranges, Pychart will pick the minimum Y value among the samples,
    # i.e., 20, as the base value of Y axis.
    ar = area.T(x_axis=xaxis, y_axis=yaxis, y_range=(0,1.1) , x_range=(0,1.1))

    # The first plot extracts Y values from the 2nd column
    # ("ycol=1") of DATA ("data=data"). X values are takes from the first
    # column, which is the default.
    plot = line_plot.T(label="foo", data=data, ycol=1, tick_mark=tick_mark.star)
    plot2 = line_plot.T(label="bar", data=data, ycol=2, tick_mark=tick_mark.square)

    ar.add_plot(plot, plot2)

    # The call to ar.draw() usually comes at the end of a program.  It
    # draws the axes, the plots, and the legend (if any).
    ar.draw()


createChart()
print 'dsfds'
