"""Source fidelity and independently verifiable optima for Session 04."""
from __future__ import annotations

from pathlib import Path

import pytest

from modeling_lab.linear import solve
from modeling_lab.session04 import (
    MACHINE_UNIT_COSTS, MACHINE_HOURS_PER_UNIT, MACHINE_HOUR_CAPACITIES,
    PRODUCT_MINIMUMS, CRUDE_PRODUCT_FRACTIONS, CRUDE_RECOVERY,
    REFINED_PRODUCT_MINIMUMS, FIXED_OPERATING_COST, machine_allocation_problem,
    crude_oil_problem, fractional_production_solution, product_revenue_cost_ratio,
)
from modeling_lab.verification import verify_solution


def test_machine_note_transcription_and_constraints():
    assert MACHINE_UNIT_COSTS == ((4,4,5,7),(6,7,5,6),(12,10,8,11))
    assert MACHINE_HOURS_PER_UNIT == ((.3,.25,.2,.2),(.2,.3,.2,.25),(.8,.6,.6,.5))
    assert MACHINE_HOUR_CAPACITIES == (1500,1200,1500,2000)
    assert PRODUCT_MINIMUMS == (3000,6000,4000)
    model = machine_allocation_problem()
    assert len(model.variables) == 12
    assert len(model.a_ub) == 7  # 4 caps, 3 minima
    assert not model.maximize
    assert model.objective_unit == 'USD'


def test_machine_optimal_plan_and_dual_lower_bound():
    model=machine_allocation_problem()
    sol=solve(model)
    assert sol.objective_value == pytest.approx(82500)
    x = [[sol.variable_values[f'x{i}_{j}'] for j in range(1,5)] for i in range(1,4)]
    for i in range(3):
        assert sum(x[i]) >= PRODUCT_MINIMUMS[i] - 1e-7
    for j in range(4):
        assert sum(x[i][j]*MACHINE_HOURS_PER_UNIT[i][j] for i in range(3)) <= MACHINE_HOUR_CAPACITIES[j] + 1e-7
    assert verify_solution(model,sol).independent_optimality_verified
    # A feasible LP dual certificate: p_i - q_j*t_ij <= c_ij, q_j>=0.
    p=(4,6,11)
    q=(0,5/3,5,0)
    assert all(p[i]-q[j]*MACHINE_HOURS_PER_UNIT[i][j] <= MACHINE_UNIT_COSTS[i][j]+1e-9 for i in range(3) for j in range(4))
    lower_bound=sum(p[i]*PRODUCT_MINIMUMS[i] for i in range(3))-sum(q[j]*MACHINE_HOUR_CAPACITIES[j] for j in range(4))
    assert lower_bound == pytest.approx(82500)


def test_crude_yields_and_exact_optimum():
    assert CRUDE_PRODUCT_FRACTIONS == ((.4,.32),(.2,.4),(.35,.2))
    assert CRUDE_RECOVERY == (.95,.92)
    assert REFINED_PRODUCT_MINIMUMS == (1_000_000,500_000,300_000)
    model=crude_oil_problem()
    sol=solve(model)
    heavy=1_000_000/(.32*.92)
    assert sol.variable_values['x_light'] == pytest.approx(0, abs=1e-7)
    assert sol.variable_values['x_heavy'] == pytest.approx(heavy)
    assert sol.objective_value == pytest.approx(15*heavy)
    assert verify_solution(model,sol).independent_optimality_verified
    # Every feasible plan costs >= (15/.2944)*(diesel output).
    multiplier=15/(.32*.92)
    assert 20 >= multiplier*(.4*.95)
    assert 15 == pytest.approx(multiplier*(.32*.92))


def test_fractional_ratio_and_hand_proof():
    s=fractional_production_solution()
    assert s.product_a == pytest.approx(50)
    assert s.product_b == pytest.approx(0)
    assert s.variable_cost == pytest.approx(2000)
    assert s.revenue == pytest.approx(4000)
    assert s.total_cost == pytest.approx(2200)
    assert s.revenue_cost_ratio == pytest.approx(20/11)
    assert product_revenue_cost_ratio(50,0) == pytest.approx(20/11)
    assert FIXED_OPERATING_COST > 0
    with pytest.raises(ValueError):
        product_revenue_cost_ratio(61,0)


def test_session04_site_exam_and_examples_exist():
    root = Path(__file__).resolve().parents[1]
    for lang in ('en','fa'):
        for name in ('index','machines','crude','ratio','computation'):
            assert (root / f'site_docs/session-04/{name}.{lang}.md').is_file()
        exam=(root/f'site_docs/exam.{lang}.md').read_text(encoding='utf8')
        for name in ('machines','crude','ratio'):
            assert f'session-04/{name}.md' in exam
        # No numerical solution targets in the exam-only review.
        assert '82500' not in exam and '50951086' not in exam
    for name in ('01_machine_allocation.py','02_crude_oil.py','03_revenue_cost_ratio.py'):
        assert (root/f'examples/session_04/{name}').is_file()
