import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from scipy import linalg
import copy


def image_svd(n):
    # read image
    img=mpimg.imread('SnakeDance.jpg')

    # generate rgb array
    [r,g,b] = [img[:,:,i] for i in range(3)]
        
    # generate U, sigma,and V for red, green and blue matrix
    #noted that r1=U, r2=sigma, r3=V, same goes to green and blue matrix
    r1, r2, r3 = linalg.svd(r)
    g1, g2, g3 = linalg.svd(g)
    b1, b2, b3 = linalg.svd(b)
    
    #check the number of non zero elements in each color of decompose sigma
    r2_nonzero=(r2!=0).sum()
    g2_nonzero=(g2!=0).sum()
    b2_nonzero=(b2!=0).sum()
    print("The number of non zero elements in decompose sigma of red, green, blue matrices are", r2_nonzero,"," ,g2_nonzero,"and" ,b2_nonzero, "respectively.")
    
    
    # keeping first n none zero elements
    r2[n:800] = np.zeros_like(r2[n:800])
    g2[n:800] = np.zeros_like(g2[n:800])
    b2[n:800] = np.zeros_like(b2[n:800])
    
    # creating diagonal matrix to perform dot multiplication
    #change the dimension of r2 to (800,1000), since original r2 from linalg.svd is (800,1)
    #can check dimension with r2.shape
    r2 = linalg.diagsvd(r2,800,1000)
    g2 = linalg.diagsvd(g2,800,1000)
    b2 = linalg.diagsvd(b2,800,1000)
    
    # perform dot multiplication to create lower resolutuion mariric 
    r_new = np.dot(r1, np.dot(r2, r3))
    g_new = np.dot(g1, np.dot(g2, g3))
    b_new = np.dot(b1, np.dot(b2, b3))
      
    img[:,:,0]=r_new
    img[:,:,1]=g_new
    img[:,:,2]=b_new
    
    fig2 = plt.figure(2)
    ax1 = fig2.add_subplot(2,2,1)
    ax2 = fig2.add_subplot(2,2,2)
    ax3 = fig2.add_subplot(2,2,3)
    ax4 = fig2.add_subplot(2,2,4)
    ax1.imshow(img)
    ax2.imshow(r_new, cmap = 'Reds')
    ax3.imshow(g_new, cmap = 'Greens')
    ax4.imshow(b_new, cmap = 'Blues')
    plt.show() 
    


#the original set
img=mpimg.imread('SnakeDance.jpg')
img_ori = copy.deepcopy(img)
[r,g,b] = [img[:,:,i] for i in range(3)]
fig = plt.figure(1)
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)
ax1.imshow(img_ori)
ax2.imshow(r, cmap = 'Reds')
ax3.imshow(g, cmap = 'Greens')
ax4.imshow(b, cmap = 'Blues')
plt.show()


#keep the first n none zero elements in sigma.input n into image_svd.
#image_svd(30)


image_svd(200)


