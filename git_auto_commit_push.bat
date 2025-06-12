@echo off
:: 取得目前日期與時間
for /f "tokens=2 delims==" %%I in ('"wmic os get localdatetime /value"') do set datetime=%%I

:: 格式化成 yyyy-MM-dd HH:mm:ss
set year=%datetime:~0,4%
set month=%datetime:~4,2%
set day=%datetime:~6,2%
set hour=%datetime:~8,2%
set minute=%datetime:~10,2%
set second=%datetime:~12,2%
set commitmsg=%year%-%month%-%day% %hour%:%minute%:%second%

:: 執行 git 操作
echo Commit message: %commitmsg%
git add .
git commit -m "%commitmsg%"
git push
pause
