"""
MFF101 - controller subclass for the Thorlabs MTS50/M-Z8 stage
"""

from .controller import Controller

class MFF101(Controller):
    """
    MFF101 - controller subclass for the Thorlabs MFF101 flipper
    """

    def __init__(self, serial_number=None, label=None):
        """Constructor

        Args:
            serial_number (str): S/N of the device
            label (str): optional name of the device
        """

        super(MFF101, self).__init__(serial_number, label)
	

