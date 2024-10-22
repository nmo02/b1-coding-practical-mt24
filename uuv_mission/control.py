class PDController:
    def __init__(self, kp: float, kd: float):
        self.kp = kp  # Proportional gain
        self.kd = kd  # Derivative gain
        self.prev_error = 0  # Store the previous error (e[t-1])

    def control(self, error: float) -> float:
    
        #Calculate the control action u[t] = KP * e[t] + KD * (e[t] - e[t-1])
       
        derivative = error - self.prev_error  # (e[t] - e[t-1])
        control_action = self.kp * error + self.kd * derivative
        self.prev_error = error  # Update the previous error
        return control_action