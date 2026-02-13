import numpy as np
import matplotlib.pyplot as plt

# --- 1. SYSTEM PARAMETERS (Prototype Scale) ---
# Based on the project's goal to build a small-scale prototype [cite: 8]
Rotor_Radius = 0.5  # meters (e.g., for a small prototype)
Rotor_Area = np.pi * (Rotor_Radius**2)
PV_Area = 0.45      # m² (Approximate PV panel area on blades)
Battery_Capacity_Ah = 100 # Amp-hours (e.g., a common deep cycle battery)
Battery_Voltage = 12 # Volts
Battery_Capacity_Wh = Battery_Capacity_Ah * Battery_Voltage # 1200 Wh (Watt-hours)
Load_Power = 35 # Watts (A constant load, like a few LED lights)

# Efficiencies
Wind_Eff = 0.40   # Power Coefficient Cp 
Solar_Eff = 0.20  # PV Efficiency 
Controller_Eff = 0.90 # Hybrid Charge Controller efficiency

# --- 2. PHYSICS MODELS ---

def calculate_wind_power(V_wind, Area, Eff=Wind_Eff):
    """Calculates wind power based on the Kinetic Energy formula."""
    rho = 1.225 # Air density in kg/m³
    P_wind = 0.5 * rho * Area * (V_wind**3) * Eff
    return P_wind

def calculate_solar_power(G_irradiance, Area, Eff=Solar_Eff):
    """Calculates solar power based on Irradiance and Area."""
    P_solar = G_irradiance * Area * Eff
    return P_solar

def update_soc(prev_SOC_Wh, P_net_W, time_step_h, Max_Capacity_Wh):
    """Updates the Battery State of Charge (Wh) over a time step."""
    
    # Simple limit check for charging and discharging
    if P_net_W > 0:
        # Charging: Add energy, limited by max capacity
        Energy_added = P_net_W * time_step_h * Controller_Eff
        new_SOC_Wh = np.clip(prev_SOC_Wh + Energy_added, 0, Max_Capacity_Wh)
    else:
        # Discharging: Subtract energy, limited by 0 Wh
        Energy_subtracted = abs(P_net_W * time_step_h / Controller_Eff) # Add controller loss on discharge
        new_SOC_Wh = np.clip(prev_SOC_Wh - Energy_subtracted, 0, Max_Capacity_Wh)
        
    return new_SOC_Wh

# --- 3. SIMULATION SETUP (24-Hour Cycle) ---

Time_Steps = 96 # 96 steps for 24 hours (4 steps per hour)
Time_Step_h = 24 / Time_Steps # 0.25 hours (15 minutes)
Hours = np.linspace(0, 24, Time_Steps)

# --- A. Input Data Simulation (Intermittency and Complementarity) ---

# Solar Irradiance (G) - Peaks at Noon (Hour 12), zero at night
G_max = 1000 # W/m²
G_irradiance = G_max * np.maximum(0, np.sin(np.pi * (Hours - 6) / 12))
# Add some cloudy day noise
G_irradiance *= (1 + 0.1 * np.random.randn(Time_Steps))
G_irradiance = np.clip(G_irradiance, 0, G_max) # Ensure it doesn't go below 0 or above G_max

# Wind Speed (V) - Fluctuating and potentially higher at night/seasonal 
Wind_Base = 6 # m/s (Average wind speed)
Wind_Speed = Wind_Base + 3 * np.sin(2 * np.pi * Hours / 24) # Diurnal cycle (stronger at night)
Wind_Speed += 1.5 * np.random.randn(Time_Steps) # Random turbulence
Wind_Speed = np.clip(Wind_Speed, 0, 15) # Wind limits

# --- 4. RUNNING THE HYBRID SIMULATION ---

# Initialize data arrays and State of Charge (SOC)
P_wind_hist = []
P_solar_hist = []
P_net_hist = []
SOC_hist_Wh = []

# Initial SOC at 50%
current_SOC_Wh = 0.5 * Battery_Capacity_Wh

for i in range(Time_Steps):
    # Calculate Power Generation
    P_wind = calculate_wind_power(Wind_Speed[i], Rotor_Area)
    P_solar = calculate_solar_power(G_irradiance[i], PV_Area)
    
    P_generated = P_wind + P_solar
    
    # Net Power (Charging or Discharging)
    P_net = P_generated - Load_Power
    
    # Update Battery SOC
    current_SOC_Wh = update_soc(current_SOC_Wh, P_net, Time_Step_h, Battery_Capacity_Wh)
    
    # Store results
    P_wind_hist.append(P_wind)
    P_solar_hist.append(P_solar)
    P_net_hist.append(P_net)
    SOC_hist_Wh.append(current_SOC_Wh)

# Convert final SOC to percentage for plotting
SOC_hist_percent = (np.array(SOC_hist_Wh) / Battery_Capacity_Wh) * 100

# --- 5. RESULTS AND VISUALIZATION ---

plt.figure(figsize=(14, 10))

# Subplot 1: Power Generation and Load (Complementary View)
plt.subplot(2, 1, 1)
plt.plot(Hours, P_solar_hist, label='Solar Power (W)', color='orange')
plt.plot(Hours, P_wind_hist, label='Wind Power (W)', color='skyblue')
plt.plot(Hours, P_solar_hist + P_wind_hist, label='Total Hybrid Power (W)', color='green', linewidth=2, linestyle='--')
plt.axhline(y=Load_Power, color='r', linestyle=':', label=f'Constant Load ({Load_Power}W)')
plt.title('Hybrid Energy Generation and Load Demand', fontsize=16)
plt.xlabel('Time (Hours)')
plt.ylabel('Power (Watts)')
plt.grid(True)
plt.legend()

# Subplot 2: Battery State of Charge (Reliability View)
plt.subplot(2, 1, 2)
plt.plot(Hours, SOC_hist_percent, label='Battery SOC (%)', color='purple', linewidth=3)
plt.axhline(y=100, color='g', linestyle='--', alpha=0.6, label='100% Max Capacity')
plt.axhline(y=20, color='r', linestyle='--', alpha=0.6, label='20% Minimum SOC')
plt.title('System Reliability: Battery State of Charge (SOC)', fontsize=16)
plt.xlabel('Time (Hours)')
plt.ylabel('State of Charge (%)')
plt.grid(True)
plt.legend()

plt.tight_layout(pad=3.0)
plt.show()

print(f"\nSimulation Complete. Final SOC: {SOC_hist_percent[-1]:.2f}%")
print("Observe how the combined output (green dashed line) is more stable than either single source alone, allowing the battery SOC (purple line) to remain stable.")