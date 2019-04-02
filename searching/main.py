import ternary_search as ts 
import binary_search as bs
import linear_search as ls

l1 = [16,20,26,30,36,40,46,50,56,60,66,70,76,80]
target = 76

ternary_search = ts.ternary_search(l1 , target)
ternary_search.ternary_search()

binary_search = bs.binary_search(l1 , target)
binary_search.binary_search()

linear_search = ls.linear_search(l1 , target)
linear_search.linear_search()