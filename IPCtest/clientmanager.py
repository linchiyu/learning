import asyncio
import cv2
import time
from multiprocessing.managers import SharedMemoryManager as Manager

import sys

if sys.version_info < (3, 9):
    from multiprocessing.managers import Server, SharedMemoryServer

    def create(self, c, typeid, /, *args, **kwargs):
        if hasattr(self.registry[typeid][-1], "_shared_memory_proxy"):
            kwargs['shared_memory_context'] = self.shared_memory_context
        return Server.create(self, c, typeid, *args, **kwargs)

    SharedMemoryServer.create = create

# In either the same shell or a new Python shell on the same machine
import numpy as np
from multiprocessing import shared_memory
from multiprocessing.managers import SharedMemoryManager
# Attach to the existing shared memory block.
class ImageManager(SharedMemoryManager):
    pass
if __name__ == '__main__':
	ImageManager.register('getSharedMemory')
	smm = ImageManager(address=('127.0.0.1', 50000), authkey=b'abc')
	smm.connect()
	existing_shm = smm.getSharedMemory()
	print(smm._Client(('127.0.0.1', 50000)))
	#what do i do now to acess the img from server
	'''img = np.ndarray((700,700,3), dtype=np.uint8, buffer=existing_shm.get_buf())

	cv2.imshow('img', img)
	cv2.waitKey()
	existing_shm.close()'''