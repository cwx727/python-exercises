#include utf-8
import csv
from pygal_maps_world.i18n import COUNTRIES
import pygal
import pygal.maps.world
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS

filename = '/home/python/ftp/share/python练习题/bookfile/chapter_16/API_7_DS2_en_csv_v2_10323378.csv'
#filename_death = '/home/python/ftp/share/python练习题/bookfile/chapter_16/death_valley_2014.csv'

def get_country_code(country_name):
	"""根据指定的国家， 返回Pygal使用的两个字母的国别码"""
	for code, name in COUNTRIES.items():
		if name == country_name:
			return code

	if country_name == 'Yemen, Rep.':
		return 'ye'

	# 如果没有找到指定的国家， 就返回None
	return None


with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	
	'''
	for index, column_header in enumerate(header_row):
		print(index, column_header)

	'''
	# 从文件中获取最高气温
	gdp_data = {}
	Indicator_Name = "GDP deflator: linked series (base year varies by country)"
	for row in reader:
		if row[2] == Indicator_Name:
			try:
				country = row[0]
				gdp = float(row[61])
			except ValueError:
				print(country, 'missing date')
				print('-------------------------')
			else:
				code = get_country_code(country)
				if code:
					gdp_data[code] = gdp
			
print(gdp_data) 		


wm_style = RS('#336699', base_style=LCS)
wm=pygal.maps.world.World(style=wm_style)
wm.title = 'GDP deflator: linked series (base year varies by country)'
wm.add('GDP deflator', gdp_data)

wm.render_to_file('GDP deflator.svg')
