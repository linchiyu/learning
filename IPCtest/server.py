# In the first Python interactive shell
import time
import numpy as np
import cv2

img = cv2.imread('f1.jpg')

img = cv2.resize(img, (700,700))

a = np.ones((100,100,3), np.int8)  # Start with an existing NumPy array
from multiprocessing import shared_memory
shm = shared_memory.SharedMemory(name='uniquememoryname', create=True, size=img.nbytes)
# Now create a NumPy array backed by shared memory
print(shm.buf)
b = np.ndarray(img.shape, dtype=img.dtype, buffer=shm.buf)
print(img.shape)
print(img.dtype)
b[:] = img[:]  # Copy the original data into shared memory

print(type(b))
print(type(a))
print('server started - run client now')

#time.sleep(10)
input()


# Clean up from within the first Python shell
print(b)
del b  # Unnecessary; merely emphasizing the array is no longer used
shm.close()
shm.unlink()  # Free and release the shared memory block at the very end
print('server end')

