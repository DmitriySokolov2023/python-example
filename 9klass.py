N = 10
A = [0]*10

from random import randint

for i in range(N):
	A[i] = randint(0, 99)
for i in range(N):
	print('A[',i,'] = ', A[i])
print(A)

sum = 0
for i in range(N):
	sum+=A[i]
print('Массив: ', A)
print('Сумма элементов массива:', sum)

imax = 0
for i in range(1,N):
	if A[i] > A[imax]: imax = i
print('Массив: ', A)
print('Максимальный элемент: ', A[imax])

for i in range(N - 1):
	imax = i
	for j in range (1, N):
		if A[j] > A[imax]: imax = j
A[i], A[imax] = A[imax], A[i]
print('Массив по возрастанию: ', A)
