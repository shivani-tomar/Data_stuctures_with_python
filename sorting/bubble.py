def bubble(a):
    size = len(a);
    swapcount =0;
    for i in range(size):
        for j in range(size-i-1):
            if a[j]>a[j+1]:
                a[j] = a[j]^a[j+1];
                a[j+1] = a[j]^a[j+1];
                a[j] = a[j] ^ a[j+1];
                swapcount+=1;
    print (swapcount);
    return a;
    
    
a = [6,5,4,3,2,1]
b = [1,2,3,4,5,6]
print(bubble(b));