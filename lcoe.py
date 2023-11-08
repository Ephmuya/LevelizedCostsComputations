def calculate_lcoe(
        capex: float, om_fixed: float, om_variable: float, discount_rate: float,
        annual_generation: float, project_lifespan: int
) -> float:
    """
    Calculate the Levelized Cost of Energy (LCOE) using the formula:
    LCOE = (CAPEX + ∑(OM_fixed / ((1 + discount_rate) ** t) + OM_variable * annual_generation / ((1 + discount_rate) ** t))) /
           ∑(annual_generation / ((1 + discount_rate) ** t))
    where t ranges from 1 to project_lifespan.
    """
    lcoe_numerator = capex + sum(
        om_fixed / ((1 + discount_rate) ** t) + om_variable * annual_generation / (
                (1 + discount_rate) ** t) for t in range(1, project_lifespan + 1))
    lcoe_denominator = sum(annual_generation / ((1 + discount_rate) ** t) for t in
                           range(1, project_lifespan + 1))
    return lcoe_numerator / lcoe_denominator


def calculate_lcoe_two(
        capex: float, om_fixed: float, om_variable: float, discount_rate: float,
        annual_generation: float, project_lifespan: int
) -> float:
    """
    Calculate the Levelized Cost of Energy (LCOE) using the formula:
    LCOE = [(FCR * CAPEX + OM_fixed) / annual_generation] + OM_variable
    where FCR is the fixed charge rate, calculated as discount_rate / (1 - (1 + discount_rate) ** (-project_lifespan)).
    """
    fcr = discount_rate / (1 - (1 + discount_rate) ** (-project_lifespan))
    return ((fcr * capex + om_fixed) / annual_generation) + om_variable


if __name__ == "__main__":
    capex = 429089887.560338
    om_fixed = capex * 0.03
    om_variable = 0.02
    discount_rate = 0.128
    annual_generation = 1245672
    project_lifespan = 25

    lcoe = calculate_lcoe(
        capex, om_fixed,
        om_variable,
        discount_rate,
        annual_generation,
        project_lifespan
    )
    print(f"LCOE first Formula: ${lcoe:} per MWh")

    lcoe = calculate_lcoe_two(
        capex, om_fixed,
        om_variable,
        discount_rate,
        annual_generation,
        project_lifespan
    )
    print(f"LCOE second Formula: ${lcoe:} per MWh")
