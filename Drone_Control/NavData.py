import time, sys
import ps_drone                                                               # Import PS-Drone-API
import markerDetection as marker
import detectGesture as dG

drone = ps_drone.Drone()                                                      # Start using drone					
drone.startup()                                                               # Connects to drone and starts subprocesses

drone.reset()                                                                 # Sets drone's status to good (LEDs turn green when red)
while (drone.getBattery()[0] == -1):  time.sleep(0.1)                         # Wait until the drone has done its reset
print "Battery: "+str(drone.getBattery()[0])+"%  "+str(drone.getBattery()[1]) # Gives a battery-status
drone.useDemoMode(False)                                                      # Give me everything...fast
drone.getNDpackage(["demo","pressure_raw","altitude","magneto","wifi"])       # Packets, which shall be decoded
time.sleep(1.0)                                                               # Give it some time to awake fully after reset

print "Altitude"+str(drone.NavData["altitude"][3])
drone.takeoff()                # Drone starts
time.sleep(7.5)                # Gives the drone time to start
drone.setSpeed(0.09)            # Sets default moving speed to 1.0 (=100%)

##### Mainprogram begin #####
NDC = drone.NavDataCount
IMC = drone.VideoImageCount
end = False
detected = False

drone.setConfigAllID()				# Go to multiconfiguration-mode
drone.sdVideo()						# Choose lower resolution (hdVideo() for...well, guess it)
drone.frontCam()					# Choose front view
CDC = drone.ConfigDataCount
while CDC == drone.ConfigDataCount:	time.sleep(0.0001)	# Wait until it is done (after resync is done)
drone.startVideo()					# Start video-function
palm_counter = 0
fist_counter = 0
v_counter = 0

while not end:
    while drone.NavDataCount == NDC:  time.sleep(0.001)                       # Wait until next time-unit
    #	# Wait until the next video-frame
    
    if drone.getKey():                end = True                              # Stop if any key is pressed
    NDC=drone.NavDataCount
    if drone.NavData["altitude"][3] < 1100:
    	drone.moveUp(0.09)
    elif drone.NavData["altitude"][3] >= 1200 and drone.NavData["altitude"][3] <= 1290:
    	drone.stop()
    	while drone.VideoImageCount==IMC: time.sleep(0.01)
    	IMC = drone.VideoImageCount
    	img  = drone.VideoImage					# Copy video-image
    	detected = dG.detectHandGesture(img)
        if detected == "V_Symbol":
            for i in range(3):
                drone.moveLeft()
                time.sleep(1)
            for i in range(3):
                drone.moveRight()
                time.sleep(1)
            print "detected V - moving left"
            drone.stop()
        elif detected == 'G_Symbol':
            for i in range(3):
                drone.moveRight()
                time.sleep(1)
            for i in range(3):
                drone.moveLeft()
                time.sleep(1)
            print "detected g - moving right"
            drone.stop()

        elif detected == 'Palm':
            for i in range(3):
                drone.moveBackward()
                time.sleep(1)
            for i in range(3):
                drone.moveForward()
                time.sleep(1)
            print "detected Palm - moving Backward"
            drone.stop()

        elif detected == 'LittleFinger':
            for i in range(3):
                drone.moveForward()
                time.sleep(1)
            for i in range(3):
                drone.moveBackward()
                time.sleep(1)
            print "detected LittleFinger - moving Forward"
            drone.stop()

        elif detected == 'Fist':
            cv2.imwrite(str(counter)+".jpg", img)
        	print str(counter)+".jpg" + "Clicking Pictures"
        	time.sleep(1)

	else:
		drone.moveDown(0.09)

drone.land()