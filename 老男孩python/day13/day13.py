
#递归
import time
def hg(n):
    print(n)
    #time.sleep(2)
    if (int(n/2)==0):
        return n
    return hg(int(n/2))
res=hg(10)
print(res)
