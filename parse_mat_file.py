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

