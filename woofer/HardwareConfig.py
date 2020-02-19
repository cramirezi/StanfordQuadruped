"""
Per-robot configuration file that is particular to each individual robot, not just the type of robot.
"""

ODRIVE_SERIAL_NUMBERS = ["35619029856331",
                         "35799416713291",
                         "59752448340023",
                         "35726434842440",
                         "35799416778827",
                         "35795121942603"]


def map_actuators_to_axes(odrives):
    axes = np.zeros((4, 3))
    axes[0][0] = odrives[1].axis1
    axes[0][1] = odrives[0].axis0
    axes[0][2] = odrives[0].axis1

    axes[1][0] = odrives[1].axis0
    axes[1][1] = odrives[2].axis1
    axes[1][2] = odrives[2].axis0

    axes[2][0] = odrives[4].axis1
    axes[2][1] = odrives[5].axis0
    axes[2][2] = odrives[5].axis1

    axes[3][0] = odrives[4].axis0
    axes[3][1] = odrives[3].axis1
    axes[3][2] = odrives[3].axis0
    return axes
