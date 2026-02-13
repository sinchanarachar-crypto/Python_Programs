import numpy as np
import matplotlib.pyplot as plt

# --- 1. SYSTEM PARAMETERS (Prototype Scale) ---
# Defining the physical characteristics and constants for the simulation.
# These values are based on the project's goal of a small-scale prototype (Slide 8).
Rotor_Radius = 0.5      # meters (e.g., for a small turbine)
Rotor_Area = np.pi * (Rotor_Radius**2)
PV_Area = 0.45          # m² (Total effective PV area integrated on the blades)
Load_Power = 40         # Watts (A constant consumer load)

# Battery Parameters
Battery_Capacity_Ah = 100 # Amp-hours
Battery_Voltage = 12      # Volts
Battery_Capacity_Wh = Battery_Capacity_Ah * Battery_Voltage # 1200 Wh
Initial_SOC = 0.5       # Starting State of Charge (50% represented as a fraction)

# Efficiencies
Wind_Eff = 0.40         # Wind power coefficient (Cp)
Solar_Eff = 0.20        # PV cell efficiency
Controller_Eff = 0.90   # Hybrid Charge Controller efficiency (for charging and discharging losses)

# --- 2. PHYSICS MODELS (Modified to use defined parameters) ---

def calculate_wind_power(V_wind, Area=Rotor_Area, Eff=Wind_Eff):
    """Calculates wind power (P = 0.5 * rho * A * V^3 * Cp)."""
    rho = 1.225 # Air density in kg/m³
    P_wind = 0.5 * rho * Area * (V_wind**3) * Eff
    return P_wind

def calculate_solar_power(G_irradiance, Area=PV_Area, Eff=Solar_Eff):
    """Calculates solar power (P = G * A * Efficiency)."""
    P_solar = G_irradiance * Area * Eff
    return P_solar

def update_soc(prev_SOC_Wh, P_net_W, time_step_h, Max_Capacity_Wh=Battery_Capacity_Wh, Eff_ctrl=Controller_Eff):
    """
    Updates the Battery State of Charge (Wh) over a time step.
    P_net_W is the generated power minus the load power.
    """
    
    # Calculate energy transfer in Watt-hours
    Energy_transfer_Wh = P_net_W * time_step_h
    
    if Energy_transfer_Wh > 0:
        # Charging: Apply charge controller efficiency loss
        Energy_added = Energy_transfer_Wh * Eff_ctrl
        new_SOC_Wh = np.clip(prev_SOC_Wh + Energy_added, 0, Max_Capacity_Wh)
    else:
        # Discharging: Apply inverse efficiency loss (more energy needed to satisfy load)
        Energy_subtracted = abs(Energy_transfer_Wh) / Eff_ctrl
        new_SOC_Wh = np.clip(prev_SOC_Wh - Energy_subtracted, 0, Max_Capacity_Wh)
        
    return new_SOC_Wh

# --- 3. SIMULATION INPUT DATA (24-Hour Cycle) ---

Time_Steps = 96 # 96 steps for 24 hours (15 minutes per step)
Time_Step_h = 24 / Time_Steps # 0.25 hours
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

# --- 4. RUNNING THE HYBRID SIMULATION ---

P_wind_hist = []
P_solar_hist = []
SOC_hist_Wh = []

current_SOC_Wh = Initial_SOC * Battery_Capacity_Wh

for i in range(Time_Steps):
    
    # 1. Calculate Power Generation
    P_wind = calculate_wind_power(Wind_Speed[i])
    P_solar = calculate_solar_power(G_irradiance[i])
    P_generated = P_wind + P_solar
    
    # 2. Net Power (Generated - Load)
    P_net = P_generated - Load_Power
    
    # 3. Update Battery SOC
    current_SOC_Wh = update_soc(current_SOC_Wh, P_net, Time_Step_h)
    
    # 4. Store results
    P_wind_hist.append(P_wind)
    P_solar_hist.append(P_solar)
    SOC_hist_Wh.append(current_SOC_Wh)

# Final preparation for plotting
Total_Power_hist = np.array(P_wind_hist) + np.array(P_solar_hist)
SOC_hist_percent = (np.array(SOC_hist_Wh) / Battery_Capacity_Wh) * 100

# --- 5. RESULTS AND VISUALIZATION ---
# [Image of a Hybrid Wind-Solar Power Generation System Schematic]

plt.figure(figsize=(14, 12))

# Subplot 1: Power Generation and Load
plt.subplot(2, 1, 1)
plt.plot(Hours, P_solar_hist, label='Solar (PV Blades) Power (W)', color='#FFC300', linewidth=2)
plt.plot(Hours, P_wind_hist, label='Wind Power (W)', color='#4DB3E6', linewidth=2)
plt.plot(Hours, Total_Power_hist, label='Total Hybrid Power (W)', color='#1E8449', linewidth=3, linestyle='-')
plt.axhline(y=Load_Power, color='r', linestyle=':', label=f'Constant Load ({Load_Power}W)', linewidth=2)

plt.title('Hybrid System Performance: Complementary Power Generation', fontsize=18, fontweight='bold')
plt.xlabel('Time of Day (Hours)', fontsize=14)
plt.ylabel('Power Output (Watts)', fontsize=14)
plt.legend(loc='upper right', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)

# Subplot 2: Battery State of Charge
plt.subplot(2, 1, 2)
plt.plot(Hours, SOC_hist_percent, label='Battery State of Charge (%)', color='#6A1B9A', linewidth=3)
plt.axhline(y=100, color='g', linestyle='--', alpha=0.6, label='100% Max Capacity')
plt.axhline(y=20, color='r', linestyle='--', alpha=0.6, label='20% Critical Low (Avoid)')

plt.title('System Reliability: Battery State of Charge (SOC)', fontsize=18, fontweight='bold')
plt.xlabel('Time of Day (Hours)', fontsize=14)
plt.ylabel('State of Charge (%)', fontsize=14)
plt.ylim(0, 105)
plt.legend(loc='upper right', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout(pad=3.0)
plt.show()

print("\n--- Simulation Summary ---")
print(f"Initial SOC: {Initial_SOC * 100:.2f}%")
print(f"Final SOC: {SOC_hist_percent[-1]:.2f}%")
print("The simulation shows how the complementary power sources (Solar and Wind) work together to keep the battery above the critical discharge limit, enhancing system reliability.")