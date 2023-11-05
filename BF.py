input = [[10, 20, 23, 4],
		 [15, 13, 6, 25],
		 [ 2, 22, 35, 34],
		 [12, 3, 14, 17]]

# 階乘
def fac(value):
	temp = 1
	for i in range(1, value+1):
		temp *= i
	return temp

# 生成階乘數列
def fac_series(value):
	times = []
	for i in range(len(input)):
		times.append(fac(len(input)-i))
	return times

# decoder
def decoder(value, times):
	temp = value
	decode = []
	for i in range(1,len(input)):
		temp_2 = temp//times[i]
		temp_3 = temp%times[i]
		decode.append(temp_2)
		temp = temp%times[i]
	return decode

# synthesis path
def path_gen(decoder, length):
	path = [] 										# 計數
	stack = list(range(1,length+1))
	for i in decoder[:]:							# 執行所有值
		temp = i 									# 不含已用過的數的計數
		count = 0 									# 計數，stack[count]
		while( temp != -1 and count<len(stack) ):
			if(stack[count]>=0):					# 判斷後temp-1
				if( temp==0 ):
					path.append(stack[count])
					stack[count] = -1
				temp = temp - 1
			count = count + 1
	for i in stack:
		if(i!=-1):	path.append(i)

	return path

# 計算路徑成績
def score(path):
	temp = 0
	for i in range(len(path)):
		temp = temp + input[i][path[i]-1]
	return temp

'''
# 主程式
mini = 9223372036854775807
count = 0
fac_seri = fac_series(len(input))

for k in range(fac_seri[0]):					# 好累喔，先不考慮剪枝
	temp = 0
	decode = decoder(k, fac_seri)
	path = path_gen(decode, len(input))
	temp = score(path)
	if(temp<mini): 								# 找最小值
		mini = temp
		final_path = path
# 輸出整理
for i in range(len(final_path)):
	final_path[i] = final_path[i]-1

print("yourAssignment",final_path)
print("Cost",mini)
'''
fac_seri = fac_series(4)
path_gen(decoder(11, fac_seri), 4)
print(path_gen(decoder(11, fac_seri), 4))