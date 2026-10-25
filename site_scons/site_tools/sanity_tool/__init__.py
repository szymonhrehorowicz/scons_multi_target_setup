"""
Sanity check
"""

import os

from SCons.Script import *
from scons_hints import *

SELF_DIR_NODE = Dir(os.path.dirname(__file__))

"""
SCons tools functions
"""


def generate(env: SConsEnvironment) -> None:
    env.AddMethod(sanity_method, "SanityTest")


def exists() -> bool:
    return True


"""
Environment functions
"""


def sanity_method(self, file_node, verbose=False):
    """Generate a txt with file_node name"""
    file_node = File(file_node)

    if verbose:
        print(f"Sanity test of: {file_node}")
