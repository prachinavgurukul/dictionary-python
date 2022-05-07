# dict1={"name":"Raju", "marks":56}
# def present(a):
#     if a in dict1:
#         print("key Exist")
#     else:
#         print("Not Exist")
# present(input("enter key to check:"))

list1=["one","two","three","four","five"]
list2=[1,2,3,4,5]
i=0
c=[]
while i<len(list1):
    b=list1[i],list2[i]
    c.append(b)
    i=i+1
print(dict(c))

