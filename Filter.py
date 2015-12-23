def g_h_filter(data, x0, dx, g, h, dt):
    x = x0
    pred = [x0]
    estimates = []
    for z in data:
        # prediction
        x_pred = x + dx * dt
        pred.append(x_pred)
        
        # update
        residual = z - x_pred
        dx = dx + h * residual / dt
        x = x_pred + g * residual
        estimates.append(x)
    
    return estimates


def k_filter(data, x0, P, Q, R):
    x_pred = [x0]
    P_pred = []
    
    x_est = []
    P_est = [P]
    K_gain = []
    
    for i in range(len(data)):
        # prediction
        x_pred.append(x_pred[-1])
        P_pred.append(P_est[-1] + Q)
    
        # update
        K_gain.append(P_pred[-1] / (P_pred[-1] + R))
        x_est.append(x_pred[-1] + K_gain[-1] * (data[i] - x_pred[-1]))
        P_est.append(1 - K_gain[-1] * P_pred[-1])
    
    return x_est