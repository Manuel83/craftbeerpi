from util import *
from model import *
import httplib, urllib

def getserial():
  # Extract serial from cpuinfo file
  cpuserial = "0000000000000000"
  try:
    f = open('/proc/cpuinfo','r')
    for line in f:
      if line[0:6]=='Serial':
        cpuserial = line[10:26]
    f.close()
  except:
    cpuserial = "0000000000000000"

  return cpuserial

<<<<<<< HEAD
@brewinit(config_parameter="SEND_STATS")
=======
@brewinit()
>>>>>>> refs/remotes/Manuel83/master
def sendStats():
    app.logger.info("Sending stats")
    try:
        serial = getserial()
        info = {
        "id": serial,
<<<<<<< HEAD
        "version": "2.2",
=======
        "version": "2.1",
>>>>>>> refs/remotes/Manuel83/master
        "kettle": [],
        "hardware": [],
        "thermometer": app.brewapp_thermometer.__class__.__name__,
        "hardware_control": app.brewapp_hardware.__class__.__name__
        }
        for k in Kettle.query.all():
            info["kettle"].append({"name": k.name, "diameter":k.diameter, "height": k.height, "agitator": k.agitator, "heater": k.heater})

        for h in Hardware.query.all():
            info["hardware"].append({"name": k.name, "type":h.type, "switch":h.switch})
        import requests
        r = requests.post('http://www.craftbeerpi.com/stats.php', json=info)
        app.logger.info(r)
    except Exception as e:
        app.logger.error("Sending stats failed: " + str(e))
