import asyncio
import cv2
import time

# In either the same shell or a new Python shell on the same machine
import numpy as np
import time
from multiprocessing import shared_memory
from multiprocessing.managers import SharedMemoryManager
# Attach to the existing shared memory block.
class ImageManager(SharedMemoryManager):
    pass
if __name__ == '__main__':
	ImageManager.register('getSharedMemory')
	smm = ImageManager(address=('127.0.0.1', 50000), authkey=b'abc')
	smm.connect()
	print(time.time())
	existing_shm = smm.getSharedMemory()
	print(time.time())
	x = existing_shm.copy()
	print(time.time())

	cv2.imshow('img', existing_shm.copy())
	cv2.waitKey()
	#what do i do now to acess the img from server
	'''img = np.ndarray((700,700,3), dtype=np.uint8, buffer=existing_shm.get_buf())

	cv2.imshow('img', img)
	cv2.waitKey()
	existing_shm.close()'''