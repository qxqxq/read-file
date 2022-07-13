# readfile


## 安装python3.7.3
1. 参考博客 https://blog.csdn.net/qq_23518283/article/details/94388366?spm=1001.2014.3001.5501
    ```
    git clone https://gitee.com/krypln/pyenv.git ~/.pyenv
    echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
    echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
    echo 'eval "$(pyenv init -)"' >> ~/.bashrc
    source ~/.bashrc
    
    mkdir ~/.pyenv/cache
    wget -c https://npm.taobao.org/mirrors/python/3.7.3/Python-3.7.3.tar.xz -P  ~/.pyenv/cache/
    
    # 在安装python之前，要先安装python的一些依赖包，否则会安装失败
    sudo apt-get install libc6-dev gcc
    sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm

    pyenv install -v 3.7.3
    pyenv global 3.7.3
    
    # 查看python和pip版本，确保是3.7.3
    root@BUPT:/mnt/core_network# python -V
    Python 3.7.3
    root@BUPT:/mnt/core_network# pip -V
    pip 19.0.3 from /root/.pyenv/versions/3.7.3/lib/python3.7/site-packages/pip (python 3.7)
    
    pip install pqi
    pqi use aliyun
    # 安装python 包管理工具
    pip install pipenv
    ```

## git 
1. cd /mnt
2. git clone https://github.com/qxqxq/read-file.git

## docker 启动

```
# 从容器快照文件中导入基础镜像，或直接在仓库拉取基础镜像文件
cat ubuntu18.04-py3.7-v1.0.tar | docker import - ubuntu18.04-py3.7:v1.0

cd /mnt/read-file

# 启动
docker-compose up -d
# 停止
docker-compose stop
```

## 终端启动方式：
项目默认放在/mnt下
1. 新开一个终端，启动web程序
- cd /mnt/read-file
- pipenv sync
- pipenv shell
- python manage.py
