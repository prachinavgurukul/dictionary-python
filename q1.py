dic1={1:10, 2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}
dic={}
# b={}
# for i in dic2:
#     if i in dic1:
#         dic1[i]=dic1[i]+dic2[i]
#         dic1.update(dic3)
#     else:
#         dic1[i]=dic2[i]
# print(dic1)



for i in dic1,dic2,dic3:
    dic.update(i)
    for i in dic:
        if i in dic1:
            if i in dic2:
                dic.update({i:(dic1[i]+dic2[i])})
print(dic)
