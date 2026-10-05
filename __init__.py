# -*- coding: utf-8 -*-
"""
CRSTools - A QGIS plugin: Check, define and convert CRS v2.
Copyright (C) 2018 by Hieu Van. Licensed under GNU GPL v2 or later.
Modified by PLT
This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load CheckDefConv class from file crs_tools.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    from .crs_tools import CheckDefConv
    return CheckDefConv(iface)
