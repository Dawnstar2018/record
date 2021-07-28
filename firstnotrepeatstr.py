#coding-utf-8#
#this script is use to  find the str which is not repeated
def firstnotrepeatstr(str):
    dict={}
    for ele in str:
        #print(ele)
        if ele in dict:
            dict[ele] +=1
        else:
            dict[ele] = 1
    print(dict)
    for i in range(0,len(str)):
        #print(str[i])
        if dict[str[i]] == 1:
            return str[i]
    return -1

a='aabbdccd'
res=firstnotrepeatstr(a)
print(res)
