import numpy as np
X=np.random.random((5,5))
Xstd=np.std(X)
Xmean=np.mean(X)
Z=((X-Xmean)/Xstd)
print(Z)
np.save('X_normalized',Z)
