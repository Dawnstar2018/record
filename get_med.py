#coding:utf-8#
class solution:
    def get_med(self,lis):
        sort_list = self.getsort(lis)
        if len(sort_list)%2 == 1:
            res = sort_list[(len(sort_list)-1)//2]
        else:
            res = (sort_list[len(sort_list)//2]+sort_list[(len(sort_list)//2)-1])/2
        return res
    def getsort(self,lis):
        for i in range(len(lis)-1):
            for j in range(i+1,len(lis)):
                if lis[i] > lis[j]:
                    lis[i],lis[j] = lis[j],lis[i]
        return lis


a=[1,3,5,6]
s=solution()
ress=s.get_med(a)
print(ress)
