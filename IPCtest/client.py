import asyncio
import cv2
import time

# In either the same shell or a new Python shell on the same machine
import numpy as np
from multiprocessing import shared_memory
# Attach to the existing shared memory block
existing_shm = None
existing_shm = shared_memory.SharedMemory(name='wnsm_609e5168')
print(existing_shm.buf)

# Note that a.shape is (6,) and a.dtype is np.int64 in this example
x = np.zeros((700,700,3), dtype=np.uint8)
img = np.ndarray((700,700,3), dtype=np.uint8, buffer=existing_shm.buf)

#print(img)
cv2.imshow('img', img)
# Back in the first Python interactive shell, b reflects this change

k = cv2.waitKey()

# Clean up from within the second Python shell
#del c  # Unnecessary; merely emphasizing the array is no longer used
existing_shm.close()