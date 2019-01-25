#include utf-8
import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename_sitka = '/home/python/ftp/share/python练习题/bookfile/chapter_16/sitka_weather_2014.csv'
filename_death = '/home/python/ftp/share/python练习题/bookfile/chapter_16/death_valley_2014.csv'


def get_data(filename, dates, highs, lows, color):
	with open(filename) as f:
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
				dates.append(current_date)
				highs.append(high)		
				lows.append(low)
	
	
	plt.plot(dates, highs, c=color, alpha=1)  #实参alpha 指定颜色的透明度
	plt.plot(dates, lows, c=color, alpha=1)
	plt.fill_between(dates, highs, lows, facecolor=color, alpha=0.1)
				
	return dates, highs, lows
dates_sitka,highs_sitka,lows_sitka = [], [], []
fig = plt.figure(dpi=128, figsize=(10, 6))
get_data(filename_sitka, dates_sitka, highs_sitka, lows_sitka, 'blue')
dates_death,highs_death,lows_death = [], [], []
get_data(filename_death, dates_death, highs_death, lows_death, 'red')

'''	
# 根据数据绘制图形	
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates_sitka, highs_sitka, c='blue', alpha=1)  #实参alpha 指定颜色的透明度
plt.plot(dates_sitka, lows_sitka, c='blue', alpha=1)
plt.plot(dates_death, highs_death, c='red', alpha=1)  #实参alpha 指定颜色的透明度
plt.plot(dates_death, lows_death, c='red', alpha=1)
plt.fill_between(dates_sitka, highs_sitka, lows_sitka, facecolor='blue', alpha=0.1)
plt.fill_between(dates_death, highs_death, lows_death, facecolor='red', alpha=0.1)
'''

# 设置图形的格式
#plt.title("Daily high and low temperatures = 2014", fontsize=24)
title = "Daily high and low temperatures - 2014\nDeath Valley and Sitka"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()

