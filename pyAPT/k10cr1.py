"""
K10CR1 - controller subclass for the Thorlabs K10CR1 rotational stage
"""

from .controller import Controller

class K10CR1(Controller):
    """
    K10CR1 - controller subclass for the Thorlabs K10CR1 stage
    """

    def __init__(self, serial_number=None, label=None, scale_correction=1.0):
        """Constructor

        Args:
            serial_number (str): S/N of the device
            label (str): optional name of the device
            scale_correction (float): correction factor for position scale
        """

        super(K10CR1, self).__init__(serial_number, label)
     
        self.max_velocity = 10
        self.max_acceleration = 10
     
     
        # From Thorlabs APT specification rev.14
        enccnt = int(409600.0/3.0 * scale_correction)
        T = 2048/6e6
        self.position_scale = enccnt
        self.velocity_scale = enccnt * T * 65536
        self.acceleration_scale = enccnt * T * T * 65536
     
        self.linear_range = (0,360)

