
class Common:

  def create_general_body(self, parent, prefix, name,
                            body_pos, body_quat,
                            joint, collision, visual, inertial
                           ):
      generic_body = parent.add(
         'body',
          pos=body_pos,
          quat=body_quat
      )

      generic_body.add(
        'joint',
        name = joint["name"] + "_" + prefix if prefix else joint["name"],
        range = joint["range"]
      )

      # inertial
      generic_body.add(
        'inertial',
        mass = inertial["mass"],
        pos = inertial["pos"],
        diaginertia= inertial["diaginertia"]
      )

      # geoms visual
      self.add_vis(
         body = generic_body,
         mesh = visual["mesh"],
         pos = visual["pos"],
         quat = visual["quat"],
         material = visual["material"]
      )

      # geoms collision
      self.add_col(
        body = generic_body,
        name = collision["name"] + "_b_1",
        size = collision["size"],
        pos  = collision["pos"]
      )

      return generic_body

  def add_vis(self,body,mesh,material,pos=None,quat=None):
    if  pos==None and quat==None:
      body.add(
          'geom',
          mesh = mesh,
          material = material,

          #Default
          type="mesh",
          contype="0",
          conaffinity="0",
          group="2"
      )
    elif pos and quat==None:
       body.add(
        'geom',
        pos = pos,
        mesh = mesh,
        material = material,  
        #Default
        type="mesh",
        contype="0",
        conaffinity="0",
        group="2"
      )
    elif quat and  pos==None:
        body.add(
        'geom',
        quat=quat,
        mesh = mesh,
        material = material,  
        #Default
        type="mesh",
        contype="0",
        conaffinity="0",
        group="2"
      )
       
    elif pos and quat:
      body.add(
        'geom',
        pos = pos,
        quat=quat,
        mesh = mesh,
        material = material,  
        #Default
        type="mesh",
        contype="0",
        conaffinity="0",
        group="2"
      )

        

  def add_col(self,body,name,size,pos,euler=[0,0,0]):
      body.add(
        'geom',
        name = name,
        pos = pos,
        euler = euler,
        size=size,

        #Default
        group="3",
        type="box",
        mass="0",
        material="green"
        )

  def add_inertial(self,body,mass,mesh,material,pos=None,quat=None):
     body.add(
        'geom',
        pos = pos if pos else [0,0,0],
        quat = quat if quat else [0,0,0,1],
        mass=mass,
        mesh = mesh,
        material = material,

        #Default
        type="mesh",
        group="4"
     )
