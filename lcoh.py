def calculate_lcoh(
        capex: float, om_percent: float, water_purification_costs: float,
        water_costs: float, stack_lifetime: int,
        electrolyzer_efficiency: float, full_load_hours: int
) -> float:
    """
    Calculate the Levelized Cost of Hydrogen (LCOH) using the formula:
    LCOH = (CAPEX / (stack_lifetime * full_load_hours) + OM_percent + water_costs + water_purification_costs) / electrolyzer_efficiency
    """
    return (capex / (
                stack_lifetime * full_load_hours) + om_percent + water_costs + water_purification_costs) / electrolyzer_efficiency


if __name__ == "__main__":
    # 2020
    electrolyzer_efficiency_2020 = 60 / 100
    stack_lifetime_2020 = 65000
    capex_2020 = 1100
    om_percent_2020 = 2 / 100
    water_purification_costs_2020 = 0.4
    water_costs_2020 = 0.97
    full_load_hours_2020 = 7884

    lcoh_2020 = calculate_lcoh(
        capex_2020, om_percent_2020,
        water_purification_costs_2020, water_costs_2020,
        stack_lifetime_2020, electrolyzer_efficiency_2020,
        full_load_hours_2020
    )

    print(f"LCOH for 2020: ${lcoh_2020:.2f}/kgH2")

    # 2030
    electrolyzer_efficiency_2030 = 68 / 100
    stack_lifetime_2030 = 90000
    capex_2030 = 650
    om_percent_2030 = 2 / 100

    lcoh_2030 = calculate_lcoh(
        capex_2030, om_percent_2030,
        water_purification_costs_2020,
        water_costs_2020,
        stack_lifetime_2030,
        electrolyzer_efficiency_2030,
        full_load_hours_2020
    )

    print(f"LCOH for 2030: ${lcoh_2030:.2f}/kgH2")
