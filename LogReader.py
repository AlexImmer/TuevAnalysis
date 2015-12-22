def read_acc_log(line):
    x_pos = line.find('x:')
    y_pos = line.find('y:')
    z_pos = line.find('z:')
    x = float(line[x_pos+3:y_pos -1])
    y = float(line[y_pos+3:z_pos -1])
    z = float(line[y_pos+3:])
    return x, y, z
       
def read_alert_log(line):
    return line[line.find('(:')+3]

def read_device_log(filename):
    res = {
        'acc_x' : [],
        'acc_y' : [],
        'acc_z' : [],
        'gps' : [],
        'time' : [],
        'alert' : []
    }
    for line in open(filename):
        if line.startswith('D/CAAccData'):
            gy = read_acc_log(line)
            res['acc_x'].append(gy[0])
            res['acc_y'].append(gy[1])
            res['acc_z'].append(gy[2])
        elif line.startswith('I/CrashAlert'):
            res['alert'].append(read_alert_log(line))
        elif line.startswith('D/CrashAlertGPS'):
            pass
        elif line.startswith('D/CAAccTime'):
            pass