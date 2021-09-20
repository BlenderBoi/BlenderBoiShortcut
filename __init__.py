bl_info = {
    'name': 'Blenderboi Shortcuts',
    'version': (0, 1, 0),
    'blender': (2, 80, 0),
    'category': 'Shortcuts'
}

import bpy

addon_keymaps = []

def register():

    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon

    if kc:
        km = kc.keymaps.new(name = "3D View", space_type="VIEW_3D")
        kmi = km.keymap_items.new("view3d.view_selected", type="BUTTON4MOUSE", value="PRESS")
        addon_keymaps.append([km, kmi])


        km = kc.keymaps.new(name = "3D View", space_type="VIEW_3D")
        kmi = km.keymap_items.new("curve.select_linked_pick", type="BUTTON5MOUSE", value="PRESS")
        addon_keymaps.append([km, kmi])

        km = kc.keymaps.new(name = "3D View", space_type="VIEW_3D")
        kmi = km.keymap_items.new("pose.select_linked_pick", type="BUTTON5MOUSE", value="PRESS")
        addon_keymaps.append([km, kmi])

        km = kc.keymaps.new(name = "3D View", space_type="VIEW_3D")
        kmi = km.keymap_items.new("mesh.select_linked_pick", type="BUTTON5MOUSE", value="PRESS")
        addon_keymaps.append([km, kmi])

        km = kc.keymaps.new(name = "3D View", space_type="VIEW_3D")
        kmi = km.keymap_items.new("armature.select_linked_pick", type="BUTTON5MOUSE", value="PRESS")
        addon_keymaps.append([km, kmi])

        km = kc.keymaps.new(name = "3D View", space_type="VIEW_3D")
        kmi = km.keymap_items.new("particle.select_linked_pick", type="BUTTON5MOUSE", value="PRESS")
        addon_keymaps.append([km, kmi])

        km = kc.keymaps.new(name = "Image", space_type="IMAGE_EDITOR")
        kmi = km.keymap_items.new("uv.select_linked_pick", type="BUTTON5MOUSE", value="PRESS")
        addon_keymaps.append([km, kmi])

        # km = kc.keymaps.new(name = "3D View", space_type="VIEW_3D")
        # kmi = km.keymap_items.new("mask.select_linked_pick", type="BUTTON5MOUSE", value="PRESS")
        # addon_keymaps.append([km, kmi])

        km = kc.keymaps.new(name = "Graph Editor", space_type="GRAPH_EDITOR")
        kmi = km.keymap_items.new("graph.select_linked", type="BUTTON5MOUSE", value="PRESS")
        addon_keymaps.append([km, kmi])

        km = kc.keymaps.new(name = "Node Editor", space_type="NODE_EDITOR")
        kmi = km.keymap_items.new("node.select_linked_from", type="BUTTON5MOUSE", value="PRESS")
        addon_keymaps.append([km, kmi])

        km = kc.keymaps.new(name = "Sequencer", space_type="SEQUENCE_EDITOR")
        kmi = km.keymap_items.new("sequencer.select_linked_pick", type="BUTTON5MOUSE", value="PRESS")
        addon_keymaps.append([km, kmi])

        km = kc.keymaps.new(name = "Node Editor", space_type="NODE_EDITOR")
        kmi = km.keymap_items.new("node.view_selected", type="BUTTON4MOUSE", value="PRESS")
        addon_keymaps.append([km, kmi])

        km = kc.keymaps.new(name = "Outliner", space_type="OUTLINER")
        kmi = km.keymap_items.new("outliner.show_active", type="BUTTON4MOUSE", value="PRESS")
        addon_keymaps.append([km, kmi])

        km = kc.keymaps.new(name = "Dopesheet", space_type="DOPESHEET_EDITOR")
        kmi = km.keymap_items.new("action.view_selected", type="BUTTON4MOUSE", value="PRESS")
        addon_keymaps.append([km, kmi])

        km = kc.keymaps.new(name = "Graph Editor", space_type="GRAPH_EDITOR")
        kmi = km.keymap_items.new("graph.view_selected", type="BUTTON4MOUSE", value="PRESS")
        addon_keymaps.append([km, kmi])

        km = kc.keymaps.new(name = "Image", space_type="IMAGE_EDITOR")
        kmi = km.keymap_items.new("image.view_selected", type="BUTTON4MOUSE", value="PRESS")
        addon_keymaps.append([km, kmi])

        km = kc.keymaps.new(name = "File Browser Main", space_type="FILE_BROWSER")
        kmi = km.keymap_items.new("file.view_selected", type="BUTTON4MOUSE", value="PRESS")
        addon_keymaps.append([km, kmi])

        km = kc.keymaps.new(name = "NLA Editor", space_type="NLA_EDITOR")
        kmi = km.keymap_items.new("nla.view_selected", type="BUTTON4MOUSE", value="PRESS")
        addon_keymaps.append([km, kmi])

        km = kc.keymaps.new(name = "Sequencer", space_type="SEQUENCE_EDITOR")
        kmi = km.keymap_items.new("sequencer.view_selected", type="BUTTON4MOUSE", value="PRESS")
        addon_keymaps.append([km, kmi])


        km = kc.keymaps.new(name = "Clip Editor", space_type="CLIP_EDITOR")
        kmi = km.keymap_items.new("clip.view_selected", type="BUTTON5MOUSE", value="PRESS")
        addon_keymaps.append([km, kmi])




def unregister():

    addon_keymaps.clear()


if __name__ == "__main__":
    register()
