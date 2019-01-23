#encoding=utf-8

number = int(input("请输入数字："))

coordinate_x = number//3
coordinate_y = number%3

print("坐标为：%d,%d" %(coordinate_x,coordinate_y))
