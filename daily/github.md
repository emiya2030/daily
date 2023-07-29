备份Dataloader

测试0.25是否可以正常生成


修改了result保存位置

结论 我训练的有问题

补救措施


2.看看元数据smpl和田中出力的smpl的对比

24csv存入output

田中的数据 smpl生成的结果和原点群非常接近
即使里面的数值差异大

# 已经知道有一个训练成功的网络

## 就用他测试出正确的mytest

mytest的设置没有问题

原因 我用之前的log测试了






3.loss

1.看看训练是哪部没对

查看生成result和log对应


# 猜想 有一半身体被遮挡
导致生成很糟糕

image/30里 存放所有的0.25intersection_30degree 训练的vert


0.25以后就是田中结果


log 0.25intersection_30degree 

result_verts/test30