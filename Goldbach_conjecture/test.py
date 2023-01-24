import time
#from pprint import pprint
import goldbach_conjecture

then=time.time()
result=goldbach_conjecture.result(10)

print(result)
#pprint(result)
print(time.time()-then, "Seconds")
