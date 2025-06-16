@echo off
setlocal EnableDelayedExpansion

:: 使用 WMIC 取得今天日期，格式為 yyyyMMdd
for /f %%a in ('wmic os get LocalDateTime ^| find "."') do set datetime=%%a
set mm=%datetime:~4,2%
set dd=%datetime:~6,2%
set folder=%mm%%dd%

:: 建立資料夾結構
mkdir %folder%\easy
mkdir %folder%\medium
mkdir %folder%\hard

:: 建立 .gitkeep 檔案
echo.>%folder%\easy\.gitkeep
echo.>%folder%\medium\.gitkeep
echo.>%folder%\hard\.gitkeep

echo Created folder structure for %folder%
pause
