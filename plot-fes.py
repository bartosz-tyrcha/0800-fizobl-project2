import numpy as np
import matplotlib.pyplot as plt


T = 300  # K
k = 1.380649e-26  # kJ/K

a = 4.141947e-24  # [a * kT] = [kJ]
N_A = 6.02214076e23  # avogadro number

d1_all = []
free_all = []

plt.figure()

for i in range(10):
    file_name = "irtg-school-mainz-2020-metad/fes_{0}.dat".format(int((i + 1) * 10))
    d1, free, der_d1 = np.loadtxt(file_name, unpack=True)  # free energy is in kJ/mol
    d1_all.append(d1)
    free_all.append(free)

free_min = np.min(free_all[-1])

for i in range(10):
    free_all[i] = (free_all[i] - free_min) / (k * T * N_A)
    plt.plot(d1_all[i], free_all[i], label="{0} ns".format(i))

plt.xlabel("Odległość Na-Cl [nm]")
plt.ylabel("Energia swobodna [kT]")
plt.legend()
plt.savefig("fes_metad.png")
plt.close()
