
materials = [
   {
      "name" :"gray",
      "rgba":[0.4, 0.4, 0.4, 1]
   },
   {
      "name" :"yellow",
      "rgba":[0.866667, 0.866667, 0.0509804, 1]
   },
   {
      "name" :"light_orange",
      "rgba":[1, 0.749, 0, 1]
   },
   {
      "name" :"green",
      "rgba":[0.11, 1, 0, 0.2]
   },
   {
    "name":"red",
    "rgba":[0.603922, 0.14902, 0.14902, 1] 
   }
]

dir_path = "assets/"
meshes = [
  "dip.stl",
  "pip.stl",
  "fingertip.stl",
  "mcp_joint.stl",

  "thumb_pip.stl",
  "thumb_fingertip.stl",
  "thumb_dip.stl",
  "palm_lower.stl"
]


# Palm site where fingers can be attached
fingers_pos ={
  "FF":[-0.00709525, 0.0230578, -0.0187224],
  "MF":[-0.00709525, -0.0223922, -0.0187224],
  "RF":[-0.00709525, -0.0678422, -0.0187224],
  "TH":[-0.0693952, -0.00124224, -0.0216224]
}
fingers_quat = {
  "FF":[0.5, 0.5, 0.5, -0.5],
  "MF":[0.5, 0.5, 0.5, -0.5],
  "RF":[0.5, 0.5, 0.5, -0.5],
  "TH":[0.707107, 0, 0.707107, 0],
}
