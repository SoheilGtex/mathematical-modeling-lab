# Computation — Session 10

The implementation at [`src/modeling_lab/hesitant_final.py`](https://github.com/SoheilGtex/mathematical-modeling-lab/blob/main/src/modeling_lab/hesitant_final.py) uses exact rational fractions for grades and membership ramps.

Run the example after installing the repository package:

```bash
python examples/session_10/01_hesitant_membership.py
python -m pytest -q tests/test_session_10_11.py
```

The module validates nonempty membership-grade sets, the \([0,1]\) range and ramp boundaries. It deduplicates identical membership grades and verifies the crisp set \(\{b,c\}\) from the lecture.

**Limitations:** finite HFS values are not probability weights, and the alternative definitions of “tall” are not empirically estimated from the five measurements.
