#Habile Technologies Assessment
#solution for problem 2

def solve(txt):
    list=" ".join(txt).split(" ")
    mid=len(list)//2
   
    if(len(list)%2==0):
        list=list[:mid]+[""]+list[mid:]
    i=mid
    j=0
    while i>0:
        if i==mid:
            list[i]=" "+list[i]+" "
        else:
            if " " not in list[i]:
                list[i],list[i+j]=" "+list[i],list[i+j]+" "

              
                list[i],list[i+j]=" "+list[i+j],list[i]+" "

                if i!=mid:
                    itr=i
                    itropp=j
            
                    while (itr<mid):

                        list[itr+1],list[itr+itropp-1]=list[itr+itropp-1],list[itr+1]
                        itr+=1
                        itropp-=2
                   
        print("".join(list))     
        i-=1
        j+=2

solve("CARDBOARD")