import os

from SCons.Script import *
from scons_hints import *

ENVIRONMENTS_DIR = Dir("#/site_scons/environments")


def get_environment(target_filename) -> SConsEnvironment:
    target_filename += ".py"
    for filename in os.listdir(ENVIRONMENTS_DIR.abspath):
        if target_filename == filename:
            env = SConscript(ENVIRONMENTS_DIR.File(filename))
            break
    else:
        raise KeyError(
            f"Unable to find environment file: [{ENVIRONMENTS_DIR.File(target_filename)}]",
        )
    return env
