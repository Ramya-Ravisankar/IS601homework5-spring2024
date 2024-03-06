'''app_controller.py: Controller module responsible for managing the flow of the application.'''
import pkgutil
import importlib
from typing import Type
from app.commands import CommandHandler, Command
from app.plugins.menu import MenuCommand

class App:
    '''Main application class.'''

    def __init__(self): # Constructor
        self.command_handler = CommandHandler()

    def load_plugins(self):
        '''Dynamically load plugins from the app.plugins directory'''
        plugins_package = 'app.plugins'
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):
            if is_pkg:  # Ensure it's a package
                plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    try:
                        if issubclass(item, (Command)):  # Assuming a BaseCommand class exists
                            self.command_handler.register_command(plugin_name, item())
                    except TypeError:
                        continue  # If item is not a class or unrelated class, just ignore
        # Register MenuCommand
        self.command_handler.register_command("menu", MenuCommand(self.command_handler))

    def start(self):
        '''Register commands from plugin module'''
        self.load_plugins()
        print("Welcome to my calculator applicaiton.")
        print("\tType 'menu' to see available commands. Type 'exit' to quit application.")
        while True:  #REPL Read, Evaluate, Print, Loop
            self.command_handler.execute_command(input(">>> ").strip())