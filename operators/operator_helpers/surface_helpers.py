# -*- coding: utf-8 -*-

"""
------------------------------------------------------------
> MESSHES

- AUTHOR:     Doramas García Jorge
- EMAIL:      doramas.dev@pm.me
- GITHUB:     https://github.com/doramasgarciajorge
- REPOSITORY: https://github.com/doramasgarciajorge/messhes
------------------------------------------------------------
"""

# Blender Messh imports
from messhes.utils.blender_functions import blender_materials


def get_toggle_viewport_icon():
    """Returns a different icon name if materials viewport color is colored 
    or not.
    """
    return "MESH_CIRCLE" if blender_materials.is_viewport_colored() \
        else "MATERIAL"


def get_toggle_viewport_text():
    """Returns a different button text if materials viewport color is colored 
    or not.
    """
    return "Discolor viewport" if blender_materials.is_viewport_colored() \
        else "Color viewport"
