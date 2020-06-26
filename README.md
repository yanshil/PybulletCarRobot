## README

Issue Link:

https://github.com/bulletphysics/bullet3/issues/2851


1. Create a new environment

```
conda crate -n bulletTest python=3
conda activate bulletTest
```

2. Build from source and test (Modify your paths accordingly!!!)

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

3. Apply fix and test

```
```



## Run


1. GUI control wheel velocity

```
cd src
## Copy the info_dict from model folder and modify urdf path
python run.py
```



2. Simple one-file script: in model folder and named as `hello_*.py`