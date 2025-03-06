class Circle:
  pi = 3.14
  def __init__(self, diameter):
    print("Creating circle with diameter {d}".format(d=diameter))
    # Add assignment for self.radius here:
    self.radius = diameter / 2

def diameter(self):
    return 2 * self.radius

def circumference(self):
    return 2 * self.pi * self.radius

def area(self):
    return self.pi * (self.radius ** 2)

def arc_length(self, theta):
    """ Calculates the arc length given an angle (theta in degrees) """
    return (theta / 360) * self.circumference()

def sector_area(self, theta):
    """ Calculates the area of a sector given an angle (theta in degrees) """
    return (theta / 360) * self.area()

def chord_length(self, theta):
    """ Calculates the chord length given an angle (theta in degrees) """
    theta_radians = math.radians(theta)
    return 2 * self.radius * math.sin(theta_radians / 2)

def segment_area(self, theta):
    """ Calculates the area of a segment given an angle (theta in degrees) """
    theta_radians = math.radians(theta)
    sector = self.sector_area(theta)
    triangle = 0.5 * (self.radius ** 2) * math.sin(theta_radians)
    return sector - triangle

def inscribed_angle(self, theta):
    """ Calculates the inscribed angle given a central angle (theta in degrees) """
    return theta / 2