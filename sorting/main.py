import bubble as b
import insertion as i
import selection as s

a = [6,5,4,3,2,1 ,7 , 9 ,10 , 34]
b = [1,2,3,4,5,6]

bub = b.Bubble(a)
bub.bubble()

sel = s.Selection(a)
sel.selection()

ins = s.Insertion(a)
ins.insertion()