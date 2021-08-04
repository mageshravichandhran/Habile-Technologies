#Habile Technologies Assessment
#solution for problem 1 


def solve(s1):
    s1_arr="".join(s1).split(" ")
    s1_arrsize=len(s1_arr)
    for i in range(0,s1_arrsize):
        min=i
        for j in range(i+1,s1_arrsize):
            if(ord(s1_arr[j][0])-ord(s1_arr[min][0]))<0:
                min=j
        temp=s1_arr[i]
        s1_arr[i]=s1_arr[min]
        s1_arr[min]=temp

    for i in range(0,s1_arrsize):
        print(s1_arr[i]+" ",end=" ")

solve("the domestic dog is a domesticated form of wolf")
