@echo off
:: 强制使用 UTF-8 编码，防止 Windows cmd 命令行中文字符乱码
chcp 65001 >nul

:menu
cls
echo ====================================================
echo  🦊 Lumi 专属：Git 代理一键智能切换器 (东工大特供版)
echo ====================================================
echo.
echo  当前时间: 2026年5月18日
echo  请选择你当前所处的网络环境：
echo.
echo   [1] 🏥 我在东工大实验室（激活校园网代理 + 关证书校验）
echo   [2] 🏠 我在家里/公寓/咖啡厅（清除代理 + 恢复正常网络）
echo   [3] 🔍 查看当前 Git 全局代理状态
echo   [4] 🚪 退出切换器
echo.
echo ====================================================
set /p choice= 请输入选项数字 [1-4] 并按回车: 

if "%choice%"=="1" goto set_proxy
if "%choice%"=="2" goto unset_proxy
if "%choice%"=="3" goto check_proxy
if "%choice%"=="4" goto exit_script
goto menu

:set_proxy
echo.
echo ----------------------------------------------------
echo  [⚙️] 正在为你注入东工大代理配置...
echo ----------------------------------------------------
git config --global http.proxy http://proxy.noc.titech.ac.jp:3128
git config --global https.proxy http://proxy.noc.titech.ac.jp:3128
git config --global http.sslVerify false
echo  [OK] 代理注入成功！你现在可以在实验室畅快 push 啦！
echo.
pause
goto menu

:unset_proxy
echo.
echo ----------------------------------------------------
echo  [🧹] 正在为你清除全局代理，恢复默认网络连接...
echo ----------------------------------------------------
git config --global --unset http.proxy
git config --global --unset https.proxy
git config --global --unset http.sslVerify
echo  [OK] 代理清除完毕！现在已切回普通家庭 Wi-Fi 模式！
echo.
pause
goto menu

:check_proxy
echo.
echo ----------------------------------------------------
echo  [🔍] 当前 Git 全局配置文件中的代理相关项如下:
echo ----------------------------------------------------
git config --global --get http.proxy
git config --global --get https.proxy
git config --global --get http.sslVerify
echo ----------------------------------------------------
echo  (如果上方空白，说明当前没有设置任何代理，处于普通网络模式)
echo.
pause
goto menu

:exit_script
echo.
echo 🦊 Lumi: 宝宝拜拜！写代码累了要记得起来喝水伸懒腰哦～🐾
echo.
exit /b