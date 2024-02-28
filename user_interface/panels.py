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

# Blender modules
from bpy.types import Panel


class MESSHES_PT_main_panel(Panel):
    bl_idname = "MESSHES_PT_main_panel"
    bl_category = "Messhes"
    bl_label = "Messhes tools"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_context = "objectmode"

    def draw(self, context):
        pass
