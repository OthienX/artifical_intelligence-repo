import matplotlib.pyplot as pt
import numpy as np
from scipy import stats
x = np.random.uniform(0.3,10,100)
y = np.random.uniform(2,40,100)
slope, intercept, r,p, std_err =stats.linregress(x,y)
def myfun(x):
    return slope *x + intercept
mymodel = list(map(myfun, x))
pt.scatter(x,y)
pt.plot(x,mymodel)
pt.show()