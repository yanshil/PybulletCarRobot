
"""
Corresponding info_dict is located in that model folder.
Just copy the info_dict to replace the following to indicate the motor ID.

options: 
    global_wheel_control: bool. If yes, one value for all wheel.
    GUI_friction: bool. If yes, you can also change friction value during simulation with GUI
    trajPlot: path. Save trajectory to a plot
    dat_savePath: path. Save (x, y, theta) to somewher
    log_mp4: path. Dump a video of the simulation.
"""

from CarRobot import CarRobot

if __name__ == "__main__":
    info_dict = {
        'jointId': {3: 'BackRight',
                    7: 'FrontRight',
                    2: 'BackLeft',
                    5: 'FrontLeft'},
        'init_motorStatus': {3: {'controlMode': 0, 'targetVelocity': -13, 'force': 5},
                                7: {'controlMode': 0, 'targetVelocity':-8, 'force': 5},
                                2: {'controlMode': 0, 'targetVelocity': 0, 'force': 5},
                                5: {'controlMode': 0, 'targetVelocity': 20, 'force': 5}},
        'init_physical_para': {3: {'lateralFriction': .7, 'angularDamping': 0, 'linearDamping': 0, 'rollingFriction': 0, 'spinningFriction': 0},
                                7: {'lateralFriction': .7, 'angularDamping': 0, 'linearDamping': 0, 'rollingFriction': 0, 'spinningFriction': 0},
                                2: {'lateralFriction': .7, 'angularDamping': 0, 'linearDamping': 0, 'rollingFriction': 0, 'spinningFriction': 0},
                                5: {'lateralFriction': .7, 'angularDamping': 0, 'linearDamping': 0, 'rollingFriction': 0, 'spinningFriction': 0}}}

    options = {'global_wheel_control': False, 
               'GUI_friction': False, 
                # 'trajPlot': "disableConeFriction_initMaxPulseZero.png",
                # 'trajPlot': "initMaxPulseZeroOnly.png",
                # 'trajPlot': "disableConeFrictionOnly.png",
                'trajPlot': "original.png",
                # 'dat_savePath': './output/test.txt',
                # 'log_mp4': 'test.mp4'
                }
    
    init_config = {
                # 'disableConeFriction': True,
                # 'initMaxPulseZero': True
    }

############# Run #####################
    c = CarRobot("../Pybullet_racecar/racecar_fix_steer.urdf", info_dict, GUI=False, init_config=init_config,
                 options=options, timesteps = 3600, debug=False, start_pos=[0, 0, 0.0007], start_ori = [0, 0, 0, 1])
    c.run()
