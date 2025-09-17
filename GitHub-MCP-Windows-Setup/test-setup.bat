@echo off
echo Testing GitHub MCP Setup
echo ========================

REM Check if Cursor config exists
set "CURSOR_CONFIG=%APPDATA%\Cursor\User\mcp.json"
if not exist "%CURSOR_CONFIG%" (
    echo ❌ MCP configuration not found at: %CURSOR_CONFIG%
    echo Please run one of the setup scripts first
    pause
    exit /b 1
)

echo ✅ MCP configuration found

REM Check JSON syntax
echo Checking JSON syntax...
powershell -Command "try { Get-Content '%CURSOR_CONFIG%' | ConvertFrom-Json | Out-Null; Write-Host '✅ JSON syntax is valid' } catch { Write-Host '❌ Invalid JSON syntax' }"

echo.
echo Configuration file contents:
echo ============================
type "%CURSOR_CONFIG%"

echo.
echo Test prompts to try in Cursor:
echo ===============================
echo 1. "List my repositories"
echo 2. "Show me recent pull requests in [your-repo]"
echo 3. "What are the latest issues in [your-repo]?"
echo 4. "Show the last 3 workflow runs for [your-repo]"
echo.
echo If you encounter issues:
echo - Restart Cursor completely
echo - Check your GitHub Personal Access Token permissions
echo - Verify the token is not expired
echo - Check the troubleshooting section in the setup guide

echo.
pause
