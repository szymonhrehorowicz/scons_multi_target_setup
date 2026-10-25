from SCons.Script import AddOption
from scons_hints import *


def options_init():
    AddOption(
        "--test-option",
        action="store_true",
        default=False,
    )
    AddOption(
        "--target",
        metavar="<target directory name>",
        default="sanity",
        help="Specify a target to build",
    )
    AddOption(
        "--verbose",
        action="store_true",
        default=False,
    )
