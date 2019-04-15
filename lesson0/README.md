# 环境准备

```bash
开课前环境准备
- 1. 如果你用的Windows系统，建议在Windows上安装虚拟机，在虚拟机上安装Linux系统，Linux系统上运行Python环境；
- 2. 如果你用的是Mac系统，那么可以直接在Mac上运行Python环境；
- 3. 虚拟机建议用Virtualbox + Vagrant, 为什么要用这款软件了？？？ 
- 3.1 这款软件能够实现Windows下项目代码和Linux系统共享；
- 3.2 Pycharm支持连接Virtualbox里的Python环境；
```

## 1. Windows系统


### 1.1 安装虚拟机

> Virtualbox是一款虚拟机软件(类似于Vmware)，Vagrant是Virtualbox的命令行管理工具, Box是虚拟机镜像；

- [Virtualbox Download](https://download.virtualbox.org/virtualbox/5.2.26/VirtualBox-5.2.26-128414-Win.exe)
- [Box Centos6.6](https://github.com/tommy-muehle/puppet-vagrant-boxes/releases/download/1.0.0/centos-6.6-x86_64.box)
- [Vagrant Download](https://releases.hashicorp.com/vagrant/2.2.4/vagrant_2.2.4_x86_64.msi)

- [Box List](http://www.vagrantbox.es/)

> 1. 首先安装Virtualbox

xxx


### 1.2. Python 3.6
- [Linux Download](https://www.python.org/ftp/python/3.6.8/Python-3.6.8.tgz)


> Linux安装
```bash
# yum install gcc gcc-c++ make openssl openssl-devel
# cd /usr/local/src
# wget https://www.python.org/ftp/python/3.6.8/Python-3.6.8.tgz
# tar -zxvf Python-3.6.8.tgz
# cd Python-3.6.8
# ./configure --prefix=/usr/local/python36
# make -j
# mkae install
```

> 环境变量
```bash
# echo "export PATH=/usr/local/python36/bin:\$PATH" > /etc/profile.d/python36.sh
# source /etc/profile
```

> 测试
```bash
# python3 -V
Python 3.6.8
```

### 1.3. IDE

- [Pycharm Download](https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=windows)

- 配置




## 2. Mac系统


### 2.1. Python 3.6
- [Mac Download](https://www.python.org/ftp/python/3.6.8/Python-3.6.8.tgz)


> Mac安装
```bash
# yum install gcc gcc-c++ make openssl openssl-devel
# cd /usr/local/src
# wget https://www.python.org/ftp/python/3.6.8/Python-3.6.8.tgz
# tar -zxvf Python-3.6.8.tgz
# cd Python-3.6.8
# ./configure --prefix=/usr/local/python36
# make -j
# mkae install
```

> 环境变量
```bash
# echo "export PATH=/usr/local/python36/bin:\$PATH" > /etc/profile.d/python36.sh
# source /etc/profile
```

> 测试
```bash
# python3 -V
Python 3.6.8
```


### 2.2. IDE

- [Pycharm Download](https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=mac)
