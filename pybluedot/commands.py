""" commands.py contains the data structures that cli.py uses to construct the arguments/subcommand structure. 
"""

# global arguments and flags to the command, like '--verbose' or '--debug'
cmd_arg = [
    {
        name: "verbose",
        action: "store_const"
    },
    {
        name: "debug",
        action: "store_const"
    }
]

# subcommands used by the program, like 'bdot init' or 'bdot search'.
# Subcommands are tied to functions, so you must specify a function to use with each subcommand.
sub_cmd = [
    {
        name: "init",
        help: "create a pybluedot configuration file",
        options: [
                {
                    name: "--force",
                    action: "store_const"
                },
                {
                    name: "--display",
                    action: "store_const"
                }
        ],
        function: "init"
    },
    {
        name: "sounds",
        help: "just useless boilerplate atm!",
        options: [],
        function: "sounds"
    }
]

