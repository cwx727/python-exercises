#including utf-8
import random

offices = [[], [], []]
teachers =["A","B","C","D","E","F","G","H","I"]
jList=[0,0,0]

for teacherName in teachers:
	index = random.randint(0,2)
	offices[index].append(teacherName)

i=0
while i < len(offices):
	jList[i]=len(offices[i])
	i+=1

jList_max_index = jList.index(max(jList))

k=0
for j in jList:
	while int(j)<=1:
		offices[k].append(offices[jList_max_index][-1])
		offices[jList_max_index].pop()
		j+=1
	k=k+1

print(offices) 	
		


