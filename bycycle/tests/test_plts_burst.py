"""Tests plotting bursts."""

import numpy as np
import pytest

from bycycle.plts import plot_burst_detect_param, plot_burst_detect_summary
from bycycle.tests.utils import plot_test
from bycycle.tests.settings import TEST_PLOTS_PATH

###################################################################################################
###################################################################################################

@plot_test
@pytest.mark.parametrize("interp", [True, False])
def test_plot_burst_detect_param(sim_args, interp):

    df = sim_args['df']
    sig = sim_args['sig']
    fs = sim_args['fs']

    thresh = np.nanmin(df['amp_consistency'].values) + 0.1

    plot_burst_detect_param(df, sig, fs, 'amp_consistency', thresh, interp=interp, save_fig=True,
                            file_path=TEST_PLOTS_PATH, file_name='test_plot_burst_detect_param')


@plot_test
@pytest.mark.parametrize("plot_only_result", [True, False])
def test_plot_burst_detect_summary(sim_args, plot_only_result):

    osc_kwargs = {'amp_fraction_threshold': 1.1,
                  'amp_consistency_threshold': .5,
                  'period_consistency_threshold': .5,
                  'monotonicity_threshold': .8,
                  'n_cycles_min': 3}

    sim_args['burst_detection_kwargs'] = osc_kwargs

    plot_burst_detect_summary(**sim_args, plot_only_result=plot_only_result,
                              save_fig=True, file_path=TEST_PLOTS_PATH,
                              file_name='test_plot_burst_detect_summary')
