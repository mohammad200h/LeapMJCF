from dm_control import mjcf

from config import dir_path, materials, meshes , fingers_pos, fingers_quat

from modeling_util import Common

class Palm(Common):
  def __init__(self,prefix=None):
    self.model = mjcf.RootElement()


    # Material
    for m in materials:
      self.model.asset.add('material',name=m["name"], rgba=m["rgba"])

    # Meshes
    for m in meshes:
       self.model.asset.add('mesh', file =dir_path + m )

    # Palm
    self.palm = self.create_palm(prefix)

    


  
    
      

  def create_palm(self,prefix=None):
    palm = self.model.worldbody.add('body', name="palm")

    # inertial
    self.add_inertial(
      body = palm,
      mass = 0.044,
      mesh= "palm_lower",
      material="gray"
    )

    # geoms visual
    self.add_vis(
       body = palm,
       mesh = "palm_lower",
       pos = [-0.0200952, 0.0257578, -0.0347224],
       quat = [1, 0, 0, 0],
       material = "red"
    )

    # geoms collision
    box_one_size = [0.012, 0.015, 0.02]
    positions = [
       [-0.008, 0.009, -0.01],
       [-0.008, -0.037, -0.01],
       [-0.008, -0.082, -0.01]
    ]
    for i, pos in enumerate(positions):
      self.add_col(
        body = palm,
        name = "palm_b_"+str(i+1),
        size = box_one_size,
        pos  = pos
      )

    self.add_col(
      body = palm,
      name = "palm_b_4",
      size = [0.022, 0.064, 0.025],
      pos  = [-0.041, -0.036, -0.01]
    )
    self.add_col(
      body = palm,
      name = "palm_b_5",
      size = [0.02, 0.04, 0.025],
      pos  = [-0.082, -0.06, -0.01]
    )


    
    for finger in ["FF","MF","RF","TH"]:
      palm.add('site', name=finger , pos=fingers_pos[finger], quat=fingers_quat[finger])

    return palm

