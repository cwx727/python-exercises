#include utf-8
import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename = '/home/python/ftp/share/python练习题/bookfile/chapter_16/sitka_weather_2014.csv'
#filename_death = '/home/python/ftp/share/python练习题/bookfile/chapter_16/death_valley_2014.csv'


with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	
	'''
	for index, column_header in enumerate(header_row):
		print(index, column_header)
	'''

	# 从文件中获取最高气温
	dates = []
	highs = []
	lows = []
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
	
# 根据数据绘制图形	
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)  #实参alpha 指定颜色的透明度
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# 设置图形的格式
#plt.title("Daily high and low temperatures = 2014", fontsize=24)
title = "Daily high and low temperatures - 2014\nDeath Valley and Sitka"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()

