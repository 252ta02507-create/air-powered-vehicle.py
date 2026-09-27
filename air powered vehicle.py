# Air Powered Vehicle

pressure = float(input("Enter air pressure (bar): "))
tank_volume = float(input("Enter air tank volume (litres): "))
efficiency = float(input("Enter system efficiency (%): "))
vehicle_speed = float(input("Enter vehicle speed (km/h): "))

# Approximate energy available from compressed air
# 1 bar-litre ≈ 100 Joules (simplified model)
air_energy = pressure * tank_volume * 100

# Account for system efficiency
usable_energy = air_energy * (efficiency / 100)

# Simplified vehicle energy consumption
energy_per_km = 5000  # Joules per km

# Calculate approximate range
range_km = usable_energy / energy_per_km

# Calculate travel time
if vehicle_speed > 0:
    travel_time = range_km / vehicle_speed
else:
    travel_time = 0

print("\n--- Air Powered Vehicle ---")
print(f"Air pressure       : {pressure:.2f} bar")
print(f"Tank volume        : {tank_volume:.2f} litres")
print(f"Usable energy      : {usable_energy:.2f} J")
print(f"Estimated range    : {range_km:.2f} km")
print(f"Estimated time     : {travel_time:.2f} hours")
