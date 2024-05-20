
# PyMJCF
from dm_control import mjcf
# config
from config import dir_path, materials, meshes
# model utility
from modeling_util import Common

class Thumb(Common):
  def __init__(self,prefix=None):
    self.model = mjcf.RootElement()

    # Material
    for m in materials:
      self.model.asset.add('material',name=m["name"], rgba=m["rgba"])

    # Meshes
    for m in meshes:
       self.model.asset.add('mesh', file =dir_path + m )

    # Defaults
    self.model.default.joint.type = 'hinge'
    self.model.default.joint.damping = 2000
    self.model.default.joint.axis = [0, 0, -1]

    # Thumb
    self.knuckle = self.create_knuckle(prefix)

    self.proximal = self.create_proximal(parent = self.knuckle)

    self.middle = self.create_general_body(
        parent = self.proximal,
        prefix = prefix,
        name = "middle",
        body_pos = [0, 0.0145, -0.017],
        body_quat = [0.707107, -0.707107, 0, 0],
        joint = {
          "name": "j2_TH",
          "range":[-1.2, 1.9]
        },
        visual = {
           "pos":[0.0439687, 0.057953, -0.00862868],
           "quat":[1, 0, 0, 0],
           "mesh":"thumb_dip",
           "material":"yellow"
        },
        collision = {
          "name":"middle_b_1",
          "pos":[-0.005, 0.01, -0.0135],
          "size":[0.015, 0.02, 0.015]
        },
        inertial = {
           "mass":0.038,
           "pos":[0,0,0],
           "diaginertia":[8.48742e-06, 7.67823e-06, 3.82835e-06]
        }
    )

    self.distal = self.create_distal(parent = self.middle)

  def create_knuckle(self,prefix):
    knuckle = self.model.worldbody.add('body', name="knuckle")

    knuckle.add(
      'joint',
      name = "knuckle_"+prefix if prefix else "knuckle",
      range = [-0.349, 2.094]
    )

    # inertial
    knuckle.add(
      'inertial',
      mass = 0.032,
      pos=[0, 0, 0],
      diaginertia=[4.7981e-06, 4.23406e-06, 2.86184e-06]
    )

    # geoms visual
    self.add_vis(
       body = knuckle,
       mesh = "pip",
       pos = [-0.00535664, 0.0003, 0.000784034],
       quat = [0.5, -0.5, -0.5, -0.5],
       material = "yellow"
    )

    # geoms collision
    self.add_col(
      body = knuckle,
      name = "knuckle_b_1",
      size = [0.018, 0.015, 0.012],
      pos  = [-0.008, 0.0, -0.012]
    )

    return knuckle

  def create_proximal(self,parent):
    proximal = parent.add(
         'body',
          name = 'proximal',
          pos=[0, 0.0143, -0.013],
          quat=[0.5, 0.5, -0.5, 0.5]
    )

    proximal.add(
      'joint',
      name = "proximal",
      range = [-0.47, 2.443]
    )

    # inertial
    proximal.add(
      'inertial',
      mass = 0.003,
      pos=[0, 0, 0],
      diaginertia=[5.93e-07, 5.49e-07, 2.24e-07]
    )

    # geoms visual
    self.add_vis(
       body = proximal,
       mesh = "thumb_pip",
       pos = [0.0119619, 0, -0.0158526],
       quat = [0.707107, 0.707107, 0, 0],
       material = "yellow"
    )

    return proximal

  def create_distal(self,parent):
    distal = parent.add(
         'body',
          name = 'distal',
          pos=[0, 0.0466, 0.0002],
          quat=[0, 0, 0, 1]
    )

    distal.add(
      'joint',
      name = "distal",
      range = [-1.34, 1.88]
    )

    # inertial
    distal.add(
      'inertial',
      mass = 0.049,
      pos=[0, 0, 0],
      diaginertia=[2.03882e-05, 1.98443e-05, 4.32049e-06]
    )

    # geoms visual
    self.add_vis(
       body = distal,
       mesh = "thumb_fingertip",
       pos = [0.0625595, 0.0784597, 0.0489929],
       material = "yellow"
    )

    # geoms collision
    self.add_col(
      body = distal,
      name = "distal_b_1",
      size = [0.015, 0.02, 0.015],
      pos  = [0.005, -0.01, -0.014]
    )
    self.add_col(
      body = distal,
      name = "distal_b_2",
      size = [0.012, 0.014, 0.013],
      pos  = [0.00094, -0.05, -0.014]
    )


    return distal
  





