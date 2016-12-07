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

# global arguments and flags to the command, like '--verbose' or '--debug'
cmd_arg = [{
    'name': 'verbose',
    'action': 'store_const'
}, {
    'name': 'debug',
    'action': 'store_const'
}]

# subcommands used by the program, like 'bdot init'
sub_cmd = [{
    'name': 'init',
    'help': 'create a pybluedot configuration file',
    'options': [{
        'name': '--force',
        'action': 'store_const'
    }, {
        'name': '--display',
        'action': 'store_const'
    }],
    'function': 'init'
}, {
    'name': 'sounds',
    'help': 'just useless boilerplate atm!',
    'options': [],
    'function': 'sounds'
}]
