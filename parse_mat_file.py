"""
NASA PCoE Battery Dataset - Data Pre-processing Script
=======================================================
Parses discharge and impedance MATLAB (.mat) files from the NASA Prognostics
Center of Excellence Battery Dataset into a clean, flattened Pandas DataFrame.

Dataset: https://www.nasa.gov/intelligent-systems-division/discovery-and-systems-health/pcoe/pcoe-data-set-repository/
Batteries: B0005, B0006, B0007, B0018

Output: battery_master_log.parquet
"""

import os
import glob
import numpy as np
import pandas as pd
from scipy.io import loadmat



# Configuration

DATA_DIR    = os.path.join(os.path.dirname(__file__), "data", "raw")
OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "data", "battery_master_log.parquet")
BATTERY_IDS = ["B0005", "B0006", "B0007", "B0018"]


# Helpers for navigating the deeply-nested MATLAB struct arrays

def _unpack(val):
    """Recursively unpack single-element numpy arrays / object arrays."""
    while isinstance(val, np.ndarray) and val.size == 1:
        val = val.flat[0]
    return val


def _get_field(struct, field_name):
    """
    Safely retrieve a named field from a MATLAB struct loaded by scipy.
    Returns None when the field does not exist.
    """
    try:
        return _unpack(struct[field_name])
    except (IndexError, KeyError, ValueError, TypeError):
        return None


def _to_flat_array(val):
    """Convert a MATLAB data vector to a flat 1-D numpy array of floats."""
    val = np.asarray(val)
    return val.flatten().astype(np.float64)

