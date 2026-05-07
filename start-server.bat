@echo off
title liminal - newest-serve :8080
cd /d "%~dp0"
echo ================================================
echo  liminal (static HTML) =^> http://localhost:8080
echo  Auto-serves highest liminal_N.html at /
echo  Bound to 0.0.0.0 - reachable via LAN / Tailscale
echo ================================================
echo.
python serve-newest.py 8080
echo.
echo Server stopped. Press any key to close.
pause >nul
