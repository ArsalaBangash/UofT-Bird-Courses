"""
This type stub file was generated by pyright.
"""

from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from typing import Any, Optional

class WebDriver(RemoteWebDriver):
    """
    Controls the WebKitGTKDriver and allows you to drive the browser.
    """
    def __init__(self, executable_path=..., port=..., options: Optional[Any] = ..., desired_capabilities=..., service_log_path: Optional[Any] = ..., keep_alive: bool = ...):
        """
        Creates a new instance of the WebKitGTK driver.

        Starts the service and then creates new instance of WebKitGTK Driver.

        :Args:
         - executable_path : path to the executable. If the default is used it assumes the executable is in the $PATH.
         - port : port you would like the service to run, if left as 0, a free port will be found.
         - options : an instance of WebKitGTKOptions
         - desired_capabilities : Dictionary object with desired capabilities
         - service_log_path : Path to write service stdout and stderr output.
         - keep_alive : Whether to configure RemoteConnection to use HTTP keep-alive.
        """
        self.service = ...
    
    def quit(self):
        """
        Closes the browser and shuts down the WebKitGTKDriver executable
        that is started when starting the WebKitGTKDriver
        """
        ...
    


