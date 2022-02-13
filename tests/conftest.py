""" Test configurations
"""

# Add command line options
def pytest_addoption(parser):
    parser.addoption("--path_vt_analyze", action="store")
    # parser.addoption("--rtol", action="store")
    # parser.addoption("--atol", action="store")
