## pipenv

- 概览
```bash
pipenv 
1. 集成了virtualenv, pip, pyenv三者的功能
2. 自动的创建和管理虚拟环境
3. 使用 Pipfile 文件添加或删除安装的包, 
    同时生成Pipfile.lock来锁定安装包的版本和依赖信息, 避免构建错误.
```

- 安装
```angular2
$ pip3 install pipenv
```

- 常用命令
```bash
// 可以初始化一个python3的虚拟环境
$ pipenv --three

// 可以初始化一个python2的虚拟环境
$ pipenv --two

//创建一个3.6.8的虚拟环境
$ pipenv --python 3.6.8 

// 激活虚拟环境
$ pipenv shell
$ pipenv run python main.py

// 更新所有依赖包
$ pipenv update

// 更新指定依赖包
$ pipenv update ipython

// 卸载包
$ pipenv uninstall ipython

// 生成requirements.txt文件
$ pipenv lock -r

// 生成dev-packages的requirements.txt文件
$ pipenv lock -r -d

// 用编辑器打开requests模块
$ pipenv open ipython
```