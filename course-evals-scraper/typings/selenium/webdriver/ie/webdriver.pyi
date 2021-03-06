"""
This type stub file was generated by pyright.
"""

from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from typing import Any, Optional

DEFAULT_TIMEOUT = 30
DEFAULT_PORT = 0
DEFAULT_HOST = None
DEFAULT_LOG_LEVEL = None
DEFAULT_SERVICE_LOG_PATH = None
class WebDriver(RemoteWebDriver):
    """ Controls the IEServerDriver and allows you to drive Internet Explorer """
    def __init__(self, executable_path=..., capabilities: Optional[Any] = ..., port=..., timeout=..., host: Optional[Any] = ..., log_level: Optional[Any] = ..., service_log_path: Optional[Any] = ..., options: Optional[Any] = ..., ie_options: Optional[Any] = ..., desired_capabilities: Optional[Any] = ..., log_file: Optional[Any] = ..., keep_alive: bool = ...):
        """
        Creates a new instance of the chrome driver.

        Starts the service and then creates new instance of chrome driver.

        :Args:
         - executable_path - path to the executable. If the default is used it assumes the executable is in the $PATH
         - capabilities: capabilities Dictionary object
         - port - port you would like the service to run, if left as 0, a free port will be found.
         - timeout - no longer used, kept for backward compatibility
         - host - IP address for the service
         - log_level - log level you would like the service to run.
         - service_log_path - target of logging of service, may be "stdout", "stderr" or file path.
         - options - IE Options instance, providing additional IE options
         - ie_options - Deprecated argument for options
         - desired_capabilities - alias of capabilities; this will make the signature consistent with RemoteWebDriver.
         - log_file - Deprecated argument for service_log_path
         - keep_alive - Whether to configure RemoteConnection to use HTTP keep-alive.
        """
        self.port = ...
        self.host = ...
        self.iedriver = ...
    
    def quit(self):
        ...
    
    def create_options(self):
        ...
    


