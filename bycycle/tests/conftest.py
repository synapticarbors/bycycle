"""Configuration file for pytest for bycycle."""

import os
import shutil
import pytest

from neurodsp.utils.sim import set_random_seed
from neurodsp.sim import sim_oscillation
from bycycle.features import compute_features
from bycycle.tests.settings import BASE_TEST_FILE_PATH, TEST_PLOTS_PATH

###################################################################################################
###################################################################################################

def pytest_configure(config):

    set_random_seed(42)


@pytest.fixture(scope='module')
def sim_args():

    # Simulate oscillating time series
    n_seconds = 10
    fs = 500
    freq = 10
    f_range = (6, 14)

    sig = sim_oscillation(n_seconds, fs, freq)

    df = compute_features(sig, fs, f_range)

    yield {'df': df, 'sig': sig, 'fs': fs}


@pytest.fixture(scope='session', autouse=True)
def check_dir():
    """Once, prior to session, this will clear and re-initialize the test file directories."""

    # If the directories already exist, clear them
    if os.path.exists(BASE_TEST_FILE_PATH):
        shutil.rmtree(BASE_TEST_FILE_PATH)

    # Remake (empty) directories
    os.mkdir(BASE_TEST_FILE_PATH)
    os.mkdir(TEST_PLOTS_PATH)
