#coding:utf-8#
class solution():
    def __init__(self):
        self.oristack=[]
        self.minstack=[]
    def push(self,node):
        self.oristack.append(node)
        if self.minstack == []:
            self.minstack.append(node)
        else:
            if node > self.minstack[-1]:
                self.minstack.append(self.minstack[-1])
            else:
                self.minstack.append(node)
        print(self.oristack,self.minstack)
    def pop(self):
        if len(self.oristack)==0:
            return 0
      #  print(self.oristack.pop(-1))
       # print(self.minstack.pop(-1))

if __name__ == '__main__':
    solution = solution()
    solution.push(1)
    solution.push(3)
    solution.pop()
