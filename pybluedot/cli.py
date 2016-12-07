import argparse
from pybluedot.commands import cmd_arg
from pybluedot.commands import sub_cmd

#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.


def cmd_to_args(cmd_arg):
    """creates argparse arguments from commands.cmd dict.
    return argparse object.
    """
    all_args = argparse.ArgumentParser()
    for arg in cmd_arg:
        for i in sorted(arg.keys()):
            # TODO(gamefiend)
            pass
    return all_args


def cmd_to_subs(sub_cmd):
    """creates subcommand arguments from commands.subcmd dict.
        returns argparse object.
    """
    all_subs = argparse.ArgumentParser()
    for sub in sub_cmd:
        for i in sorted(sub):
            # TODO(gamefiend)
            pass
    return all_subs


if __name__ == "__main__":
    bdot_args = cmd_to_args(cmd_arg)
    bdot_subcmds = cmd_to_subs(sub_cmd)
    bdot_args.parse()
    bdot_subcmds.parse()
