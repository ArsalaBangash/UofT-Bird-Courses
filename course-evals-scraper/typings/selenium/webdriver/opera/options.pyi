"""
This type stub file was generated by pyright.
"""

from selenium.webdriver.chrome.options import Options as ChromeOptions

class Options(ChromeOptions):
    KEY = ...
    def __init__(self):
        ...
    
    @property
    def capabilities(self):
        ...
    
    def set_capability(self, name, value):
        """Sets a capability."""
        ...
    
    @property
    def android_package_name(self):
        """
        Returns the name of the Opera package
        """
        ...
    
    @android_package_name.setter
    def android_package_name(self, value):
        """
        Allows you to set the package name

        :Args:
         - value: devtools socket name
        """
        ...
    
    @property
    def android_device_socket(self):
        """
        Returns the name of the devtools socket
        """
        ...
    
    @android_device_socket.setter
    def android_device_socket(self, value):
        """
        Allows you to set the devtools socket name

        :Args:
         - value: devtools socket name
        """
        ...
    
    @property
    def android_command_line_file(self):
        """
        Returns the path of the command line file
        """
        ...
    
    @android_command_line_file.setter
    def android_command_line_file(self, value):
        """
        Allows you to set where the command line file lives

        :Args:
         - value: command line file path
        """
        ...
    
    def to_capabilities(self):
        """
            Creates a capabilities with all the options that have been set and

            returns a dictionary with everything
        """
        ...
    


class AndroidOptions(Options):
    def __init__(self):
        self.android_package_name = ...
    


