import numpy as np
import matplotlib.pyplot as plt

# --- 1. SYSTEM PARAMETERS (Prototype Scale) ---
# Defining the physical characteristics and constants for the simulation.
Rotor_Radius = 0.5      # meters
Rotor_Area = np.pi * (Rotor_Radius**2)
PV_Area = 0.45          # m²
Load_Power = 40         # Watts (A constant consumer load)

# Battery Parameters
Battery_Capacity_Ah = 100 # Ah
Battery_Voltage = 12      # V
Battery_Capacity_Wh = Battery_Capacity_Ah * Battery_Voltage # 1200 Wh
Initial_SOC = 0.5       # Starting State of Charge (50% represented as a fraction)

# Efficiencies
Wind_Eff = 0.40         # Wind power coefficient (Cp)
Solar_Eff = 0.20        # PV cell efficiency
Controller_Eff = 0.90   # Hybrid Charge Controller efficiency

# --- 2. PHYSICS MODELS ---

def calculate_wind_power(V_wind):
    """Calculates wind power (P = 0.5 * rho * A * V^3 * Cp)."""
    rho = 1.225 # Air density in kg/m³
    P_wind = 0.5 * rho * Rotor_Area * (V_wind**3) * Wind_Eff
    return P_wind

def calculate_solar_power(G_irradiance):
    """Calculates solar power (P = G * A * Efficiency)."""
    P_solar = G_irradiance * PV_Area * Solar_Eff
    return P_solar

def update_soc(prev_SOC_Wh, P_net_W, time_step_h):
    """Updates the Battery State of Charge (Wh) over a time step, considering controller loss."""
    Energy_transfer_Wh = P_net_W * time_step_h
    
    if Energy_transfer_Wh > 0:
        # Charging: Apply charge controller efficiency loss
        Energy_added = Energy_transfer_Wh * Controller_Eff
        new_SOC_Wh = np.clip(prev_SOC_Wh + Energy_added, 0, Battery_Capacity_Wh)
    else:
        # Discharging: Apply inverse efficiency loss
        Energy_subtracted = abs(Energy_transfer_Wh) / Controller_Eff
        new_SOC_Wh = np.clip(prev_SOC_Wh - Energy_subtracted, 0, Battery_Capacity_Wh)
        
    return new_SOC_Wh

# --- 3. SIMULATION INPUT DATA (24-Hour Cycle) ---

Time_Steps = 96 # 96 steps for 24 hours (15 minutes per step)
Time_Step_h = 24 / Time_Steps # 0.25 hours

# Time array for both power and SOC data (starts at 0.00 for clean plotting)
Hours = np.linspace(0, 24, Time_Steps) 

# A. Solar Irradiance (G) - Peaks at Noon, zero at night
G_max = 950 # W/m²
G_irradiance = G_max * np.maximum(0, np.sin(np.pi * (Hours - 6) / 12)) 
G_irradiance *= (1 + 0.05 * np.random.randn(Time_Steps))
G_irradiance = np.clip(G_irradiance, 0, G_max)

# B. Wind Speed (V) - Stronger at night/morning to show complementarity
Wind_Base = 5 # m/s
Wind_Speed = Wind_Base + 2.5 * np.sin(2 * np.pi * (Hours - 6) / 24) 
Wind_Speed += 1.0 * np.random.randn(Time_Steps)
Wind_Speed = np.clip(Wind_Speed, 0, 15)

# --- 4. PRE-CALCULATE ALL DATA POINTS ---
P_wind_data = []
P_solar_data = []
SOC_Wh_data = [Initial_SOC * Battery_Capacity_Wh]

current_SOC_Wh = Initial_SOC * Battery_Capacity_Wh

for i in range(Time_Steps):
    P_wind = calculate_wind_power(Wind_Speed[i])
    P_solar = calculate_solar_power(G_irradiance[i])
    P_generated = P_wind + P_solar
    P_net = P_generated - Load_Power
    
    current_SOC_Wh = update_soc(current_SOC_Wh, P_net, Time_Step_h)
    
    P_wind_data.append(P_wind)
    P_solar_data.append(P_solar)
    SOC_Wh_data.append(current_SOC_Wh)

# We need 96 power points (calculated at each time step) and 97 SOC points (initial + 96 steps).
# For plotting power data against time, we truncate the time array to 96 points for alignment.
Plot_Hours_Power = Hours[1:] # Use 96 points for power: [0.25, 0.5, ..., 24.0]

# For plotting SOC data, we use the full 97 points
Plot_Hours_SOC = np.linspace(0, 24, Time_Steps + 1) # [0.0, 0.25, ..., 24.0]

Total_Power_data = np.array(P_wind_data) + np.array(P_solar_data)
SOC_percent_data = (np.array(SOC_Wh_data) / Battery_Capacity_Wh) * 100

# --- 5. RESULTS AND VISUALIZATION (Static Plot) ---

plt.figure(figsize=(14, 12))

# Subplot 1: Power Generation and Load
plt.subplot(2, 1, 1)
# Note: Using the first 96 points of the Hours array (or Plot_Hours_Power) aligns with the 96 data points
plt.plot(Hours, P_solar_data, label='Solar (PV Blades) Power (W)', color='#FFC300', linewidth=2)
plt.plot(Hours, P_wind_data, label='Wind Power (W)', color='#4DB3E6', linewidth=2)
plt.plot(Hours, Total_Power_data, label='Total Hybrid Power (W)', color='#1E8449', linewidth=3, linestyle='-')
plt.axhline(y=Load_Power, color='r', linestyle=':', label=f'Constant Load ({Load_Power}W)', linewidth=2)

plt.title('Hybrid System Performance: Complementary Power Generation', fontsize=18, fontweight='bold')
plt.xlabel('Time of Day (Hours)', fontsize=14)
plt.ylabel('Power Output (Watts)', fontsize=14)
plt.legend(loc='upper right', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.xlim(0, 24)


# Subplot 2: Battery State of Charge
plt.subplot(2, 1, 2)
# Note: Using the 97-point Plot_Hours_SOC array for the 97-point SOC data
plt.plot(Plot_Hours_SOC, SOC_percent_data, label='Battery State of Charge (%)', color='#6A1B9A', linewidth=3)
plt.axhline(y=100, color='g', linestyle='--', alpha=0.6, label='100% Max Capacity')
plt.axhline(y=20, color='r', linestyle='--', alpha=0.6, label='20% Critical Low (Avoid)')

plt.title('System Reliability: Battery State of Charge (SOC)', fontsize=18, fontweight='bold')
plt.xlabel('Time of Day (Hours)', fontsize=14)
plt.ylabel('State of Charge (%)', fontsize=14)
plt.ylim(0, 105)
plt.xlim(0, 24)
plt.legend(loc='upper right', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout(pad=3.0)
plt.show()

print("\n--- Simulation Summary ---")
print(f"Initial SOC: {Initial_SOC * 100:.2f}%")
print(f"Final SOC: {SOC_percent_data[-1]:.2f}%")
print("The static graph now displays the full 24-hour simulation results without the Colab module error.")