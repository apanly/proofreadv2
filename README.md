#python 文本纠错
####近来发现语言识别过程中会有很多是有偏差了的,经常查询发现lucene可以实现纠错功能，前提是需要大量的文本，后来发现有pylucene就想到了用这个

#开发语言
* python

#python依赖包
* PyLucene
* jcc

#如何使用
* python javaproofread.py


#遇到的问题
* 一直报错：lucene.InvalidArgsError: (<type 'SpellChecker'>, 'indexDictionary', (<PlainTextDictionary: org.apache.lucene.search.spell.PlainTextDictionary@51cc87e3>,)),感觉没错了

#解决方案
* 虽然pylucene是python版的，但是也是需要java运行环境的，所以我觉得还不如就用java的服务算了，由于都是在同一台机器，就想到了socket通信
  java做服务端，python做客户端
* 还有一直比较二逼的方法，在java生成字典，复制到python的工作目录，这个想法听起来就听二的，不过也是一种解决方法，当然最好的就是把报错解决掉了





#How to install jcc
*  wget https://pypi.python.org/packages/source/J/JCC/JCC-2.17.tar.gz
*  cd JCC-2.17
*  python setup.py build
*  sudo python setup.py install

#How to install pylucene
#####PyLucene is a Python extension built with JCC.
* wget http://mirror.bit.edu.cn/apache/lucene/pylucene/pylucene-3.6.2-1-src.tar.gz
* cd pylucene-3.6.2-1
* 修改Makeifle 根据自己的版本打开不同的地方
  打开了这几行注释：

  >   # Linux     (Ubuntu 11.10 64-bit, Python 2.7.2, OpenJDK 1.7)
  
       PREFIX_PYTHON=/usr
  
       ANT=ant
  
       PYTHON=$(PREFIX_PYTHON)/bin/python
  
       JCC=$(PYTHON) -m jcc --shared
  
       NUM_FILES=3

   修改-m jcc 为 -m jcc.__main__
* 编译安装
  make
  sudo make install

