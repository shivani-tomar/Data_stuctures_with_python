def insertion(a):
    size = len(a);
    for i in range(size):
        temp = a[i];
        j = i;
        while(j>0  and temp<a[j-1]):
            a[j] = a[j-1];
            j-=1;
        a[j] = temp;
    return a;


a = [7,6,8,3,4] 
print(insertion(a));          
