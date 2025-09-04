import numpy as np
import matplotlib.pyplot as plt

# Load data
fig, ax = plt.subplots(figsize=(20,10))
data = np.loadtxt('lab 3 comparator circuit outout.txt', delimiter=',')

# Plot
plt.plot(data[:, 0], data[:, 1], linestyle = "-", label="Comparator output")
plt.plot(data[:, 0], data[:, 2], linestyle = "--", label="LDR V out (V)")
plt.plot(data[:, 0], data[:, 3], linestyle = "-.", label = "Potentiometer V out (V)")
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")



plt.legend()
plt.title('Oscilloscope output from comparator circuit, with LDR-motor setup and potentiometer')
plt.grid()
plt.savefig("Lab 3 first exercise circuit.png")
plt.show()
