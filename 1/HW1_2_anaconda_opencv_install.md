# Anaconda install
Since Miniconda is already enough for basic function, we give an example of installing Miniconda instead of Anaconda for convenience. \
Basic steps of installing miniconda and Anaconda are similar.

## Environment
UBUNTU 16.04 

## Step
* Download run file. \
We downloaded version Miniconda3-py39_4.9.2-Linux-x86_64.sh. \
[miniconda](https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh) \
[anaconda](https://repo.anaconda.com/archive/Anaconda3-2021.05-Linux-x86_64.sh)

* Run the following command to install miniconda sh file. 
```
sh Miniconda3-py39_4.9.2-Linux-x86_64.sh
```
* Pressing ENTER and accept license terms.

* Installation completed
* Create conda environments \
torch_1.6 is env name, set anyname as you like and I choosed python of version 3.6 here.
```
conda create -n torch_1.6 python=3.6
```
* Activate environment
```
conda activate torch_1.6
```
# Opencv install
* install with conda with specific version
``` 
conda install opencv-python
```
* install specific version with pip
```
pip install opencv-python==4.1.0.25
```
or install default version
```
pip install opencv-python
```

