@echo off
echo ====================================================
echo  🦊 Lumi 专属：东工大代理一键修复与重置脚本
echo ====================================================
echo.

echo 1. 正在彻底清除之前错误的代理配置（包括那些讨厌的中括号）...
git config --global --unset http.proxy
git config --global --unset https.proxy
echo 清理完成！
echo.

echo 2. 正在重新注入最干净的东工大代理（不带任何排版格式）...
git config --global http.proxy http://proxy.noc.titech.ac.jp:3128
git config --global https.proxy http://proxy.noc.titech.ac.jp:3128
git config --global http.sslVerify false
echo 注入完成！
echo.

echo 3. 正在为你检查当前的全局 Git 配置：
echo ----------------------------------------------------
git config --global --list
echo ----------------------------------------------------
echo.

echo [OK] 修复全部搞定啦！宝宝，现在直接输入: git push