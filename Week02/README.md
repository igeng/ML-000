学习笔记
# 后续关注极客大学的 NLP + CV 训练营

# 前言：追求极致性能直接用C/C++

# python代码优化重点：
## 1、使用profiler分析工具对代码运行时间进行分析，找到代码运行的瓶颈--即消耗时间最多的地方进行优化；
## 2、一定要从大到小，由浅入深，由粗到细进行优化：
### （1）首先在python的代码层面上进行优化，即时间复杂度分析，减少循环，分解复杂运算操作，抽出重复计算的部分，
###		将重复使用的操作返回的结果使用统一的变量表示，这样使得相应的操作只做一次就够了。
### （2）在python层面上优化到不能优化了，再使用底层的语言如Cython和C++进行操作。
###	（3）最后再考虑多进程和多线程，即并发，但是这里涉及到python的GIL（全局解释器）造成了伪并发，考虑使用Openmp绕过GIL。
## GIL：https://blog.csdn.net/weixin_41594007/article/details/79485847

# profiler
## 1、优化原则：profiler-based optimization
### （1）将profiler分析工具当作显微镜，当观察到不同代码块之间的花销几乎一样，优化完毕，睡觉咯
### （2）实在不行，换框架
## 2、优化顺序
### （1）算法本身
### （2）算法复杂度
### （3）实现细节
### （4）
## line_profiler的使用：https://blog.csdn.net/guofangxiandaihua/article/details/77825524

# 寻找hotspots
## 使用profiler工具进行寻找
## 常用工具：function profiler、line profiler、Vtune

# Tips：万事不决，先看内存读取，其实也给我一个思路，在函数参数入口处也可以看做读取数据，这里的参数形式要好好优化！

# 内存层次：内存-Cache-Register
# Cache最关键重要：尽量保证成批读取邻近的数据，考虑一块内存的同一块数据反复读

# Tips：阅读VTune-Cookbook

# SIMD： 
## 保证数组排列连续
## https://zhuanlan.zhihu.com/p/31271788
## https://www.cnblogs.com/xidian-wws/p/11023762.html
## Wikipedia https://en.wikipedia.org/wiki/SIMD
## 专栏系列 https://zhuanlan.zhihu.com/p/55403951

# Vtune c++ cython
## https://software.intel.com/content/www/us/en/develop/articles/qualify-for-free-software.html

## https://software.intel.com/content/www/us/en/develop/documentation/vtune-cookbook/top/tuning-recipes/cache-misses-in-segmented-cache.html

# openmp
## https://www.openmp.org//wp-content/uploads/openmp-examples-4.5.0.pdf

# data leakage 数据泄露

作业说明
# 作业分为两种形式，一个是在colab上完成的jupyter notebook版本，一个是.py文件
# 第一份代码添加了每一个版本的说明，和最后的结果展示，按照优化程度由简单到复杂排列，
# 第二份代码是尽量以工程代码格式写的，在本次作业中对于line_profiler的使用，写了一个简单的实现方式，可以直接运行python文件即可输出时间消耗

参考：https://mp.weixin.qq.com/s/-Vr0u5dH4cCAOMRf_Dss_Q，一位同学写的十分详尽的代码优化思路和实现，感谢分享！









