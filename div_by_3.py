import numpy as np
A=np.arange(1,101)
B=A.reshape(10,10)
squares=B**2
div3=np.array([(squares[squares%3==0])])
print(squares,div3)
np.save('div_by_3',squares,div3)
