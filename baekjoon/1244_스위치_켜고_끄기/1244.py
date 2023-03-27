import sys
sys.stdin = open("input.txt")

n = int(input())
lst = [-1] + list(map(int,input().split()))
num_student = int(input())
n = len(lst)

def switch(index):
    if lst[index] == 1:
        lst[index] = 0
    else:
        lst[index] = 1

for _ in range(num_student):
    gender, num = map(int,input().split())

    # 남학생
    # if gender == 1:
    #     for i in range(num, n, num):
    #         if lst[i] == 1:
    #             lst[i] = 0
    #         else:
    #             lst[i] = 1
    #         lst[i] = 1 if lst[i] == 0 else 0

    if gender == 1:
        for i in range(n):
            if i % num == 0:
                switch(i)
    elif gender == 2:
        switch(num)
        k = 1
        while 1:
            if 0<=num-k and num+k<n and lst[num - k] == lst[num + k]:
                switch(num-k)
                switch(num+k)
                k += 1
            else:
                break

lst = lst[1:]
lst.pop(0)
for i in range(0, n, 20):
    print(*lst[i:i+20])