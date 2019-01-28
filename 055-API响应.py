import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)

# 将API响应存储在一个变量中
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])

repo_dicts = response_dict['items']
'''
print("Repositories returned:", len(repo_dicts))

repo_dict = repo_dicts[0]
print("\nKeys:", len(repo_dict))
for key in sorted(repo_dict.keys()):
	print(key)

print("\nSelected information about first repository:")
for repo_dict in repo_dicts:
	print("Name:", repo_dict['name'])
	print('Owner:', repo_dict['owner']['login'])
	print('Stars:', repo_dict['stargazers_count'])
	print('Repository:', repo_dict['html_url'])
	print('Created:', repo_dict['created_at'])
	print('Updated:', repo_dict['updated_at'])
	print('Description:', repo_dict['description'])
'''	

names, plot_dicts = [], []
for repo_dict in repo_dicts:
	names.append(repo_dict['name'])
	
	#使用键'value' 存储了星数， 并使用键'label' 存储了项目描述。
	polt_dict = {
		'value': repo_dict['stargazers_count'],
		'label': str(repo_dict['description']),
		'xlink': repo_dict['html_url'],
		}
	plot_dicts.append(polt_dict)
#stars.append(repo_dict['stargazers_count'])
	
my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config()
#让标签绕x 轴旋转45度
my_config.x_label_rotation = 45
#隐藏了图例
my_config.show_legend = False
#设置了图表标题、 副标签和主标签的字体大小
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
#使用truncate_label 将较长的项目名缩短为15个字符（如果你将鼠标指向屏幕上被截短的项目名， 将显示完整的项目名）
my_config.truncate_label = 15
#将show_y_guides 设置为False， 以隐藏图表中的水平线
my_config.show_y_guides = False
#设置了自定义宽度， 让图表更充分地利用浏览器中的可用空间
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')
