"""
This type stub file was generated by pyright.
"""

from .compat import MutableMapping
from typing import Any, Optional

"""
This type stub file was generated by pyright.
"""
class CaseInsensitiveDict(MutableMapping):
    """A case-insensitive ``dict``-like object.

    Implements all methods and operations of
    ``MutableMapping`` as well as dict's ``copy``. Also
    provides ``lower_items``.

    All keys are expected to be strings. The structure remembers the
    case of the last key to be set, and ``iter(instance)``,
    ``keys()``, ``items()``, ``iterkeys()``, and ``iteritems()``
    will contain case-sensitive keys. However, querying and contains
    testing is case insensitive::

        cid = CaseInsensitiveDict()
        cid['Accept'] = 'application/json'
        cid['aCCEPT'] == 'application/json'  # True
        list(cid) == ['Accept']  # True

    For example, ``headers['content-encoding']`` will return the
    value of a ``'Content-Encoding'`` response header, regardless
    of how the header name was originally stored.

    If the constructor, ``.update``, or equality comparison
    operations are given keys that have equal ``.lower()``s, the
    behavior is undefined.
    """
    def __init__(self, data: Optional[Any] = ..., **kwargs):
        ...
    
    def __setitem__(self, key, value):
        ...
    
    def __getitem__(self, key):
        ...
    
    def __delitem__(self, key):
        ...
    
    def __iter__(self):
        ...
    
    def __len__(self):
        ...
    
    def lower_items(self):
        """Like iteritems(), but with all lowercase keys."""
        ...
    
    def __eq__(self, other):
        ...
    
    def copy(self):
        ...
    
    def __repr__(self):
        ...
    


class LookupDict(dict):
    """Dictionary lookup object."""
    def __init__(self, name: Optional[Any] = ...):
        self.name = ...
    
    def __repr__(self):
        ...
    
    def __getitem__(self, key):
        ...
    
    def get(self, key, default: Optional[Any] = ...):
        ...
    


