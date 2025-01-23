import numpy as np


#   Waverider Body Dimensions
desL = 3.6  # Length of Body (meters)
W = 2.6     # Width of Vehicle at the tail end (meters)
H = 1.7     # Height of Body Over Shock Cone at the rear (meters)


#   Basic Flowfield
M1 = 5
gamma = 1.4

#   Manual Tuning
# beta = 19.29
# beta_rad = np.radians(beta)
#   Body Dimension Tuner
beta_rad = np.arctan(H / desL)
beta = (beta_rad * 180) / np.pi


#   Define TE constants

#   Manual Tuning
# L = 20
#   Body Dimension Tuner
L = 2*desL  # Max. Length (See User Menu)

Rs = L * np.tan(beta_rad)  # Trailing Edge Parameter (See User Menu)

#   Manual Tuning
# R1_multiplier = 0.5
# W2_multiplier = 0.45
#   Body Dimension Tuner
R1_multiplier = 0.5
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
