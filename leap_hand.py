
# PyMJCF
from dm_control import mjcf

from leap_finger import Finger
from leap_thumb import Thumb
from leap_palm import Palm

class LeapHand(object):
  def __init__(self):
    
    palm = Palm().model

    # attaching fingers to site
    for finger in ["FF","MF","RF"]:
      site = palm.find('site',finger)
      site.attach(Finger().model)
    
    #attach thumb
    site = palm.find('site',"TH")
    site.attach(Thumb().model)

    self.model = palm


hand = LeapHand()

print(hand.model.to_xml_string())