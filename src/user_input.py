import numpy as np

#   Calculates Shock Turn Angle Theta
#   (copied code from oblique_shock.py)
def theta_calc(m1, gamma, beta):
    tan_theta = 2 * (1 / np.tan(beta_rad)) * ((m1 ** 2 * np.sin(beta_rad) ** 2 - 1) / (m1 ** 2 * (gamma + np.cos(2 * beta_rad)) + 2))
    theta_rad = np.atan(tan_theta)

    return theta_rad

#   Waveride Dimensions
desL = 10  # Length of Body
H = 3.5 # Height of Body Over Shock Cone at the rear
W = 9   # Width of Vehicle at the tail end

#   Basic Flowfield
M1 = 5
gamma = 1.4
# beta = 19.29
# beta_rad = np.radians(beta)
beta_rad = np.arctan(H/desL)
beta = (beta_rad * 180)/np.pi
theta_rad = theta_calc(M1, gamma, beta_rad)

#   Define TE constants
L = 18                                # Max. Length (See User Menu)
Rs = L * np.tan(beta_rad)    # Trailing Edge Parameter (See User Menu)
R1 = .5 * Rs                        # Trailing Edge Parameter (See User Menu)
W2 = 0.6429 * Rs                        # Trailing Edge Parameter (See User Menu)

#   Resolution
N = 500                      # Leading Edge Resolution (500 or more is recommended!)
N_l = 12                     # Lower Surface Resolution
N_up = 10                    # Upper Surface Resolution

#   Trailing Edge Curve
a = -R1
b = 2 * (R1 - np.sqrt(Rs**2 - W2**2)) / W2**2
c = (np.sqrt(Rs**2 - W2**2) - R1) / W2**4

#   Trailing Edge Function
def z(y):
    func = a + b * y**2 + c * y**4    # Define Your Own Trailing Edge Function
    return func

