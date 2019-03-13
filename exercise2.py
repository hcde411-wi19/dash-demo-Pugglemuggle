# Exercise 2
# Create another visualization of your choice of data and chart type.
# You can use pandas to help loading data, or just hard-coded the data is fine.

# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

# static data
months = ['March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December', 'January', 'February']
total_users = [18, 16, 20, 28, 26, 19, 53, 41, 38, 43, 31, 35]
# TODO: working on this file to add more codes...

# initialize Dash environment
app = dash.Dash(__name__)

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
        id='example-graph',
        figure={
            # configure the data
            'data': [
                # set x to be weekday, and y to be the counts. We use bars to represent our data.
                {'x': months, 'y': total_users, 'type': 'line', 'name': 'Total Visitors'},

            ],
            # configure the layout of the visualization --
            'layout': {
                'title': 'Users Visiting RedBubble store per Month'
            }
        }
    )
])

if __name__ == '__main__':
    # start the Dash app
    app.run_server(debug=True)



