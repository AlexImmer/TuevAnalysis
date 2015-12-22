from SensorData import SensorData

def read_acc_log(line):
    x_pos = line.find('x:')
    y_pos = line.find('y:')
    z_pos = line.find('z:')
    x = float(line[x_pos+3:y_pos -1])
    y = float(line[y_pos+3:z_pos -1])
    z = float(line[z_pos+3:])
    return x, y, z
       
def read_alert_log(line):
    return line[line.find('):')+3:]

def read_gps_log(line):
    return float(line[line.find('):')+3:])

def read_time_log(line):
    pos = line.find('Europe')-9
    return line[pos:pos+8]

def avg_acc(d):
    size = len(d)
    if size == 0:
        return 0, 0, 0
    x = sum([x[0] for x in d])/size
    y = sum([y[1] for y in d])/size
    z = sum([z[2] for z in d])/size
    return x, y, z

def read_device_log(filename):
    res = {
        'acc_x' : [],
        'acc_y' : [],
        'acc_z' : [],
        'gps' : [],
        'time' : [],
        'alert' : []}
    
    for line in open(filename):
        if line.startswith('D/CAAccData'):
            gy = read_acc_log(line)
            res['acc_x'].append(gy[0])
            res['acc_y'].append(gy[1])
            res['acc_z'].append(gy[2])
        elif line.startswith('I/CrashAlert'):
            res['alert'].append(read_alert_log(line))
        elif line.startswith('D/CrashAlertGPS'):
            res['gps'].append(read_gps_log(line))
        elif line.startswith('D/CAAccTime'):
            res['time'].append(read_time_log(line))
    return res 

def device_log_to_sensordata(filename):
    sensordata = []
    g_acc = []
    alerts = []
    gps = [0]
    
    for line in open(filename):
        if line.startswith('D/CAAccData'):
            g_acc.append(read_acc_log(line))
        elif line.startswith('I/CrashAlert'):
            alerts.append(read_alert_log(line))
        elif line.startswith('D/CrashAlertGPS'):
            gps.append(read_gps_log(line))
        elif line.startswith('D/CAAccTime'):
            time = read_time_log(line)
            accs = avg_acc(g_acc)
            sd = SensorData(accs[0], accs[1], accs[2], gps[-1], time, alerts)
            sensordata.append(sd)
            g_acc = []
            alerts = []
    
    return sensordata