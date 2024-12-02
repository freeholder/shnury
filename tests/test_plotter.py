import pytest
from unittest import mock
import matplotlib.pyplot as plt
from app.plotter import plot_finger_load_comparison_horizontal

finger_loads_ycu = {
    'lfi5': 5,
    'lfi4': 3,
    'lfi3': 4,
    'lfi2': 6,
    'lfi1': 2,
    'rfi2': 7,
    'rfi3': 8,
    'rfi4': 1,
    'rfi5': 9,
}

finger_loads_vyzov = {
    'lfi5': 3,
    'lfi4': 4,
    'lfi3': 5,
    'lfi2': 7,
    'lfi1': 3,
    'rfi2': 5,
    'rfi3': 6,
    'rfi4': 2,
    'rfi5': 10,
}

def test_plot_finger_load_comparison_horizontal():
    with mock.patch.object(plt, 'show') as mock_show:
        plot_finger_load_comparison_horizontal(finger_loads_ycu, finger_loads_vyzov)
        
        mock_show.assert_called_once()
