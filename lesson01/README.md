# 环境准备

```bash
开课前环境准备工作
1. 如果你用的Windows系统，建议在Windows上安装虚拟机，在虚拟机上安装Linux系统，Linux系统上运行Python环境；
2. 如果你用的是Mac系统，那么可以直接在Mac上运行Python环境；
3. 虚拟机建议用Virtualbox + Vagrant
```

## 1. Windows系统


### 1.1 安装虚拟机

> Virtualbox是一款虚拟机软件，Vagrant是Virtualbox的命令行管理软件；

- [Virtualbox Download](https://download.virtualbox.org/virtualbox/5.2.26/VirtualBox-5.2.26-128414-Win.exe)
- [Vagrant Download](https://releases.hashicorp.com/vagrant/2.2.4/vagrant_2.2.4_x86_64.msi)

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

> 测试
```bash
# python -V
```

### 1.3. IDE

- [Win Pycharm Download](https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=windows)

- 配置




## 2. Mac系统



### 2.1. Python 3.6
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

> 测试
```bash
# python -V
```


### 2.1. IDE

- [Mac Pycharm Download](https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=mac)
