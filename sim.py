import pybullet as p
import pybullet_data
import time

p.connect(p.GUI)

p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.loadURDF("plane.urdf", [0, 0, 0.0])
p.setGravity(0,0,0)




dummy=p.loadURDF("urdf/dummy.urdf", [0, 0, 0.0])
p.setJointMotorControl2(dummy, 0, p.VELOCITY_CONTROL, 0, force=0)
p.setJointMotorControl2(dummy, 1, p.VELOCITY_CONTROL, 0, force=0)
p.setJointMotorControl2(dummy, 2, p.VELOCITY_CONTROL, 0, force=0)
p.setJointMotorControl2(dummy, 3, p.VELOCITY_CONTROL, 0, force=0)
while 1:
	p.stepSimulation()
	time.sleep(0.001)
p.disconnect()
