#include utf-8
import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename_sitka = '/home/python/ftp/share/python练习题/bookfile/chapter_16/sitka_weather_2014.csv'
filename_death = '/home/python/ftp/share/python练习题/bookfile/chapter_16/death_valley_2014.csv'

class Get_data():
	def __init__(self, filename, color):
		self.filename = filename
		self.color = color
		self.dates = []
		self.highs = []
		self.lows = []

	
	def get_data_file(self):
		with open(self.filename) as f:
			reader = csv.reader(f)
			header_row = next(reader)

			# 从文件中获取最高气温	
			for row in reader:
				try:
					current_date = datetime.strptime(row[0], "%Y-%m-%d")
					high = int(row[1])
					low = int(row[3])
				except ValueError:
					print(current_date, 'missing date')
				else:
					self.dates.append(current_date)
					self.highs.append(high)		
					self.lows.append(low)

		
	def plot_datas(self):

		plt.plot(self.dates, self.highs, c=self.color, alpha=1)  #实参alpha 指定颜色的透明度
		plt.plot(self.dates, self.lows, c=self.color, alpha=1)
		plt.fill_between(self.dates, self.highs, self.lows, facecolor=self.color, alpha=0.1)
		
	def output_data(self):
		self.get_data_file()
		self.plot_datas()

fig = plt.figure(dpi=128, figsize=(10, 6))
			
sitka = Get_data(filename_sitka, 'blue')
sitka.output_data()

death = Get_data(filename_death, 'red')
death.output_data()

# 设置图形的格式
#plt.title("Daily high and low temperatures = 2014", fontsize=24)
title = "Daily high and low temperatures - 2014\nDeath Valley and Sitka"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()

