import paho.mqtt.publish as publish

import numpy as np

#mat = np.zeros((10,10))
#print(mat)
publish.single("paho/test/", 3, hostname="localhost")
