""" A simple plugin loader."""
import importlib


class PluginInterface:
    """A plugin has a single function called initialize"""
    @staticmethod
    def initialize() -> None:
        """Initialize the plugin"""


def import_module(name: str) -> PluginInterface:
    return importlib.import_module(name)  # type: ignore
    # importlib return module tyep which is different from PluginInterface


def load_plugins(plugins: list[str]):
    """Load the plugin defined in the plugins list."""
    for plugin_name in plugins:
        plugin = import_module(plugin_name)
        plugin.initialize() # importlib中引入的module后调用initialize方法， 把类注册到factory中