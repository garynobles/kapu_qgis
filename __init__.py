# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Kapu
                                 A QGIS plugin
 Access the Kapu blockchain
                             -------------------
        begin                : 2018-02-21
        copyright            : (C) 2018 by Gary Nobles
        email                : garynobles@hotmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load Kapu class from file Kapu.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .kapu import Kapu
    return Kapu(iface)
