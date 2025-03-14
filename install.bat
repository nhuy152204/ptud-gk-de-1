@echo off
echo ===========================
echo 🚀 Đang cài đặt môi trường Flask...
echo ===========================

cd /d %~dp0  REM Chuyển đến thư mục của script

REM Tạo môi trường ảo nếu chưa tồn tại
if not exist venv (
    python -m venv venv
)

REM Kích hoạt môi trường ảo (chỉ hoạt động trong cmd, không dùng cho PowerShell)
call venv\Scripts\activate.bat

REM Cài đặt thư viện nếu `requirements.txt` tồn tại
if exist requirements.txt (
    echo ===========================
    echo 📦 Đang cài đặt thư viện...
    echo ===========================
    pip install --no-cache-dir -r requirements.txt
) else (
    echo Lỗi: Không tìm thấy file requirements.txt!
    exit /b
)

echo ===========================
echo ✅ Cài đặt hoàn tất!
echo ===========================
pause
