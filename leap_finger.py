
# PyMJCF
from dm_control import mjcf
# config
from config import dir_path, materials, meshes
# model utility
from modeling_util import Common


class Finger(Common):
    def __init__(self,prefix=None):
      """4 DoF finger"""
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
   
      # Finger
      self.knuckle = self.create_knuckle(prefix)

      self.proximal = self.create_general_body(
          parent = self.knuckle,
          prefix = prefix,
          name = "proximal",
          body_pos = [-0.0122, 0.0381, 0.0145],
          body_quat = [0.5, -0.5, -0.5, 0.5],
          joint = {
            "name": "j1_FF",
            "range":[-1.047, 1.047]
          },
          visual = {
             "pos":[0.00964336, 0.0003, 0.000784034],
             "quat":[0.5, -0.5, -0.5, -0.5],
             "mesh":"pip",
             "material":"yellow"
          },
          collision = {
            "name":"proximal_b_1",
            "pos":[0.01, 0.0, -0.013],
            "size":[0.02, 0.015, 0.01]
          },
          inertial = {
             "mass":0.032,
             "pos":[0,0,0],
             "diaginertia":[4.7981e-06, 4.23406e-06, 2.86184e-06]
          }
      )

      self.middle = self.create_general_body(
          parent = self.proximal,
          prefix = prefix,
          name = "middle",
          body_pos = [0.015, 0.0143, -0.013],
          body_quat = [0.5, 0.5, -0.5, 0.5],
          joint = {
            "name": "j2_FF",
            "range":[-0.506, 1.885]
          },
          visual = {
             "pos":[0.0211334, -0.00843212, 0.00978509],
             "quat":[0, -1, 0, 0],
             "mesh":"dip",
             "material":"yellow"
          },
          collision = {
            "name":"middle_b_1",
            "pos":[0.0105, -0.034, 0.015],
            "size":[0.02, 0.014, 0.015]
          },
          inertial = {
             "mass":0.037,
             "pos":[0,0,0],
             "diaginertia":[6.68256e-06, 6.24841e-06, 5.02002e-06]
          }
      )

      self.distal = self.create_general_body(
          parent = self.middle,
          prefix = prefix,
          name = "distal",
          body_pos = [-4.08806e-09, -0.0361, 0.0002],
          body_quat = None,
          joint = {
            "name": "j3_FF",
            "range":[-0.366, 2.042]
          },
          visual = {
             "pos":[0.0132864, -0.00611424, 0.0145],
             "quat":[0, 1, 0, 0],
             "mesh":"fingertip",
             "material":"yellow"
          },
          collision = {
            "name":"distal_b_1",
            "pos":[0.0009, -0.034, 0.0145],
            "size":[0.012, 0.014, 0.012]
          },
          inertial = {
             "mass":0.016,
             "pos":[0,0,0],
             "diaginertia":[3.37527e-06, 2.863e-06, 1.54873e-06]
          }
      )

    def create_knuckle(self,prefix):
      knuckle = self.model.worldbody.add('body', name="knuckle" )

      knuckle.add(
        'joint',
        name = "knuckle_"+prefix if prefix else "knuckle",
        range = [-0.314, 2.23]
      )

      # inertial
      knuckle.add(
        'inertial',
        mass = 0.044,
        pos=[0, 0, 0],
        diaginertia=[1.47756e-05, 1.31982e-05, 6.0802e-06]
      )

      # geoms visual
      self.add_vis(
         body = knuckle,
         mesh = "mcp_joint",
         pos = [0.0084069, 0.00776624, 0.0146574],
         quat = [1, 0, 0, 0],
         material = "gray"
      )

      # geoms collision
      self.add_col(
        body = knuckle,
        name = "knuckle_b_1",
        size = [0.012, 0.015, 0.02],
        pos  = [0.0, 0.008, 0.015]
      )
      self.add_col(
        body = knuckle,
        name = "knuckle_b_2",
        size = [0.015, 0.025, 0.015],
        pos  = [-0.03, 0.04, 0.018]
      )

      return knuckle


class FingerXML(object):
    pass




finger = Finger()
print(finger.model.to_xml_string())