# Exercise 3
# Create a visualization with interactivity. Similar to Exercise 2,
# you can decide what you want to use as data and
# chart type.
# Exercise 2
# Create another visualization of your choice of data and chart type.
# You can use pandas to help loading data, or just hard-coded the data is fine.

# -*- coding: utf-8 -*-
import json
import dash
import dash_core_components as dcc
import dash_html_components as html
import json
from textwrap import dedent as d
from dash.dependencies import Input, Output

# static data
months = ['March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December', 'January', 'February']
total_users = [27, 16, 20, 28, 26, 19, 53, 41, 38, 43, 31, 35]
usa_users = [15, 11, 10, 15, 20, 13, 24, 25, 30, 35, 23, 27]
uk_users = [6, 0, 2, 3, 1, 2, 7, 4, 1, 1, 3, 1]
germany_users = [1, 1, 0, 0, 2, 1, 4, 3, 1, 2, 1, 2]
canada_users = [0, 1, 3, 2, 0, 0, 8, 0, 1, 0, 1, 0]
australia_users = [0, 0, 0, 0, 0, 0, 1, 3, 0, 1, 1, 1]

# TODO: working on this file to add more codes...

# initialize Dash environment
app = dash.Dash(__name__)

styles = {
    'pre': {
        'border': 'thin lightgrey solid',
        'overflowX': 'scroll'
    }
}

# set up an layout
app.layout = html.Div(children=[
    # H1 title on the page
    html.H1(children='Visitors of my RedBubble Store'),

    # a div to put a short description
    html.Div(children='''
        This is a visualization of the number of visitors my RedBubble store has had over the last year.
    '''),

    # append the visualization to the page
    dcc.Graph(
        id='exercise3',
        figure={
            # configure the data
            'data': [
                # set x to be weekday, and y to be the counts. We use bars to represent our data.
                {'x': months, 'y': total_users, 'type': 'line', 'name': 'Total Visitors'},
                {'x': months, 'y': usa_users, 'type': 'line', 'name': 'USA Visitors'},
                {'x': months, 'y': uk_users, 'type': 'line', 'name': 'UK Visitors'},
                {'x': months, 'y': germany_users, 'type': 'line', 'name': 'Germany Visitors'},
                {'x': months, 'y': canada_users, 'type': 'line', 'name': 'Canada Visitors'},
                {'x': months, 'y': australia_users, 'type': 'line', 'name': 'Australia Visitors'},
            ],
            # configure the layout of the visualization --
            'layout': {
                'title': 'Users Visiting RedBubble store per Month',
                'clickmode': 'event+select'
            }
        }
    )
])

if __name__ == '__main__':
    # start the Dash app
    app.run_server(debug=True)
