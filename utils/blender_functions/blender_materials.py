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

# Blender imports
import bpy

# Blender Messh imports
from messhes.utils import color_helpers


def materials_exists():
    """Returns True if scene has at least one material."""
    return bool(bpy.data.materials)


def is_viewport_colored():
    """Returns True if Blender's materials viewport color is not the default
    color.
    """
    materials = bpy.data.materials

    if not materials_exists():
        return False
    
    for material in materials:
        color = tuple(material.diffuse_color)
        if color_helpers.is_default_color(color):
            return False
    
    return True
