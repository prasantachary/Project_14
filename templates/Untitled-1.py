L = [55,78,24,999,33,420,78]
user = int(input('Enter the value to search:  '))
for ind in range(len(L)):
	if(L[ind] == user):
		print(f'user value present in {ind}')
		break
else: 
	print(-1)