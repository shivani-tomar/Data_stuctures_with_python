# def swap(a,b):
#     a = a^b;
#     b = a^b;
#     a = a^b;
#     result = [];
#     result.append(a);
#     result.append(b);
#     return result;

import dis
def selection(a):
    size = len(a);
    swapcount =0;
    for i in range(0,size):
        minimum = i;
        #print("i is" , i);
        for j in range(i+1 , size):
            #print("j is " ,j);
            if a[minimum]<a[j]:
               minimum = j;
       a[minimum] , a[i] = a[i],a[minimum] 
       swapcount+=1;
    print(swapcount);
    return a;
    
    
a = [7,6,5,4,3,2,1]
b=[1,2,3,4,5,6,7]
print(selection(a));