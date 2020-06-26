## README

This is a repo to store related material of [this issue](https://github.com/bulletphysics/bullet3/issues/2851)


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
