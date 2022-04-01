# SpamDetection
to classify short message
## 1. 数据预处理
### 1.1 数据集
>使用带标签的中文短信数据集（五年前的），来源[FlyAI中文垃圾短信识别竞赛](https://flyai.com/d/SpamMessage)
*[数据集地址](https://github.com/hrwhisper/SpamMessage/tree/master/data)*

### 1.2 格式转换
>需要什么格式?

1. pickle
   - pickle模块支持python任意数据类型，包括对象。但是仅限于python程序间的交互
   - pickle模块的读写模式都是wb、rb类型的，文件需要以wb、rb模式打开
   - 被pickle序列化后的文件内容不可读，但是反序列化后可以取出数据
   
2. json
   - json 可以传递 字符串格式的字典、数组，不可以传递 元组
   - json 最后一行末尾不可以有‘ ，’
   - json 文件总 False True 需要用 false true 来表示
   - json 中的字符串必须用英文状态下的 双引号

### 1.3 划分数据集
>按6:2:2
划分出训练集、交叉验证集、测试集

*对于小规模样本集（几万量级），常用的分配比例是 60% 训练集、20% 验证集、20% 测试集*