def count_smileys(list):
    count = 0
    for i in range(0,len(list)):
        if len(list[i]) == 2 and (list[i][0] == ':' or list[i][0] == ';' )and (list[i][1] == ')' or list[i][1] == 'D'):
            count = count + 1
            #print(list[i][0],"len = 2",list[i][1])
        else:
            pass
        if len(list[i]) == 3 :
            if list[i][0] == ':' or list[i][0] == ';':
                if list[i][1] == '-' or list[i][1] == '~':
                    if list[i][2] == ')' or list[i][2] == 'D':
                        count = count + 1
                        #print(list[i])
    return count
print(count_smileys([':)',':(',':D',':O',':;']))
''' codewars :
from re import findall
def count_smileys(arr):
    return len(list(findall(r"[:;][-~]?[)D]", " ".join(arr))))
'''