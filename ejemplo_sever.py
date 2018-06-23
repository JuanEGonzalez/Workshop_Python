import pandas as pd
df_estaciones_M10 = pd.read_csv('Estaciones_RM_1semana.csv')
df_estaciones_M10

from bokeh.plotting import figure, output_file, reset_output
from bokeh.io import show, output_notebook
from bokeh.models.widgets import Button, Select
from bokeh.layouts import widgetbox
from bokeh.models import ColumnDataSource
from bokeh.io import curdoc
from bokeh.layouts import column

# crear widgets
button = Button(label="Button")
select = Select(title="Estación:", value="Estación Independencia", options=df_estaciones_M10.estacion.unique().tolist())

source_estacion = ColumnDataSource(data=dict(Fecha=[], MP10=[]))
                                           
p1 = figure(x_axis_type="datetime", title="Estación", plot_width=800, plot_height=250, y_range = (0,400))
p1.xaxis.axis_label = 'Fecha'
p1.yaxis.axis_label = 'MP10'

p1.line(x = "Fecha", y = "MP10", legend='MP10', color='navy', source = source_estacion)
#p1.circle(x = "Fecha", y = "MP10", legend='MP10', color='navy', size = 5, source = source_estacion)
p1.legend.location = "top_left"

def select_estacion():
    sel_value = select.value
    p1.title.text = "Elegido: " + sel_value
    print(sel_value)
    return df_estaciones_M10[df_estaciones_M10.estacion == sel_value]
def update():
    df_sel = select_estacion()
    source_estacion.data = dict(
        Fecha = df_sel.FECHA_HORA.tolist(),
        MP10 = df_sel.MP10.tolist(),
    )
    
select.on_change('value', lambda attr, old, new: update())
# mostrar resultados
l = column(widgetbox(button, select, width=300), p1)
update()

#show(l)
curdoc().add_root(l)
curdoc().title = "Ensayo_Bokeh"