# -*- coding: utf-8 -*-

__all__ = [
  'GMOKeysLookup'
]  # This should be a list of all public methods and attributes that can be imported from this
   # module elsewhere. This list should contain the class names of all the model-specific keys
   # keys lookup classes defined here.

# Python 2 standard library imports
import csv
import io
import logging
import os

# Python 2 non-standard library imports

# Oasis utils and other Oasis imports

from oasislmf.keys.lookup import OasisBaseKeysLookup
from oasislmf.utils.log import oasis_log

# Model keys server imports
from utils import *

class GMOKeysLookup(OasisBaseKeysLookup):
    """
    Model-specific keys lookup logic.
    """

    @oasis_log()
    def __init__(self, keys_data_directory=None, supplier=GEMFoundation, model_name=GMO, model_version=None):
        """
        Initialise the static data required for the lookup.
        """
        super(self.__class__, self).__init__(
            keys_data_directory,
            supplier,
            model_name,
            model_version
        )
        pass
    
    
    @oasis_log()
    def process_locations(self, loc_df):
        """
        Process location rows - passed in as a pandas dataframe.
        """
        pass
