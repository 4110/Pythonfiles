import folium
import pandas as pd

state_geo = 'states2.json'
state_air_quality = 'kisedata.csv'

state_data = pd.read_csv(state_air_quality)

#Let Folium determine the scale
map = folium.Map(location=[21, 78], zoom_start=5)

folium.Choropleth(
    geo_data=state_geo,
    data=state_data,
    columns=['State', 'Total'],
    key_on='feature.id',
    fill_color='YlGn',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Total Deaths (%)'
).add_to(map)

folium.LayerControl().add_to(map)


map.save('kise.html')