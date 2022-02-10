""" Regression test scripts for VTide
"""
from pathlib import Path
import os
import shutil
import subprocess
import pytest
import pandas as pd
from pytest_regressions import dataframe_regression


def read_inputs_from_main_input(fpath):
    """ Read input files from the vt_analyze main input. """
    input_files = []
    with open(fpath, "r") as f:
        for _ in range(3):
            input_files.append(f.readline().split()[0])
    return input_files


def copy_vt_analyze_input():
    """ Copy the input files to the current test directory. """
    path_current = Path(__file__).parent
    path_base = path_current.parent
    path_input = path_base / "example/model_data"
    input_files = ["analysis_main.inp", ]
    path_main_input = path_input / input_files[0]
    shutil.copy(path_main_input, path_current)
    input_files.extend(read_inputs_from_main_input(path_main_input))
    for fname in input_files:
        src = path_input / fname
        shutil.copy(src, path_current)
    return input_files


def delete_vt_analyze_input(files):
    """ Remove input files once a test run is done. """
    path_current = Path(__file__).parent
    for f in files:
        os.remove(path_current / f)


@pytest.fixture(scope="module")
def vt_analyze(pytestconfig):
    """ Run the vt_analyze. """
    path_bin = pytestconfig.getoption("path_vt_analyze")
    input_files = copy_vt_analyze_input()
    path_current = Path(__file__).parent
    os.chdir(path_current)
    cmd = [path_bin, "analysis_main.inp"]
    subprocess.run(cmd)
    delete_vt_analyze_input(input_files)


@pytest.fixture()
def vt_analyze_constituent(vt_analyze):
    """ Get a data frame from the constituent file
    """
    path_current = Path(__file__).parent
    os.chdir(path_current)
    df = pd.read_csv("run66b_2010_07_constituent.out", skiprows=11)
    return df


def test_vt_analyze_constituent(vt_analyze_constituent, dataframe_regression):
    """ Test regression from a constituent output file """
    dataframe_regression.check(vt_analyze_constituent)
