class ArgumentChecker:
    def __init__(self, args: list[str]):
        self.args = args
        self.commands = {}
        self.aliases = {}
        self.flags = {}

    def checkUsage(self):
        if len(self.args) == 1:
            print(self.getUsage())
            exit(-1)

    def getUsage(self):
        return """main.py <command>
        -h help     Displays the help command
        -c compile <TARGET_FILE> [OUTPUTFILE]   Compiles a target file
        """

    def execute(self):
        execute_path = self.args.pop(0)
        arg_command = self.args.pop(0).strip("-")
        command = self.getCommand(arg_command)

        if command == None: exit(-1) # command not registered
        executor, required_args, optional_args = command

        if len(self.args) < len(required_args): exit(-1) # too few arguments passed in
        elif len(self.args) - len(required_args) > len(optional_args): exit(-1) # too many arguments passed in
        executor(*self.args)

    def getCommand(self, commandName: str):
        return self.commands.get(commandName if commandName in self.commands else self.aliases.get(commandName))

    def addCommand(self, commandName: str, alias: str, executor: callable, required_args: list[str], optional_args: list[str]):
        self.commands[commandName] = (executor, required_args, optional_args)
        self.aliases[alias] = commandName