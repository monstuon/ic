c1 = np.random.rand(150,2)+[1,1]
c2 = np.random.rand(100,2)+[10,1.5]
c3 = np.random.rand(50,2)+[4.9,5.8]
m = np.append(c1,c2, axis=0)
m = np.append(m,c3, axis=0)

r,c = subclust2(m,1.5)

plt.figure()
plt.scatter(m[:,0],m[:,1])
plt.scatter(c[:,0],c[:,1], marker='X')