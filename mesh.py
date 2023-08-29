import bpy
import mathutils
r = 10
black = bpy.data.materials.new("Black")
black.diffuse_color = (0,0,0,0.8)
black.specular_intensity = 0
def addBall(x,y,z):
    bpy.ops.mesh.primitive_ico_sphere_add()
    # our created cube is the active one
    obj = bpy.context.active_object
    obj.active_material = black
    # Remove object from all collections not used in a scene
    bpy.ops.collection.objects_remove_all()
    # add it to our specific collection
    bpy.data.collections['Balls'].objects.link(obj)
    obj.location  = obj.location + mathutils.Vector((x*r,y*r,z*r))

    
    
def addRod(x,y,z ):
    bpy.ops.mesh.primitive_cube_add()
    # our created cube is the active one
   
    obj = bpy.context.active_object
    obj.active_material = black
    # Remove object from all collections not used in a scene
    bpy.ops.collection.objects_remove_all()
    # add it to our specific collection
    bpy.data.collections['Rods'].objects.link(obj)
   # obj.location  = obj.location + mathutils.Vector((x*r+r/2,y*r,z*r))
    bpy.ops.transform.translate(value=(x*r,y*r,z*r))
    

def alignRodX():
    bpy.ops.transform.resize(value=(r/2, 0.1, 0.1))
    bpy.ops.transform.translate(value=(r/2,0,0))
    
    
def alignRodY():
    bpy.ops.transform.resize(value=(0.1, r/2, 0.1))
    bpy.ops.transform.translate(value=(0,r/2,0))
  
    
def alignRodZ():
    bpy.ops.transform.resize(value=(0.1, 0.1, r/2))
    bpy.ops.transform.translate(value=(0,0,r/2))
  
        
def addMesh(w,h,d):
    for x in range(w):
        for y in range(h):
            for z in range(d):
                addBall(x,y,z)
    for x in range(w):
        for y in range(h):
            for z in range(d):    
                if x!= w-1:
                    addRod(x,y,z)
                    alignRodX()
                if y != h-1:
                    addRod(x,y,z)
                    alignRodY()
                if z != d-1:
                    addRod(x,y,z)
                    alignRodZ()
                            
    
def setupCollection(name): # deletes and creates a new collection called name

    collection = bpy.data.collections.get(name)
    try:
        bpy.data.collections.remove(collection)
    finally:
        
        collection = bpy.data.collections.new(name)
        bpy.context.scene.collection.children.link(collection)
       
def cleanUp():
    for block in bpy.data.objects: #remove orphaned nodes
        if not block.users:
            bpy.data.objects.remove(block)
    for block in bpy.data.meshes: #remove orphaned nodes
        if not block.users:
            bpy.data.meshes.remove(block)
    for block in bpy.data.materials: #remove orphaned nodes
        if not block.users:
            bpy.data.materials.remove(block)
if __name__ == "__main__":

    setupCollection("Balls")   
    setupCollection("Rods")   
    
    addMesh(3,3,3)

    cleanUp()
