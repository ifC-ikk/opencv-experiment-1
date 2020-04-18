sigma=0.3
sd = float(sigma)
lw = int(3.0 * sd + 0.5)
kernel=filters._gaussian_kernel1d(3,0, lw)[::-1]
print(kernel)

def gausskernel(size):
    sigma=0.3
    gausskernel=np.zeros((size,size),np.float32)
    for i in range (size):
        for j in range (size):
            norm=math.pow(i-1,2)+pow(j-1,2)
            gausskernel[i,j]=math.exp(-norm/(2*math.pow(sigma,2)))
    sum=np.sum(gausskernel)
    kernel=gausskernel/sum
    return kernel

plt.imshow(gausskernel(3),cmap='gray')