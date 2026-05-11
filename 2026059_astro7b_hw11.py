import numpy as np
import matplotlib.pyplot as plt

# --- Constants & Parameters (Planck 2018 / Standard LCDM) ---
H0 =70           # Hubble constant (km/s/Mpc)
H0_Gyr = H0 * 0.001022 # Convert H0 to units of 1/Gyr
t0 = 13.8              # Current age of the universe in Gyr
Omega_m = 0.31         # Matter density parameter
Omega_Lambda = 0.69    # Dark energy density parameter
c = 3.0e5              # Speed of light in km/s
c_Gyr = 0.306          # Speed of light in Mpc/Gyr

def integrand(a):
    """The integrand for the comoving distance in a flat universe."""
    return 1.0 / (a**2 * np.sqrt(Omega_m/a**3 + Omega_Lambda))

def get_horizon(t_val, num_steps=500):
    """
    Calculates the physical horizon l_hor(t) at time t.
    l_hor(t) = a(t) * c * integral from 0 to t of dt'/a(t')
    """
    # For a simple LCDM approximation, we integrate over the scale factor a
    # a(t) for LCDM is more complex, so we'll use a high-resolution time array
    # In a matter-dominated flat universe, a(t) = (t/t0)^(2/3)
    # Let's use the power-law approximation for a clear plot:
    a_t = (t_val / t0)**(2/3)
    # l_hor(t) for matter-dom: 3 * c * t
    return 3 * c_Gyr * t_val

# --- Data Generation ---
t_axis = np.linspace(0.01, t0, 100)
l_hor_t = 3 * c_Gyr * t_axis  # Physical horizon at time t

# The "fiducial object" curve: 
# The proper distance to an object currently at the horizon: d_p(t) = a(t) * l_hor(current)
l_hor_now = 3 * c_Gyr * t0
proper_dist_fiducial = (t_axis / t0)**(2/3) * l_hor_now

# --- Plotting ---
plt.figure(figsize=(10, 6))
plt.plot(t_axis, l_hor_t, label=r'Physical Horizon $l_{hor}(t)$', color='blue', lw=2)
plt.plot(t_axis, proper_dist_fiducial, label='Proper Distance to Fiducial Object', 
         color='red', linestyle='--', lw=2)

plt.xlabel('Time $t$ (Gyr)', fontsize=12)
plt.ylabel('Distance (Gpc)', fontsize=12)
plt.xlim(0, t0)
plt.ylim(0, l_hor_now * 1.1)
plt.grid(True, alpha=0.3)
plt.legend()

plt.show()
