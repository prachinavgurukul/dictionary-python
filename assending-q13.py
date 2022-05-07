a={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
sortedByKey={k:v for k,v in sorted(a.items())}
print(sortedByKey)
# dic={k:v for k,v in sorted(a.items(),key=lambda v:v[1],reverse=True)}
# print(dic)




# list=[6,9,15,3,1,0,5,8,7,17]
# i=0
# for i in range (i,len(list)):
#     for j in range(i+1,len(list)):
#         if (list[i]>list[j]):
#             temp=list[i]
#             list[i]=list[j]
#             list[j]=temp
# print(list)

