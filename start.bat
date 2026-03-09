@echo off
chcp 65001 > nul
title مجمّع الأخبار العالمي

echo.
echo  ========================================
echo   مجمّع الأخبار العالمي - جاري التشغيل
echo  ========================================
echo.

:: التحقق من وجود Python
python --version > nul 2>&1
if errorlevel 1 (
    echo [خطأ] Python غير مثبّت!
    echo يرجى تحميله من: https://www.python.org/downloads/
    echo تأكد من تفعيل خيار "Add Python to PATH" أثناء التثبيت
    pause
    exit /b 1
)

:: الانتقال لمجلد البرنامج
cd /d "%~dp0"

:: التحقق من المكتبات وتثبيتها إن لزم
echo [1/3] التحقق من المكتبات...
pip show flask > nul 2>&1
if errorlevel 1 (
    echo [2/3] تثبيت المكتبات المطلوبة...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo [خطأ] فشل تثبيت المكتبات!
        pause
        exit /b 1
    )
) else (
    echo [2/3] المكتبات موجودة.
)

echo [3/3] تشغيل الخادم...
echo.
echo  سيفتح المتصفح تلقائياً...
echo  للوصول من iPhone: افتح المتصفح واكتب العنوان المعروض
echo.
echo  لإيقاف البرنامج: اضغط Ctrl+C
echo  ========================================
echo.

:: فتح المتصفح بعد ثانيتين
start /b cmd /c "timeout /t 3 > nul && start http://localhost:5000"

:: تشغيل الخادم
python app.py

pause
