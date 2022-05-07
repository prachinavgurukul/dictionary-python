my_dict={
'a':50, 
'b':58, 
'c':56,
'd':40, 
'e':100, 
'f':20
}
a=0
for i in my_dict:
    if my_dict[i]>a:
        a=my_dict[i]
        b=0
        for j in my_dict:
            if my_dict[j]>b and my_dict[j]!=a:
                b=my_dict[j]
                c=0
                for k in my_dict:
                    if my_dict[k]>c and my_dict[k]!=a and my_dict[k]!=b:
                        c=my_dict[k]
print([a,b,c])
    
    