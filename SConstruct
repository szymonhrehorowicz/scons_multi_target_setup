import os
import sys
from site_scons.scons_hints import *


def main():
    target_dir_name = GetOption("target")
    target_dir_node = Dir("#/targets").Dir(target_dir_name)

    if not os.path.isdir(target_dir_node.abspath):
        print("Unable to find target [{}]".format(target_dir_node.name))
        sys.exit(-1)

    if not has_subsidary_scons(target_dir_node):
        print(
            "Target directory [{}] is invalid! Expecting SConscript inside!".format(
                target_dir_node.abspath
            )
        )
        sys.exit(-1)

    Export("target_dir_node")

    SConscript(target_dir_node.File("SConscript"))


def has_subsidary_scons(dirnode):
    """
    Check if a directory node has a subsidiary SConscript file exactly named "SConscript"
    :param dirnode: A directory node (Dir)
    :return: Boolean indicating that the provided directory node contains an SConscript file (bool)
    """
    filenames = os.listdir(dirnode.abspath)
    return len(list(filter(lambda filename: filename == "SConscript", filenames))) > 0


main()
