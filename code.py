from itertools import product #used to find the cartesian product from the given iterator, output is lexicographic ordered (dictionary)

K,M = map(int,input().split())
N = (list(map(int, input().split()))[1:] for _ in range(K))
results = map(lambda x: sum(i**2 for i in x)%M, product(*N))
print(max(results))

#we need to develop a python program that can read an integer input separated with lines and then we need to print the maximum value on the output screen.



