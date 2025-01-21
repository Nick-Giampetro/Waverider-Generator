import numpy as np


#   Waverider Body Dimensions
desL = 10   # Length of Body
W = 10       # Width of Vehicle at the tail end
H = 10     # Height of Body Over Shock Cone at the rear


#   Basic Flowfield
M1 = 5
gamma = 1.4
# beta = 19.29
# beta_rad = np.radians(beta)
beta_rad = np.arctan(H / desL)
beta = (beta_rad * 180) / np.pi



#   Define TE constants
L = 2*desL  # Max. Length (See User Menu)
Rs = L * np.tan(beta_rad)  # Trailing Edge Parameter (See User Menu)

# Manual Tuning
#R1_multiplier = 0.5
#W2_multiplier = 0.45

# Body dimension Tunner
R1 = Rs-H
R1_multiplier = R1/Rs
W2_multiplier = (W/2)/Rs

R1 = R1_multiplier * Rs  # Trailing Edge Parameter (See User Menu)
W2 = W2_multiplier * Rs  # Trailing Edge Parameter (See User Menu)

#   Resolution
N = 500  # Leading Edge Resolution (500 or more is recommended!)
N_l = 12  # Lower Surface Resolution
N_up = 10  # Upper Surface Resolution

#   Trailing Edge Curve
a = -R1
b = 2 * (R1 - np.sqrt(Rs ** 2 - W2 ** 2)) / W2 ** 2
c = (np.sqrt(Rs ** 2 - W2 ** 2) - R1) / W2 ** 4


#   Trailing Edge Function
def z(y):
    func = a + b * y ** 2 + c * y ** 4  # Define Your Own Trailing Edge Function
    return func
