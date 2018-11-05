import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

app = dash.Dash()

df = pd.read_csv(
    './episode_data.csv'
    )

available_shows = df['show'].unique()

app.layout = html.Div([
    html.Div([

        html.Div([
            dcc.Dropdown(
                id='show-name',
                options=[{'label': i, 'value': i} for i in available_shows],
                value='The Bitcoin Podcast'
            ),
        ],
        style={'width': '48%', 'display': 'inline-block'}),
    ]),

    dcc.Graph(id='indicator-graphic'),

    # dcc.Slider(
    #     id='year--slider',
    #     min=df['Year'].min(),
    #     max=df['Year'].max(),
    #     value=df['Year'].max(),
    #     step=None,
    #     marks={str(year): str(year) for year in df['Year'].unique()}
    # )
])

@app.callback(
    dash.dependencies.Output('indicator-graphic', 'figure'),
    [dash.dependencies.Input('show-name', 'value')]
    )
def update_graph(show_name):
    dff = df[df['show'] == show_name]

    return {
        'data': [go.Bar(
            name = 'LibSyn', 
            x = dff['downloads'],
            y = dff['title'],
            # width = [0.5 for _ in dff['title'].values],
            marker={
                'color': dff['color'],
                'line': dict(
                    color = "e8800f",
                    width = 0
                )
            },
            opacity = 0.85,
            orientation = 'h'
        )],
        'layout': go.Layout(
            barmode="stack",
            margin=go.Margin(
                l=375,
                r=30,
                b=30,
                t=50,
                pad=4
            ),
            yaxis = dict(
        #         title = 'Total downloads',
                gridcolor='#f2f2f2',
        #         zerolinecolor='#969696',
        #         showline=True,
                # constrain="domain",
                # constraintoward="top",
                # fixedrange=True,
                autorange=False,
                range=[0,20]
            ),
            xaxis = dict(
        #         zerolinecolor='#969696'
                gridcolor='#f2f2f2',
        #         tickangle=45,
            ),
            paper_bgcolor='rgba(242,242,242,0)',
            plot_bgcolor='#d7d8d8',
            # font=dict(family='Helvetica, sans-serif', size=16, color='#2e2e2e'),
            # width=1200,
            legend=dict(
                x=0.8,
                y=1
            )
        )
    }


if __name__ == '__main__':
    app.run_server()