'''
11-2 人口数量 ： 修改前面的函数， 使其包含第三个必不可少的形参population ， 并返回一个格式为City, Country - population xxx 的字符串，
如Santiago, Chile - population 5000000 。 
'''


def get_formatted_city(city, country, population=''):
    if population:
        full_city = (city + ', ' + country).title() + ' - population ' + population
    else:
        full_city = (city + ', ' + country).title()
    return full_city
