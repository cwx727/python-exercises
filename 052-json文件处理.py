#include utf-8
import json
from pygal_maps_world.i18n import COUNTRIES
import pygal
import pygal.maps.world
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS

def get_country_code(country_name):
	"""根据指定的国家， 返回Pygal使用的两个字母的国别码"""
	for code, name in COUNTRIES.items():
		if name == country_name:
			return code

	if country_name == 'Yemen, Rep.':
		return 'ye'

	# 如果没有找到指定的国家， 就返回None
	return None

filename = '/home/python/ftp/share/python练习题/bookfile/chapter_16/population_data.json'
with open(filename) as f:
	pop_data = json.load(f)

# 创建一个包含人口数量的字典	
cc_populations = {}
for pop_dict in pop_data:
	if pop_dict['Year'] == '2010':
		country = pop_dict['Country Name']
		population = int(float(pop_dict['Value']))
		code = get_country_code(country)
		if code:
			cc_populations[code] = population
		
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
	if pop < 10000000:
		cc_pops_1[cc] = pop
	elif pop < 1000000000:
		cc_pops_2[cc] = pop
	else:
		cc_pops_3[cc] = pop
		
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))
	
wm_style = RS('#336699', base_style=LCS)
wm=pygal.maps.world.World(style=wm_style)
wm.title = 'World Population in 2010, by Country'
wm.add('0-10m', cc_pops_1)
wm.add('10-1bn', cc_pops_2)
wm.add('>1bm', cc_pops_3)

wm.render_to_file('world_population2.svg')







