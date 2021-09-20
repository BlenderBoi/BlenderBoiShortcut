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
    if wm.keyconfigs.addon:
        km = wm.keyconfigs.addon.keymaps.new(name='Shortcut Test', space_type='EMPTY')
        kmi = km.keymap_items.new('view3d.view_selected', 'BUTTON4MOUSE', 'PRESS')
        addon_keymaps.append((km, kmi))
        
        
        


def unregister():

    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        for km, kmi in addon_keymaps:
            km.keymap_items.remove(kmi)
    addon_keymaps.clear()

if __name__ == "__main__":
    register()

