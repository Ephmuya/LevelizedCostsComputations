def calculate_lcoa(
        capex: float, opex_percent: float, lifetime: int, regen_storage_capex: float,
        storage_opex_percent: float, electricity_demand: float
) -> float:
    """
    LCOA = (CAPEX + Regeneration & Storage CAPEX) / (Lifetime * (1 - OPEX) + Electricity Demand)

    """
    total_capex = capex + regen_storage_capex
    total_opex = opex_percent + storage_opex_percent
    return total_capex / (lifetime * (1 - total_opex) + electricity_demand)


if __name__ == "__main__":
    capex = 802.6
    opex_percent = 1.50 / 100
    lifetime = 25
    regen_storage_capex = 0.95
    storage_opex_percent = 1 / 100
    electricity_demand = 0.9

    lcoa = calculate_lcoa(capex, opex_percent, lifetime, regen_storage_capex,
                          storage_opex_percent, electricity_demand)

    print(f"LCOA: ${lcoa:.2f}/t NH3/year")
