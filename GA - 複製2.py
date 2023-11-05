import random
import csv
import os

input = [[0.43045255, 0.78681387, 0.07514408, 0.72583933, 0.52916145, 0.87483212, 0.34701621],
[0.68704291, 0.45392742, 0.46862110, 0.67669006, 0.23817468, 0.87520581, 0.67311418],
[0.38505150, 0.05974168, 0.11388629, 0.28978058, 0.66089373, 0.92592403, 0.70718757],
[0.24975701, 0.16937649, 0.42003672, 0.88231235, 0.74635725, 0.59854858, 0.88631100],
[0.64895582, 0.58909596, 0.99772334, 0.85522575, 0.33916707, 0.72873479, 0.26826203],
[0.47939038, 0.88484586, 0.05122520, 0.83527995, 0.37219939, 0.20375257, 0.50482283],
[0.58926554, 0.45176739, 0.25217475, 0.83548120, 0.41687026, 0.00293049, 0.23939052]]



# evolution函式需要做排序
def mergeSort(arr):
	if len(arr) > 1:
		# Finding the mid of the array
		mid = len(arr)//2

		# Dividing the array elements into 2 halves
		L = arr[:mid][:]
		R = arr[mid:][:]
 
		# Sorting the first half and second half
		L = mergeSort(L)
		R = mergeSort(R)

		return merge(L,R)

	else:	return arr	

def merge(L,R):
	L_index,R_index = 0,0
	merge_list = []

	# 判斷列表裡面是否還有元素可以用
	while L_index < len(L) and R_index < len(R):
	# 哪邊的元素小於另外一邊的的元素就把哪邊的元素加入進去，對應的索引加一
		if L[L_index][0] > R[R_index][0]:
			merge_list.append([L[L_index][0],L[L_index][1]])
			L_index += 1
		else:
			merge_list.append([R[R_index][0],R[R_index][1]])
			R_index += 1
	# 下面的這兩個就是，如果有一個列表全部添加了，另外一個列表直接新增到merge_list裡面了
	merge_list += L[L_index:]
	merge_list += R[R_index:]
	return merge_list

def probability(value):
	if( value>=random.random() ): return 1
	else: return 0

# 基因生成
def chromosomes(length):
	chromo = []
	while(length):
		chromo.append(random.randint(1,length))
		length = length - 1
	return chromo

# synthesis path
def path_gen(chromo, length):
	path = [] 										# 計數
	stack = list(range(1,length+1))
	for i in chromo[:]:								# 執行除了最後一個外的
		temp = i 									# 不含已用過的數的計數
		count = 0 									# 計數，stack[count]
		while( temp != -1 and count<len(stack) ):
			if(stack[count]>=0):					# 判斷後temp-1
				if( temp==1 ):
					path.append(stack[count])
					stack[count] = -1
				temp = temp - 1
			count = count + 1
	for i in stack:
		if(i!=-1):	path.append(i)

	return path

# 交配
def crossover(chromo1, chromo2, cut):
	cross = []
	for i in range(cut):
		cross.append(chromo1[i])
	for i in range(cut,len(chromo1)):
		cross.append(chromo2[i])
	return cross

# 計算路徑成績
def score(path):
	temp = 0
	for i in range(len(path)):
		temp = temp + input[i][path[i]-1]
	return temp

def evolution(pool, cut, prob):
	#變數設定
	evolu = []
	rank = []
	temp_path = []
	#生成所有分數
	for i in range( len(genetic_pool) ):
		temp_path = path_gen(pool[i][:],len(pool[i][:]))	#解碼
		rank.append( [score(temp_path),i] )

	#排序
	rank = mergeSort(rank)

	#PR前50交配
	chromo1 = pool[ rank[i][1] ][:]				#強勢基因
	for i in range(len(genetic_pool)//2):
		chromo2 = pool[ rank[i+1][1] ][:]
		evolu.append(crossover(chromo1, chromo2, cut))
		evolu.append(crossover(chromo2, chromo1, cut))

	#突變
	for i in range(len(evolu)):
		for j in range(len(evolu[0][:])):
			if(probability(prob)):
				evolu[i][j] = random.randint(1,len(evolu[0][:])-j)

	return evolu	



# 變數設定
genetic_pool = []
pool_score = []
pool_path = []
aaa = []
bbb = []
pool_size = 8
evolu_times = 100
cut = len(input)//3
prob = 0.1

# 生成基因池
for i in range(pool_size):
	genetic_pool.append(chromosomes(len(input)))

# 演化
genetic_pool = evolution(genetic_pool,cut,prob)
for i in range(evolu_times):

	pool_path = []
	pool_score = []
	for j in range( len(genetic_pool) ):
		pool_score.append([ score( path_gen( genetic_pool[j][:], len(genetic_pool[0][:]) ) ) ,i ])
	pool_score = mergeSort(pool_score)
#	for j in range( len(genetic_pool) ):
#		pool_path.append( path_gen( genetic_pool[ pool_score[j][1] ][:], len(genetic_pool[0][:]) ) )	

#	final_path = []
#	for i in range( len( pool_path[-1][:] ) ):
#		final_path.append( pool_path[-1][i]-1 )
	aaa.append(pool_score[-1][0])
#	bbb.append(final_path)

	genetic_pool = evolution(genetic_pool,cut,prob)

print("Cost",aaa)

filename = '分析7.csv'
with open('分析7.csv', 'w', newline='') as csvfile:
	# 建立 CSV 檔寫入器
	writer = csv.writer(csvfile)
	writer.writerow(["演化時間", "分數", "路徑"])

	# 寫入列資料
	for i in range(100):
		writer.writerow([i, aaa[i]])


