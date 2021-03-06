"""
This type stub file was generated by pyright.
"""

from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver

class WebDriver(RemoteWebDriver):
    """
    Simple RemoteWebDriver wrapper to start connect to Selendroid's WebView app

    For more info on getting started with Selendroid
    http://selendroid.io/mobileWeb.html
    """
    def __init__(self, host=..., port=..., desired_capabilities=...):
        """
        Creates a new instance of Selendroid using the WebView app

        :Args:
         - host - location of where selendroid is running
         - port - port that selendroid is running on
         - desired_capabilities: Dictionary object with capabilities
        """
        ...
    


