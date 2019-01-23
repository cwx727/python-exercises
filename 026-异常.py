#including utf-8

class ShortInputError(Exception):
	def __init__(self, length, atleast):
		Exception.__init__(self)
		self.length = length
		self.atleast = atleast
		
try:
	s = input("请输入：")
	
	if len(s) < 3:
		raise ShortInputError(len(s),3)
	
except EOFError:
		print("你输入了一个结束标记EOF")

except ShortInputError as x:
		print("ShortInputError:输入的长度是%d，长度至少是%d"%(x.length, x.atleast))

else:
	print("没有发生异常")






