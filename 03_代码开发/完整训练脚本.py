# 🔥 立即开始训练代码

## 📋 复制即用的完整代码

### 完整训练脚本 (train_plants.py)
```python
from fastai.vision.all import *
import matplotlib.pyplot as plt
from pathlib import Path

# ===== 1️⃣ 环境检查 =====
print("🔍 检查环境...")
try:
    import torch
    print(f"✅ PyTorch 版本: {torch.__version__}")
except:
    print("❌ 请先安装 PyTorch: pip install torch torchvision")

# ===== 2️⃣ 数据路径 =====
path = Path('D:/植物识别项目/02_数据集/10植物测试集')

# 检查数据文件夹
if not path.exists():
    print(f"❌ 数据文件夹不存在: {path}")
    print("请先在 D:/植物识别项目/02_数据集/10植物测试集 创建植物文件夹")
    exit()

# ===== 3️⃣ 数据加载 =====
print("📊 加载数据...")
try:
    # 创建数据加载器
    dls = ImageDataLoaders.from_folder(
        path,
        train_pct=0.8,      # 80%用于训练
        valid_pct=0.2,      # 20%用于验证
        seed=42,            # 固定随机种子，确保结果可复现
        item_tfms=Resize(224),  # 所有图片调整为224x224
        batch_tfms=augmentations  # 自动数据增强
    )

    print(f"✅ 数据加载成功！")
    print(f"📁 发现的植物类别: {len(dls.vocab)}")
    print(f"🌱 植物种类: {list(dls.vocab)}")

except Exception as e:
    print(f"❌ 数据加载失败: {e}")
    print("请检查每个植物文件夹是否包含图片")

# ===== 4️⃣ 查看数据示例 =====
print("🎨 展示一些数据样本...")
try:
    dls.show_batch(max_n=6, figsize=(6,6))
    plt.savefig('D:/植物识别项目/04_模型训练/数据示例.png')
    print("✅ 数据示例已保存")
except:
    print("⚠️ 无法显示图片（可能无图形环境）")

# ===== 5️⃣ 创建模型 =====
print("🧠 创建AI模型...")
learn = cnn_learner(dls, resnet34, metrics=accuracy)
print("✅ 模型创建成功！使用 ResNet34 预训练模型")

# ===== 6️⃣ 开始训练 =====
print("🏃 开始训练...这需要几分钟时间")
try:
    # 训练5轮，每轮会显示进度
    learn.fit(5)

    print("🎉 训练完成！")

    # 保存模型
    model_path = 'D:/植物识别项目/04_模型训练'
    model_path = Path(model_path)
    model_path.mkdir(exist_ok=True)

    learn.save(model_path/'plant_model_v1')
    print("✅ 模型已保存")

except Exception as e:
    print(f"❌ 训练失败: {e}")
    print("可能原因：数据太少或GPU不可用")

# ===== 7️⃣ 评估结果 =====
print("📈 评估训练结果...")
try:
    # 获取最佳准确率
    metrics = learn.validate()
    accuracy = metrics[1]
    print(f"🎯 模型准确率: {accuracy:.2%}")

    # 保存训练记录
    with open('D:/植物识别项目/04_模型训练/训练记录.txt', 'w') as f:
        f.write(f"训练日期: 2026-07-28\n")
        f.write(f"植物种类: {len(dls.vocab)}\")
        f.write(f"准确率: {accuracy:.2%}\n")
        f.write(f"模型: ResNet34\n")
        f.write(f"训练轮数: 5\n")

except Exception as e:
    print(f"评估出错: {e}")

# ===== 8️⃣ 测试预测 =====
print("🧪 测试单个图片预测...")
def predict_plant(img_path):
    """预测植物种类"""
    try:
        pred, pred_idx, prob = learn.predict(img_path)
        confidence = prob[pred_idx]
        print(f"🌱 预测结果: {pred}")
        print(f"📊 置信度: {confidence:.2%}")
        return pred, confidence
    except Exception as e:
        print(f"❌ 预测失败: {e}")
        return None, None

# ===== 9️⃣ 创建简单界面 =====
print("🖥️ 创建简单测试界面...")
try:
    from tkinter import Tk, filedialog, Label, Button, Frame
    from PIL import Image, ImageTk
    import tkinter as tk

    class PlantIdentifier:
        def __init__(self, master):
            self.master = master
            master.title("🌱 植物识别小工具")
            master.geometry("400x300")

            # 标题
            Label(master, text="植物识别AI", font=("Arial", 16)).pack(pady=10)

            #上传按钮
            Button(master, text="📷 选择图片", command=self.upload_image,
                   bg="green", fg="white", font=("Arial", 12)).pack(pady=20)

            # 结果显示
            self.result_label = Label(master, text="等待上传图片...",
                                     font=("Arial", 12))
            self.result_label.pack(pady=10)

            self.confidence_label = Label(master, text="",
                                         font=("Arial", 10))
            self.confidence_label.pack(pady=5)

        def upload_image(self):
            file_path = filedialog.askopenfilename(
                filetypes=[("图片文件", "*.jpg *.png *.jpeg")]
            )

            if file_path:
                try:
                    # 预测
                    plant, confidence = predict_plant(file_path)

                    if plant:
                        self.result_label.config(
                            text=f"🌺 这是：{plant}"
                        )
                        self.confidence_label.config(
                            text=f"📊 置信度：{confidence:.2%}"
                        )
                    else:
                        self.result_label.config(
                            text="❌ 识别失败"
                        )
                except Exception as e:
                    self.result_label.config(text=f"❌ 错误: {e}")

    # 运行界面
    root = Tk()
    app = PlantIdentifier(root)
    root.mainloop()

    print("✅ 测试界面已启动")

except ImportError:
    print("⚠️ tkinter不可用，跳过图形界面")
    print("可以在命令行使用 predict_plant() 函数")

except Exception as e:
    print(f"界面创建失败: {e}")

# ===== 10️⃣ 完成 =====
print("\n🎊 恭喜！你的第一个植物识别模型完成了！")
print("\n📋 接下来可以：")
print("1. 用GUI界面测试新图片")
print("2. 尝试更多植物种类")
print("3. 优化模型准确率")
print("4. 识别错误分析")

# ===== 备用：如果遇到问题 =====
if False:  # 把这里改成 True 来跳过训练，使用示例数据
    print("\n🔧 调试模式：创建示例数据")
    # 创建虚拟文件夹和图片用于测试代码结构
```

## 🚀 快速运行指南

### 方法1：直接运行
```bash
# 复制上面的代码到文件
# 保存为: D:\植物识别项目\03_代码开发\train_plants.py

# 运行（需要先安装fastai）
python D:\植物识别项目\03_代码开发\train_plants.py
```

### 方法2：Jupyter Notebook（推荐新手）
```python
# 分步运行，更容易理解
# 1️⃣ 先运行数据加载部分
# 2️⃣ 再运行模型创建
# 3️⃣ 最后运行训练
```

## 📊 预期输出示例

```
🔍 检查环境...
✅ PyTorch 版本: 2.0.0

📊 加载数据...
✅ 数据加载成功！
📁 发现的植物类别: 10
🌱 植物种类: ['玫瑰', '向日葵', '百合', '菊花', '兰花', '仙人掌', '竹子', '枫树', '松树', '荷花']

🏃 开始训练...这需要几分钟时间
epoch 0: loss 2.30, accuracy 0.10 (训练中...)
epoch 1: loss 1.80, accuracy 0.35
epoch 2: loss 1.20, accuracy 0.65
epoch 3: loss 0.80, accuracy 0.78
epoch 4: loss 0.60, accuracy 0.85

🎉 训练完成！
🎯 模型准确率: 85.00%

🌱 预测结果: 玫瑰
📊 置信度: 92.50%

🎊 恭喜！你的第一个植物识别模型完成了！
```

## 🔧 常见问题解决

### 问题1：找不到数据
```
错误: 数据文件夹不存在
解决: 确保在 D:/植物识别项目/02_数据集/10植物测试集
      创建了10个植物文件夹，每个包含图片
```

### 问题2：训练失败
```
错误: CUDA out of memory
解决: 1. 减少图片数量
      2. 使用更小模型（resnet18)
      3. 降低batch_size
```

### 问题3：准确率太低
```
解决方法:
- 增加图片数量（每种30+张）
- 确保图片清晰度高
- 检查标注是否正确
- 增加训练轮数
```

## 🎯 优化建议

### 如果准确率 > 80% 🌟
- 恭喜！模型训练成功
- 可以尝试更多植物种类
- 测试真实场景图片

### 如果准确率 < 60% ⚠️
- 检查图片质量
- 增加数据量
- 调整训练参数
- 考虑数据增强

## 💡 下一步计划

1. **今天完成** ✅
   - 训练10种植物模型
   - 达到80%+准确率

2. **明天计划** 🎯
   - 添加10种新植物
   - 优化到90%准确率
   - 制作手机版

3. **本周目标** 🏆
   - 识别50种植物
   - 网页版上线
   - 分享给朋友使用

---

**🌟 开始训练吧！有任何问题随时问我！** 🚀
```

