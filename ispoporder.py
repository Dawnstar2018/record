#coding=utf-8#
class sloution():
    def __init__(self):
        self.pushseq = []
        #self.popseq = popseq
    def ispoporder(self,node,popseq):
        print('a is:',node)
        print('b is:',popseq)
        l_push = len(node)
        print('l_push is ',l_push)
        l_pop = len(popseq)
        i_popseq_idx = 0;
        for i in range(0,l_push):
            #print('node i is:',node[i])
            self.pushseq.append(node[i])
            while self.pushseq[-1] == popseq[i_popseq_idx]:
                #print('popseq is :',popseq[i_popseq_idx])
                self.pushseq.pop(-1)
                i_popseq_idx = i_popseq_idx + 1
        if self.pushseq ==[]:
            return True
        print(self.pushseq)
        return False

if __name__== '__main__':
    a=[1,2,3,4,5]
    b=[4,5,3,1,2]
    s=sloution()
    s.ispoporder(a,b)



