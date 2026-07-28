@echo off
echo 🔧 开始安装植物识别AI环境...
echo.

echo 1️⃣ 检查Python版本...
python --version
if errorlevel 1 (
    echo ❌ 未找到Python，请先安装Python 3.8+
    echo 访问：https://python.org/downloads
    pause
    exit
)
echo ✅ Python已安装
echo.

echo 2️⃣ 创建专用环境...
conda create -name plant_recognition python=3.8 -y
if errorlevel 1 (
    echo ⚠️ conda不可用，尝试使用Python虚拟环境...
    python -m venv plant_recognition
    if errorlevel 1 (
        echo ❌ 无法创建虚拟环境
        pause
        exit
    )
    echo ✅ 虚拟环境创建成功
    goto activate_venv
)
echo ✅ Conda环境创建成功
goto activate_conda

:activate_conda
echo 3️⃣ 激活Conda环境...
call conda activate plant_recognition
goto install_libs

:activate_venv
echo 3️⃣ 激活虚拟环境...
call plant_recognition\Scripts\activate
goto install_libs

:install_libs
echo 4️⃣ 安装PyTorch...
echo 这可能需要几分钟，请耐心等待...
pip install torch torchvision
echo ✅ PyTorch安装完成
echo.

echo 5️⃣ 安装FastAI...
pip install fastai
echo ✅ FastAI安装完成
echo.

echo 6️⃣ 安装辅助库...
pip install pandas numpy matplotlib pillow scikit-learn
echo ✅ 所有库安装完成
echo.

echo 7️⃣ 测试安装...
python -c "import torch; print('✅ PyTorch:', torch.__version__)"
python -c "from fastai.vision.all import *; print('✅ FastAI: 可用')"
python -c "import pandas; print('✅ Pandas: 可用')"
echo.

echo 🎉 环境配置完成！
echo.
echo 🚀 使用方法：
echo   Conda用户输入：conda activate plant_recognition
echo   Venv用户输入：plant_recognition\Scripts\activate
echo.
echo 🌱 然后运行训练脚本：
echo   python D:\植物识别项目\03_代码开发\完整训练脚本.py
echo.
echo 📊 接下来收集10种植物图片到：
echo   D:\植物识别项目\02_数据集\10植物测试集
echo.
echo 💡 遇到问题？随时询问！
echo.

pause
```

