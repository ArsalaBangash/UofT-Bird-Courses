"""
This type stub file was generated by pyright.
"""

from typing import Any, Optional

class ActionBuilder(object):
    def __init__(self, driver, mouse: Optional[Any] = ..., keyboard: Optional[Any] = ...):
        self.devices = ...
        self.driver = ...
    
    def get_device_with(self, name):
        ...
    
    @property
    def pointer_inputs(self):
        ...
    
    @property
    def key_inputs(self):
        ...
    
    @property
    def key_action(self):
        ...
    
    @property
    def pointer_action(self):
        ...
    
    def add_key_input(self, name):
        ...
    
    def add_pointer_input(self, kind, name):
        ...
    
    def perform(self):
        ...
    
    def clear_actions(self):
        """
            Clears actions that are already stored on the remote end
        """
        ...
    
    def _add_input(self, input):
        ...
    


