import numpy as np
import matplotlib.pyplot as plt

# Model parameters (starting estimates — we'll tune these later)
R_s = 0.1      # Ohmic/membrane resistance (ohms)
R_ct = 0.3     # Charge transfer resistance (ohms)
C_dl = 1e-3    # Double layer capacitance (farads)

# Frequency sweep
f = np.logspace(-1, 7, 1000)  # 0.1Hz to 10MHz
omega = 2 * np.pi * f       # Angular frequency

# Impedance of parallel R_ct and C_dl
Z_parallel = R_ct / (1 + 1j * omega * R_ct * C_dl)

# Total impedance
Z_total = R_s + Z_parallel

# Extract real and imaginary parts
Z_real = np.real(Z_total)
Z_imag = np.imag(Z_total)

# Plot Nyquist (standard EIS visualization)
plt.figure(figsize=(7, 5))
plt.plot(Z_real, -Z_imag, 'b.-')
plt.xlabel("Z_real (Ω)")
plt.ylabel("-Z_imag (Ω)")
plt.title("Nyquist Plot — PEM Fuel Cell (Simulated)")
plt.grid(True)
plt.axis('equal')
plt.tight_layout()
plt.savefig("nyquist_simulated.png")
plt.show()

print("Done. Plot saved as nyquist_simulated.png")