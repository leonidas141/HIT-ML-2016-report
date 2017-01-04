##原理与基本概念

K近邻算法(K Nearest Neighbor)，又称KNN算法，是机器学习中一种比较经典的算法。在根据有无监督分类中，属于监督学习方法。由Bhattacharya和Gangopadhyay在1990年提出$ ^{[1]}$。

KNN算法是一种用于分类和回归的非参数统计方法。在KNN分类中，输出为一个分类族群。一个对象的分类是由其邻居的“多数表决”决定的，k个最近邻居中最常见的分类决定了赋予该对象的类别，若k=1，则该对象与最近的一个对象相同。KNN方法采用向量空间模型来分类，类型相同的个体之间，彼此之间的相似度高，可以计算待分类样本与已知数据的相似程度来将其分类。

K近邻算法与其他分类器类似，包括两个阶段：训练和分类。

在训练阶段，只需要输入特征向量和标签。训练样本是多维特征空间向量，每个样本带有一个类别标签。

在训练阶段，需要输入一个常熟$k$和一个测试数据的特征空间向量。此特征向量将会被归类为最接近该点的$k$个样本点中最频繁出现的一类。

为了衡量两个样本之间的距离，需要引入一种度量单位。这一单位可以使用欧氏距离，海明距离或者其他特殊算法，例如邻近成分分析法等。其中，欧氏距离和海明距离分别适用于连续样本和离散样本，本次实验中选择海明距离作为度量单位，描述手写文字之间的距离。

##伪代码

***

__Algorithm 1. (PseudoCode for K Nearist Neighbor)__

***

begin



##K近邻算法的程序实现

这一部分使用Python实现K近邻算法的实现

##使用K近邻算法实现手写数字识别

这一部分使用Python实现K近邻算法的实现与调用。

使用数据集进行测试和

##对K近邻算法的分析