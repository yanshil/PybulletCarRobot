import pybullet as p
import time
import pybullet_data
physicsClient = p.connect(p.GUI)#or p.DIRECT for non-graphical version
p.setAdditionalSearchPath(pybullet_data.getDataPath()) #optionally
p.setGravity(0,0,-10)
planeId = p.loadURDF("plane.urdf")
cubeStartPos = [0,0,0]
cubeStartOrientation = p.getQuaternionFromEuler([0,0,0])
robotId = p.loadURDF("simple_cuboid_4074g.urdf",cubeStartPos, cubeStartOrientation, 
                   flags=p.URDF_USE_INERTIA_FROM_FILE
                   )

wheel_id = [1, 2, 0, 3]
wheel_name = ['BR', 'FR', 'BL', 'BF']
wheel_velocity = [-13 ,-18, 2.7, 14.7]

for j in range(p.getNumJoints(robotId)):
    info = p.getJointInfo(robotId, j)
    jid = info[0]
    jname = info[1].decode("utf-8")
    jtype = info[2]
    if jtype == p.JOINT_REVOLUTE:
        print(jname)
        p.setJointMotorControl2(bodyUniqueId=robotId, 
                                jointIndex=jid, 
                                controlMode=p.VELOCITY_CONTROL,
                                force = 0)

p.setPhysicsEngineParameter(enableConeFriction=0)

for wid, wvec in zip(wheel_id, wheel_velocity):
    p.setJointMotorControl2(bodyUniqueId=robotId, 
                            jointIndex=wid, 
                            controlMode=p.VELOCITY_CONTROL,
                            targetVelocity = wvec,
                            force = 5)

for i in range (10000):
    p.stepSimulation()
    time.sleep(1./240.)

p.disconnect()

