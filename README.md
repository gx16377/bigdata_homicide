# bigdata_homicide
PerMonth下是每项按月统计的结果  
	年龄按5岁一档划分了，-1是原来的0(unknown)或者998（不知道什么玩意，只要998，凶手带回家？  
NNdata下是转成每行一条，第一列是要预测的结果（真实值），后面是预测的参数的格式，暂时是年龄或州id什么的、月份、前5个月数据、前5年同月数据  
state.m是matlab的神经网络预测代码，结果上只比用前5年同月数据平均值预测好一点点  

--6.5--  
预测每个州的案件的把数据异常的那几个州去掉了  
把所有州（或其他的）一个模型的补全了，结果放在res里，格式：州id(或年龄)、年、月、真实值、预测值  
试了试每个州训练一个模型，效果不好，其他的还没试  
截图里ground是真实值的平均数，error_avg是用前5个月的平均值作为预测的平均误差，error_nn是神经网络预测的误差

##喵？
vis目录里是可视化的货
* 地图&时间轴，展示各州案件数随时间变化
* 接楼上，点击地图上的某个州，跳转到详细数据展示
* 2楼不存在的，还没做好
 