# plugin_manager.py

class PluginManager:
    def __init__(self):
        # Dictionary to store plugins with their name as key
        self.plugins = {}

    def load_plugins(self):
        """
        Dynamically load plugins or hardcode them here.
        """
        # Instantiate and load the plugins here
        self.plugins['addition_plugin'] = AdditionPlugin()
        self.plugins['subtraction_plugin'] = SubtractionPlugin()
        self.plugins['multiplication_plugin'] = MultiplicationPlugin()
        self.plugins['division_plugin'] = DivisionPlugin()

    def list_plugins(self):
        """
        Returns a list of the loaded plugin names.
        """
        return list(self.plugins.keys())


class AdditionPlugin:
    def add(self, x, y):
        """ Add two numbers """
        return x + y


class SubtractionPlugin:
    def subtract(self, x, y):
        """ Subtract two numbers """
        return x - y


class MultiplicationPlugin:
    def multiply(self, x, y):
        """ Multiply two numbers """
        return x * y


class DivisionPlugin:
    def divide(self, x, y):
        """ Divide two numbers and handle division by zero """
        if y == 0:
            raise ZeroDivisionError("Cannot divide by zero!")
        return x / y
class PluginManager:
    def __init__(self):
        self.plugins = {}

    def load_plugins(self):
        # Dynamically load plugins or hardcode them here
        self.plugins['addition_plugin'] = AdditionPlugin()
        self.plugins['subtraction_plugin'] = SubtractionPlugin()
        # Add more plugins as necessary

    def list_plugins(self):
        # Returns a list of loaded plugin names
        return list(self.plugins.keys())

