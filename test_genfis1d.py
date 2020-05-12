#test genfis 1D
def my_exponential(A, B, C, x):
    return A*np.exp(-B*x)+C

data_x = np.arange(0,10.1,0.1)
data_y = my_exponential(9, 0.5,1, data_x)
data = np.vstack((data_x, data_y)).T

fis2 = fis()
fis2.genfis(data,0.9)
fis2.viewInputs()
r = fis2.evalfis(np.vstack(data_x))

plt.figure()
plt.plot(data_x,data_y)
plt.plot(data_x,r,linestyle='--')
