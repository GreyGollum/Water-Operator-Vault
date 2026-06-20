@echo off
setlocal

REM Water Operator Vault - Local Printable Packet Builder
REM Run this from anywhere. It will build DOCX/PDF artifacts into:
REM 08 Printable Study Materials\Build Artifacts

cd /d "%~dp0.."

echo.
echo ===============================================
echo Water Operator Vault - Build Printable Packets
echo ===============================================
echo.

where python >nul 2>nul
if errorlevel 1 (
  echo ERROR: Python was not found on PATH.
  echo Install Python 3.12+ or use the Python launcher.
  pause
  exit /b 1
)

echo Installing/updating Python DOCX dependency...
python -m pip install python-docx
if errorlevel 1 (
  echo ERROR: Could not install python-docx.
  pause
  exit /b 1
)

echo.
echo Building printable packets locally...
python tools\run_printable_packet_build.py --local
if errorlevel 1 (
  echo.
  echo ERROR: Printable packet build failed.
  pause
  exit /b 1
)

echo.
echo Done. Output folder:
echo 08 Printable Study Materials\Build Artifacts
echo.
pause
