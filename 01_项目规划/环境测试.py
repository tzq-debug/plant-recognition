# 🔍 环境测试脚本
print("🧪 开始测试AI植物识别环境...")
print("=" * 50)

import sys
print(f"Python版本: {sys.version}")
print()

# 测试PyTorch
try:
    import torch
    print(f"✅ PyTorch: {torch.__version__}")
    if torch.cuda.is_available():
        print(f"🔥 GPU可用: {torch.cuda.get_device_name(0)}")
    else:
        print("💡 使用CPU模式（速度较慢，但完全可用）")
except ImportError:
    print("❌ PyTorch未安装 - 运行: pip install torch torchvision")
    exit()

# 测试FastAI
try:
    from fastai.vision.all import *
    print("✅ FastAI: 可用")
except ImportError:
    print("❌ FastAI未安装 - 运行: pip install fastai")
    exit()

# 测试其他库
libs = {
    'pandas': '数据处理',
    'numpy': '数值计算',
    'matplotlib': '图表显示',
    'PIL': '图片处理',
    'sklearn': '机器学习'
}

for lib, desc in libs.items():
    try:
        globals()[f"import_{lib}"] = __import__(lib if lib != 'PIL' else 'Pillow')
        print(f"✅ {lib}: {desc}功能可用")
    except ImportError:
        print(f"⚠️ {lib}: 可选库，不影响主要功能")

print("=" * 50)

# 测试核心功能
print("🎯 测试核心AI功能...")

# 1. 测试图片处理
try:
    # 创建测试图片路径
    from pathlib import Path
    test_path = Path('D:/植物识别项目/02_数据集/10植物测试集')

    if test_path.exists():
        print("✅ 数据文件夹存在")
        # 统计文件夹数量
        folders = [f for f in test_path.iterdir() if f.is_dir()]
        print(f"📁 发现 {len(folders)} 个植物文件夹")
        if len(folders) > 0:
            print("🌱 植物种类:", [f.name for f in folders][:5], "...")
        else:
            print("⚠️ 需要先创建植物文件夹并添加图片")
    else:
        print("⚠️ 数据文件夹尚未创建")
        print("📋 请先创建: D:/植物识别项目/02_数据集/10植物测试集")

except Exception as e:
    print(f"⚠️ 数据检查出错: {e}")

print("=" * 50)
print("🎊 环境测试完成！")
print()
print("🚀 如果看到多个✅，说明环境配置成功！")
print("🌱 下一步：收集植物图片，开始训练模型")
print("💡 提示：每种植物需要20-30张清晰图片")
print()
print("📞 需要帮助？告诉我测试结果！")
```

