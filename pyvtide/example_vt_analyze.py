# This script runs an vt_analyze example under the example directory
# using a Python that wraps vt_analyze.

from pathlib import Path
import numpy as np
# `vtide_f`` module file must be in the same directory.
import vtide_f


def read_analysis_main_inp(fname):
    """ Read the main analysis input file and return the list of the input
        files.
    """
    input_files = []
    with open(fname, "r") as f:
        for i in range(6):
            input_files.append(f.readline().split()[0])
    return input_files


def main():
    """ Main function """
    # Main input file
    path_analysis_main = "../example/model_data/analysis_main.inp"
    path_input_base = Path(path_analysis_main).parent
    input_files = read_analysis_main_inp(path_analysis_main)
    fname = str(path_input_base / input_files[0])

    # Read a analysis input file
    analysis_info = vtide_f.file_io.vt_analysis_info(fname.ljust(80))
    fname = str(path_input_base / input_files[1])

    # Read constituents from a file
    vtide_f.constituent.vt_read_constituent_db(fname.ljust(80))
    # Store `file_analysis_out`. The variable is used by `vt_analyze`
    vtide_f.file_io.file_analysis_out = input_files[3].ljust(80)

    # Map input variables of `vt_analyze`
    latd = analysis_info[0]
    latm = analysis_info[1]
    mf = analysis_info[6]
    ndef = analysis_info[7]
    itrend = analysis_info[8]
    nloc = analysis_info[9]
    name = analysis_info[10]
    freqc = analysis_info[11]
    ninfer_cnstnts = analysis_info[13]
    ninfer = analysis_info[14]
    infer_main_cons = analysis_info[15]
    infer_names = analysis_info[16]
    infer_freq = analysis_info[17]
    infer_amp = analysis_info[18]
    infer_zeta = analysis_info[19]
    id1 = analysis_info[20]
    im1 = analysis_info[21]
    iy1 = analysis_info[22]
    id2 = analysis_info[23]
    im2 = analysis_info[24]
    iy2 = analysis_info[25]
    ic1 = analysis_info[26]
    ic2 = analysis_info[27]

    # Count the number of the observation data
    fname = str(path_input_base / input_files[2]).ljust(80)
    nobs = vtide_f.file_io.vt_count_data(fname, ndef, nloc,
                                         id1, im1, iy1, ic1,
                                         id2, im2, iy2, ic2)
    # Read in the observation data
    itime, obsdata = vtide_f.file_io.vt_read_data(fname, ndef, nloc,
                                                  id1, im1, iy1, ic1,
                                                  id2, im2, iy2, ic2,
                                                  nobs)
    # Run the tidal harmonic analysis, `vt_analyze`
    analysis = vtide_f.vt_analyze(nobs,
                                  itime,
                                  obsdata,
                                  latd, latm,
                                  mf, ndef, itrend, nloc,
                                  name, freqc,
                                  ninfer_cnstnts, ninfer,
                                  infer_main_cons,
                                  infer_names,
                                  infer_freq,
                                  infer_amp,
                                  infer_zeta)

    # Show a couple of outputs
    print("Show some outputs from vt_analyze")
    # Amplitude
    print("Amplitudes:")
    ampc = analysis[0]
    print(ampc[:mf, 0, :])

    # Amplitudes of inferred components
    print("Amplitudes of inferred constituents:")
    ampci = analysis[2]
    print(ampci[:ninfer_cnstnts, 0, 0, :])


if __name__ == "__main__":
    main()
