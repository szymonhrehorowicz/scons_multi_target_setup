import os

from options import options_init
from scons_hints import *

options_init()

environment_variables = {
    "PYTHONPATH": [
        Dir("#/site_scons"),
    ],
}

for variable, dir_nodes in environment_variables.items():
    if variable not in os.environ:
        os.environ[variable] = ""

    dir_paths = [Dir(dir_node).abspath for dir_node in dir_nodes]
    os.environ[variable] = os.pathsep.join(
        dir_paths + os.environ[variable].split(os.pathsep)
    )
