#def cal_num_club_sum(n):
#	sum = 0
#	for n in [int(i) for i in str(n)]:
#		sum = sum + n * n * n
#	return sum
#
#n = 999
#result = 0
#while True:
#	result = cal_num_club_sum(n)
#	if result != n:
#		n = result
#	else:
#		print(result)
#		break


def cal_num_club_sum(n):
	sum = 0
	for n in [int(i) for i in str(n)]:
		sum = sum + n * n * n
	return sum


n = 48
result = 0
while True:
	result = cal_num_club_sum(n)
	if result != n:
		print(result)
		n  = result
	else:
		print(result)
		break


























#list = [2,3,4,5,6,2,4]
#print list

#b = set(list)

#print b

#b = sorted(b, reverse = True)

#for x in b:
#	print x

#s = "ajldjlajfdljfddd"
#s = set(s)

#s.sort()
#res = "".join(s)
#print res


#def getmin(list):
#	for x in list:
#		print x



#getmin(list)

#for x in range(1, 10):
#	print x

#dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}


#for key, value in dict.items():
#	print key + ":" + str(value)


#print sum(range(1,101))





#print(get_club_sum(12))


#def cal_num_club_sum(n):
#	sum = 0
#	for n in [int(i) for i in str(n)]:
#		sum = sum + n * n * n
#	return sum
#
#n = 999
#result = 0
#while True:
#	result = cal_num_club_sum(n)
#	if result != n:
#		n = result
#	else:
#		print(result)
#		break


def cal_num_club_sum(n):
	sum = 0
	for n in [int(i) for i in str(n)]:
		sum = sum + n * n * n
	return sum


n = 48
result = 0
while True:
	result = cal_num_club_sum(n)
	if result != n:
		print(result)
		n  = result
	else:
		print(result)
		break


























#list = [2,3,4,5,6,2,4]
#print list

#b = set(list)

#print b

#b = sorted(b, reverse = True)

#for x in b:
#	print x

#s = "ajldjlajfdljfddd"
#s = set(s)

#s.sort()
#res = "".join(s)
#print res


#def getmin(list):
#	for x in list:
#		print x



#getmin(list)

#for x in range(1, 10):
#	print x

#dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}


#for key, value in dict.items():
#	print key + ":" + str(value)


#print sum(range(1,101))





#print(get_club_sum(12))
'''

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print [x for x in a if x % 2 == 0]

print filter(lambda x : x % 2 == 0, a)

a, b =  5, 6
print (a,b)
b, a  = a, b
print (a,b)
'''