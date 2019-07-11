# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
'''
You are given N counters, initially set to 0, and you have two possible operations on them:

increase(X) − counter X is increased by 1,
max counter − all counters are set to the maximum value of any counter.
A non-empty array A of M integers is given. This array represents consecutive operations:

if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),
if A[K] = N + 1 then operation K is max counter.
'''

def solution(N, A):
    arr = [0]*(N+1)
    m = 0
    mm = 0
    for i in A:
        if i > N:
            mm = m
        else:
            if arr[i] < mm:
                arr[i] = mm
            arr[i]+=1
            m = max(m,arr[i])
        #print(arr,i,m)
    del(arr[0])
    for i,ele in enumerate(arr):
        if arr[i] < mm:
            arr[i] = mm
    return arr
