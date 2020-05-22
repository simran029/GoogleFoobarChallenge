# Hello World program in Python
    
def solution(l):
  #  print(len(l))
    if len(l)<3:
        return 0
    ans = [0]*len(l)
    x = len(l)-2
    res=0
    while x>=0 :
        y = 0
        z = len(l)-1
        div = 0
        mul = 0
        while x>y:
            if l[x]%l[y]==0:
                div +=1
            y +=1
        while x<z:
            if l[z]%l[x]==0:
                mul +=1
            z -=1
        res= res + mul*div
        x -=1
            
    return res
            
            
    
#
#print(solution([1,2,4,6]))    
        
