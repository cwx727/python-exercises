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

filename = '/home/python/ftp/share/python练习题/bookfile/chapter_16/okfn.json'
with open(filename) as f:
	pop_data = json.load(f)
#for pop_dict in pop_data:
#	print(pop_dict)

# 创建一个包含人口数量的字典	
cc_gdps = {}
for pop_dict in pop_data:
	if pop_dict['Year'] == 2016:
		country = pop_dict['Country Name']
		gdp = int(float(pop_dict['Value']))
		code = get_country_code(country)
		if code:
			cc_gdps[code] = gdp
'''
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_gdps.items():
	if pop < 1000000000:
		cc_pops_1[cc] = pop
	elif pop < 5000000000:
		cc_pops_2[cc] = pop
	else:
		cc_pops_3[cc] = pop
	
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))
'''
wm_style = RS('#336699', base_style=LCS)
wm=pygal.maps.world.World(style=wm_style)
wm.title = 'World gdp in 2014, by Country'
wm.add('gdp', cc_gdps)

wm.render_to_file('World_GDP.svg')







