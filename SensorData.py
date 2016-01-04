import numpy as np


class SensorData(object):
    def __init__(self, x, y, z, gps, time, alert):
        self.x = x
        self.y = y
        self.z = z
        self.speed = gps
        self.time = self.to_secs(time)
        self.alerts = alert
        self.acc = 0
        
    def acc_force(self):
        rms = self.x ** 2 + self.y ** 2 + self.z ** 2
        return np.sqrt(rms)
    
    @classmethod
    def to_secs(cls, t):
        h = int(t[:2])
        m = int(t[3:5])
        s = int(t[6:])
        return 60 ** 2 * h + 60 * m + s

    
def add_speed(sensors):
    init_spd = 0
    for i in range(len(sensors)):
        sensors[i].acc = (sensors[i].speed - init_spd) * 1000/3600
        init_spd = sensors[i].speed
       