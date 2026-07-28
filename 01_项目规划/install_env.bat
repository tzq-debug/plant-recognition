@echo off
chcp 65001 >nul
echo.
echo Installing Plant Recognition AI Environment...
echo.

echo Step 1: Checking Python...
python --version
if errorlevel 1 (
    echo ERROR: Python not found. Please install Python 3.8+ first
    echo Visit: https://python.org/downloads
    pause
    exit
)
echo SUCCESS: Python is installed
echo.

echo Step 2: Creating conda environment...
conda create -n plant_recognition python=3.8 -y
if errorlevel 1 (
    echo WARNING: conda not available, trying virtual environment...
    python -m venv plant_recognition
    if errorlevel 1 (
        echo ERROR: Cannot create virtual environment
        pause
        exit
    )
    echo SUCCESS: Virtual environment created
    goto activate_venv
)
echo SUCCESS: Conda environment created
goto activate_conda

:activate_conda
echo Step 3: Activating conda environment...
call conda activate plant_recognition
goto install

:activate_venv
echo Step 3: Activating virtual environment...
call plant_recognition\Scripts\activate
goto install

:install
echo Step 4: Installing PyTorch (this takes several minutes)...
pip install torch torchvision
echo SUCCESS: PyTorch installed
echo.

echo Step 5: Installing FastAI...
pip install fastai
echo SUCCESS: FastAI installed
echo.

echo Step 6: Installing additional libraries...
pip install pandas numpy matplotlib pillow scikit-learn
echo SUCCESS: All libraries installed
echo.

echo Step 7: Testing installation...
python -c "import torch; print('SUCCESS: PyTorch', torch.__version__)"
python -c "from fastai.vision.all import *; print('SUCCESS: FastAI available')"
echo.

echo ========================================
echo INSTALLATION COMPLETE!
echo.
echo How to use:
echo - If using conda: conda activate plant_recognition
echo - If using venv: plant_recognition\Scripts\activate
echo.
echo Then run:
echo python D:\植物识别项目\03_代码开发\complete_training_script.py
echo.
echo Next: Create folders for plant images in:
echo D:\植物识别项目\02_数据集\10植物测试集
echo ========================================
echo.
pause
```

