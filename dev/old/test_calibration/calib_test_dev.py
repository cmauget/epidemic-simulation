from calibration_dev import calibModelDev
import matplotlib.pyplot as plt

model = calibModelDev()

out, fitted_curve, data, name_comp = model.calib("config_SIR_example.json",25, method='powell')

print(out.params)

plt.plot(fitted_curve[1,:])
plt.plot(data[name_comp[1]], '+')
plt.show()
