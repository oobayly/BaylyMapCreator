# -*- coding: utf-8 -*-
"""
/***************************************************************************
 BaylyMapCreator
                                 A QGIS plugin
 Map Creator for Jack Bayly
                             -------------------
        begin                : 2016-12-17
        copyright            : (C) 2016 by John Bayly
        email                : john@bayly.eu
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
    """Load BaylyMapCreator class from file BaylyMapCreator.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .bayly_map_creator import BaylyMapCreator
    return BaylyMapCreator(iface)
