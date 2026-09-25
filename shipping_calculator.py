
# shipping_calculator.py
# Starter code for calculating shipping logistics rates

def calculate_shipping_cost(weight_kg, distance_km, rate_per_kg_km=0.05):
    """Calculate base shipping cost."""
    if weight_kg <= 0 or distance_km <= 0:
        raise ValueError("Weight and distance must be positive.")
    return round(weight_kg * distance_km * rate_per_kg_km, 2)

def estimate_delivery_days(distance_km, service="standard"):
    """Estimate delivery time based on distance and service level."""
    speeds = {"standard": 500, "express": 1000, "overnight": 2000}
    if service not in speeds:
        raise ValueError(f"Unknown service: {service}")
    return max(1, round(distance_km / speeds[service]))

if __name__ == "__main__":
    cost = calculate_shipping_cost(10, 1200)
    days = estimate_delivery_days(1200, "express")
    print(f"Shipping cost: ${cost}")
    print(f"Estimated delivery: {days} day(s)")
