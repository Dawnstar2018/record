#coding:utf-8#
# use to print matrix clockwise

class solution():
    def out_matirx(self,matrix):
        res=[]
        while matrix:
            res.append(matrix.pop(0))
            print(res)
            if not matrix or not matrix[0]:
                break
            matrix = self.turn(matrix)
        return res

    def turn(self,matrix):
        n_row = len(matrix)
        n_col = len(matrix[0])
        new_matrix=[]
        for i in range(0,n_col):
            sp=[]
            for j in range(0,n_row):
                sp.append(matrix[j][i])
            new_matrix.append(sp)
            #print(new_matrix)
        new_matrix.reverse()
        return new_matrix



a=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
s=solution()
s.out_matirx(a)
