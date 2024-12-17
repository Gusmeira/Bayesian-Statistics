import plotly.graph_objects as go
import plotly.subplots
from typing import List, Union, Optional




# USED WITH PLOTLY TO ELABORATE THE DESIGN ===========================================================
def main_layout(fig:go.Figure, width=700, height=600, x=None, y=None, title=None,
               x_range=None, y_range=None, paper_color='white', 
               customdata:Union[str, None]=None, hover_customdata='Info', 
               hover_x='x',hover_y='y', **kwargs) -> go.Figure:
    fig.layout = go.Layout(
        width=width,
        height=height,
        plot_bgcolor=paper_color,
        paper_bgcolor=paper_color,
        xaxis={'gridcolor':'#cccccc', 'linecolor':'black','title':x, 'range':x_range},
        yaxis={'gridcolor':'#cccccc', 'linecolor':'black','title':y, 'range':y_range},
        title={'text':title},
        **kwargs
    )
    if customdata == 'no':
        ...
    elif customdata is None:
        fig.update_traces(patch={
            'customdata':customdata, 'hovertemplate': hover_x + ': %{x}<br>' + hover_y + ': %{y}'
        })
    else:
        fig.update_traces(patch={
            'customdata':customdata,
            'hovertemplate': hover_x + ': %{x}<br>' + hover_y + ': %{y}<br>' + hover_customdata + ': %{customdata}<br>'
        })
    return fig
# ====================================================================================================
def main_subplot_layout(fig:go.Figure, width=1400, height=500, title=None, paper_color='white',
                        x=None, y=None, rows=1, cols=2, x_range=None, y_range=None,
                        customdata:Union[str, None]=None, hover_customdata='Info', 
                        hover_x='x',hover_y='y', **kwargs) -> go.Figure:
    fig.update_layout({
        'width':width,
        'height':height,
        'plot_bgcolor':paper_color,
        'paper_bgcolor':paper_color,
        'title':title,
        **kwargs
    })
    for xaxis in fig.select_xaxes():
        xaxis.update(
            showgrid=True,
            gridcolor='#CCCCCC',
            linecolor='black',
            title=x,
            range=x_range
        )
    for yaxis in fig.select_yaxes():
        yaxis.update(
            showgrid=True,
            gridcolor='#CCCCCC',
            linecolor='black',
            title=y,
            range=y_range
        )
    if customdata == 'no':
        ...
    elif customdata is None:
        fig.update_traces(patch={
            'customdata':customdata, 'hovertemplate': hover_x + ': %{x}<br>' + hover_y + ': %{y}'
        })
    else:
        fig.update_traces(patch={
            'customdata':customdata,
            'hovertemplate': hover_x + ': %{x}<br>' + hover_y + ': %{y}<br>' + hover_customdata + ': %{customdata}<br>'
        })
    return fig
# ====================================================================================================