## README

This is a repo to store related material of [this issue](https://github.com/bulletphysics/bullet3/issues/2851)

```
pip install pybullet
```

Model:
1. Pybullet_racecar
2. simple_cuboid
3. Mecanum_simple

### Hello_example
```
cd Pybullet_racecar
python hello_racecar.py
```

## Complex_custmoize
```
cd src
python run.py
```

### About info_dict

For every robot folder, it has it's own info_dict

### 2020/7/11

Update based on 

> disable all the motor constraints of the Roller by this p.setJointMotorControl2(objUid, linkIndex, p.VELOCITY_CONTROL, force=0) which is a tedious work, so i just change the maxMotorImpulse to 0 when create the default motor constraint in the function PhysicsServerCommandProcessor::createJointMotors() and then rebuilt the engine.
> disable the cone frition by this p.setPhysicsEngineParameter(enableConeFriction=0).


### 2020/6/26 

1. Create a new conda environment

```
conda crate -n bulletTest python=3
conda activate bulletTest
```

2. Build from source and test (Modify paths accordingly!!!)

```
git clone https://github.com/bulletphysics/bullet3.git
cd bullet3
rm CMakeCache.txt
mkdir build_cmake
cd build_cmake
cmake -DBUILD_PYBULLET=ON -DBUILD_PYBULLET_NUMPY=OFF -DUSE_DOUBLE_PRECISION=ON -DCMAKE_BUILD_TYPE=Release -DPYTHON_SITE_PACKAGES=/home/yanshimsi/miniconda3/envs/bulletTest/lib/python3.8/site-packages -DPYTHON_EXECUTABLE:FILEPATH=/home/yanshimsi/miniconda3/envs/bulletTest/bin/python3 -DPYTHON_INCLUDE_DIR:PATH=/home/yanshimsi/miniconda3/envs/bulletTest/include/python3.8 -DPYTHON_LIBRARY:FILEPATH=/home/yanshimsi/miniconda3/envs/bulletTest/lib/libpython3.8.so ..
make -j 4
cd examples
cd pybullet
export PYTHONPATH=$PYTHONPATH:"$(pwd)"
#ln -s pybullet.dylib pybullet.so
#python -c "import pybullet"

cd /mnt/d/GitHub/PybulletCarRobot/bullet3/examples/pybullet/gym/
export PYTHONPATH=$PYTHONPATH:"$(pwd)"
```

* Test before applying fix

```
cd /mnt/d/GitHub/PybulletCarRobot/mecanum_simple
python hello_mecanum.py

pip install scipy matplotlib
cd /mnt/d/GitHub/PybulletCarRobot/src
python run.py
## Will generate a video
```

3. Apply fix and test

```
cd /mnt/d/GitHub/PybulletCarRobot/bullet3
git apply ../patch.diff
### error: corrupt patch at line 101
```
