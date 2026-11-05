"""Run: python examples/session_10/01_hesitant_membership.py (after pip install -e .)."""
from modeling_lab.hesitant_final import HEIGHTS, CLASS_HFS, crisp_threshold, tall_ramp

if __name__ == '__main__':
    print('Source finite HFS:', CLASS_HFS)
    print('Above 180 cm:', sorted(crisp_threshold(HEIGHTS, 180)))
    for student, height in HEIGHTS.items():
        print(student, 'height=', height, 'tall-ramp=', float(tall_ramp(height)))
