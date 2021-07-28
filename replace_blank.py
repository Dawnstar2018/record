#replace blank
def replace_blank(strs,max_len):
    if len(strs)==0 or max_len == 0:
        return False
    else:
        blank_num = strs.count(' ')
        original_len = len(strs)-1
        strs += (""for i in range(2*blank_num))
        after_len = len(strs)-1
        if after_len > max_len:
            return False
        while after_len != original_len:
            if strs[original_len] == " ":
                after_len-=2
                strs[after_len:after_len+3]="%20"
            else:
                strs[after_len]=strs[original_len]
            after_len-=1
            original_len-=1
        return strs

test_string = "We are happy "
string_lst = list(test_string)
res=replace_blank(string_lst,100)
print(res)

