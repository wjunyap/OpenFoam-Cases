import numpy as np
import matplotlib.pyplot as plt
# Load (skip lines starting with '#')
data = np.loadtxt("postProcessing/forceCoeffs/0/coefficient.dat", comments="#")
t  = data[:, 0]
Cd = data[:, 1]
Cl = data[:, 4]
# Drop transient phase (first 25% of run)
mask = t > 0.7 * t.max()
t, Cd, Cl = t[mask], Cd[mask], Cl[mask]
# adjustTimeStep produces non-uniform Δt. Resample to uniform.
dt_target = np.median(np.diff(t))
t_uni  = np.arange(t[0], t[-1], dt_target)
Cl_uni = np.interp(t_uni, t, Cl)
Cd_uni = np.interp(t_uni, t, Cd)
# FFT of (Cl - mean) to find the dominant frequency
N      = len(Cl_uni)
freqs  = np.fft.rfftfreq(N, d=dt_target)
spec   = np.abs(np.fft.rfft(Cl_uni - Cl_uni.mean()))
peak_idx = np.argmax(spec[1:]) + 1     # exclude DC bin
f_shed   = freqs[peak_idx]
# Reference quantities
U_inf, D = 1.0, 5.0
St = f_shed * D / U_inf
print(f"Mean Cd       : {Cd_uni.mean():.4f}")
print(f"RMS Cl        : {np.std(Cl_uni):.4f}")
print(f"Peak Cl       : {np.max(np.abs(Cl_uni)):.4f}")
print(f"Shedding freq : {f_shed:.4f} Hz")
print(f"Strouhal      : {St:.4f}")
print(f"Period        : {1/f_shed:.4f} s")
# Plot
fig, axes = plt.subplots(2, 1, figsize=(10, 6))
axes[0].plot(t_uni, Cl_uni, label="Cl")
axes[0].plot(t_uni, Cd_uni - Cd_uni.mean(), alpha=0.6, label="Cd - mean")
axes[0].set_xlabel("Time (s)"); axes[0].set_ylabel("Coefficient")
axes[0].legend(); axes[0].grid(True)
axes[1].plot(freqs, spec)
axes[1].axvline(f_shed, color="r", ls="--", label=f"f = {f_shed:.4f} Hz")
axes[1].set_xlim(0, 0.2); axes[1].set_xlabel("Frequency (Hz)")
axes[1].set_ylabel("Cl spectrum"); axes[1].legend(); axes[1].grid(True)
plt.tight_layout(); plt.savefig("strouhal.png", dpi=150)
plt.show()
