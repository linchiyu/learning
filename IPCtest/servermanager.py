# In the first Python interactive shell

import cv2
import time
import numpy as np
from managers import SharedMemoryManager
from multiprocessing import shared_memory
from functools import partial


class ImageManager(SharedMemoryManager):
    pass

def getshm1(shm, **kwargs):
	#print(shm, kwargs)
	img = np.ndarray((700,700,3), dtype=np.uint8, buffer=shm.buf)
	return img

if __name__ == '__main__':

	img = cv2.imread('f1.jpg')

	img = cv2.resize(img, (700,700))
	#img = np.zeros((700,700,3), dtype=np.uint8)

	#shm = shared_memory.SharedMemory(name='aaa', create=True, size=img.nbytes)
	#SharedMemoryManager.register('getSharedMemory', callable=lambda:shm)
	shm = shared_memory.SharedMemory(name='uniquename', create=True, size=img.nbytes)
	b = np.ndarray((700,700,3), dtype=np.uint8, buffer=shm.buf)
	print(type(shm))
	ImageManager.register('getSharedMemory', callable=partial(getshm1, shm))

	#smm = ImageManager(address=('127.0.0.1', 50000), authkey=b'abc')
	smm = ImageManager(address=('127.0.0.1', 50000), authkey=b'articfoxmemoryauthkey')

	smm.start()

	#print(smm._number_of_objects())
	#print(shm.__dict__)
	# Now create a NumPy array backed by shared memory
	#b = np.ndarray(img.shape, dtype=img.dtype, buffer=shm.buf)
	b[:] = img[:]  # Copy the original data into shared memory

	print('server started - run client now')

	#time.sleep(20)
	input()
	img = np.zeros((700,700,3), dtype=np.uint8)

	b[:] = img[:]
	input()
	smm.shutdown()
	shm.close()
	shm.unlink()


	print('server end')

