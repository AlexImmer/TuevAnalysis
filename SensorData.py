class SensorData(object):
    def __init__(self, x, y, z, gps, time, alert):
        self.x = x
        self.y = y
        self.z = z
        self.speed = gps
        self.time = time
        self.alerts = alert