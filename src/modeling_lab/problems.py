"""Problem data from the first class's handwritten modeling notes.

The base models preserve the notes' nonnegative *continuous* variables.
Integer restrictions, when requested in examples, are explicit extensions.
"""

from .linear import LinearProgram


def diet_problem() -> LinearProgram:
    """Minimize daily food cost, subject to vitamin A and B requirements.

    Variables: p = cheese, s = milk, t = eggs (units as in the notes).
    Objective is in toman. Source >= constraints are negated to <= form.
    """
    return LinearProgram(
        name="Session 01 — Diet problem",
        variables=("p", "s", "t"),
        objective=(100.0, 50.0, 40.0),
        maximize=False,
        a_ub=((-1.0, -4.0, -2.0), (-1.0, -2.0, -3.0)),
        b_ub=(-12.0, -14.0),
        constraint_names=("vitamin_A_min_12", "vitamin_B_min_14"),
        bounds=((0.0, None), (0.0, None), (0.0, None)),
        objective_unit="toman/day",
    )


def boat_production_problem() -> LinearProgram:
    """Maximize profit from regular and competition boats.

    Variables: x=regular, y=competition. Profit measured in 1000 toman.
    Machine time is converted from 5 hours to 300 minutes.
    """
    return LinearProgram(
        name="Session 01 — Boat production",
        variables=("x", "y"),
        objective=(50.0, 80.0),
        maximize=True,
        a_ub=((50.0, 30.0), (20.0, 15.0), (3.0, 5.0)),
        b_ub=(1000.0, 300.0, 200.0),
        constraint_names=("aluminum_kg", "machine_minutes", "labor_hours"),
        bounds=((0.0, None), (0.0, None)),
        objective_unit="thousand toman",
    )
