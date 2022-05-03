def solution(N):
    list1 = []
  
    while N != 0:
        if N % 2 ==0:
            list1.append(0)
            N /= 2
        else:
            list1.append(1)
            N = (N-1)/2
    max =0
    count =0
    list1 = list1[list1.index(1):]
    for i in list1:
        if i==0:
            count+=1
        else:
            if count>max:
                max=count
            count=0
    return max