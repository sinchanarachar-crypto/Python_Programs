import numpy as np
import matplotlib.pyplot as plt

# -------------------------------
# 1. SYSTEM PARAMETERS
# -------------------------------
Rotor_Radius = 0.5  # meters
Rotor_Area = np.pi * Rotor_Radius**2
PV_Area = 0.45      # m²
Battery_Capacity_Ah = 100
Battery_Voltage = 12
Battery_Capacity_Wh = Battery_Capacity_Ah * Battery_Voltage
Load_Power = 35  # Watts

# Efficiencies
Wind_Eff = 0.40
Solar_Eff = 0.20
Controller_Eff = 0.90

# -------------------------------
# 2. PHYSICS MODELS
# -------------------------------
def calculate_wind_power(V, area, eff=Wind_Eff):
    rho = 1.225  # kg/m³
    return 0.5 * rho * area * V**3 * eff

def calculate_solar_power(G, area, eff=Solar_Eff):
    return G * area * eff

def update_soc(prev_soc, net_power, dt, max_capacity):
    if net_power > 0:
        added = net_power * dt * Controller_Eff
        new_soc = np.clip(prev_soc + added, 0, max_capacity)
    else:
        subtracted = abs(net_power * dt / Controller_Eff)
        new_soc = np.clip(prev_soc - subtracted, 0, max_capacity)
    return new_soc

# -------------------------------
# 3. SIMULATION SETUP
# -------------------------------
np.random.seed(42)  # For reproducibility
Time_Steps = 96
Time_Step_h = 24 / Time_Steps
Hours = np.linspace(0, 24, Time_Steps)

# Solar Irradiance
G_max = 1000
G_irradiance = G_max * np.maximum(0, np.sin(np.pi * (Hours - 6) / 12))
G_irradiance *= (1 + 0.1 * np.random.randn(Time_Steps))
G_irradiance = np.clip(G_irradiance, 0, G_max)

# Wind Speed
Wind_Base = 6
Wind_Speed = Wind_Base + 3 * np.sin(2 * np.pi * Hours / 24)
Wind_Speed += 1.5 * np.random.randn(Time_Steps)
Wind_Speed = np.clip(Wind_Speed, 0, 15)

# -------------------------------
# 4. SIMULATION EXECUTION
# -------------------------------
P_wind_hist = np.zeros(Time_Steps)
P_solar_hist = np.zeros(Time_Steps)
P_net_hist = np.zeros(Time_Steps)
SOC_hist_Wh = np.zeros(Time_Steps)

current_SOC = 0.5 * Battery_Capacity_Wh

for i in range(Time_Steps):
    P_wind = calculate_wind_power(Wind_Speed[i], Rotor_Area)
    P_solar = calculate_solar_power(G_irradiance[i], PV_Area)
    P_total = P_wind + P_solar
    P_net = P_total - Load_Power
    current_SOC = update_soc(current_SOC, P_net, Time_Step_h, Battery_Capacity_Wh)

    P_wind_hist[i] = P_wind
    P_solar_hist[i] = P_solar
    P_net_hist[i] = P_net
    SOC_hist_Wh[i] = current_SOC

SOC_hist_percent = (SOC_hist_Wh / Battery_Capacity_Wh) * 100

# -------------------------------
# 5. VISUALIZATION
# -------------------------------
plt.figure(figsize=(14, 10))

# Power Generation
plt.subplot(2, 1, 1)
plt.plot(Hours, P_solar_hist, label='Solar Power (W)', color='orange')
plt.plot(Hours, P_wind_hist, label='Wind Power (W)', color='skyblue')
plt.plot(Hours, P_solar_hist + P_wind_hist, label='Total Hybrid Power (W)', color='green', linestyle='--', linewidth=2)
plt.axhline(y=Load_Power, color='red', linestyle=':', label=f'Load ({Load_Power}W)')
plt.title('Hybrid Power Generation vs Load')
plt.xlabel('Time (Hours)')
plt.ylabel('Power (W)')
plt.grid(True)
plt.legend()

# Battery SOC
plt.subplot(2, 1, 2)
plt.plot(Hours, SOC_hist_percent, label='Battery SOC (%)', color='purple', linewidth=3)
plt.axhline(y=100, color='green', linestyle='--', alpha=0.6, label='Max Capacity')
plt.axhline(y=20, color='red', linestyle='--', alpha=0.6, label='Min SOC Threshold')
plt.title('Battery State of Charge Over Time')
plt.xlabel('Time (Hours)')
plt.ylabel('SOC (%)')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()

# -------------------------------
# 6. SUMMARY
# -------------------------------
print(f"\nSimulation Complete. Final SOC: {SOC_hist_percent[-1]:.2f}%")
if np.any(SOC_hist_percent < 20):
    print("⚠️ Warning: Battery SOC dropped below 20% — potential reliability issue.")
else:
    print("✅ Battery SOC remained above critical threshold throughout the day.")