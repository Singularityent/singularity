@echo off
echo Setting up GitHub MCP for Cursor (Remote Server)
echo ================================================

REM Create Cursor config directory if it doesn't exist
set "CURSOR_CONFIG=%APPDATA%\Cursor\User"
if not exist "%CURSOR_CONFIG%" (
    echo Creating Cursor config directory...
    mkdir "%CURSOR_CONFIG%"
)

REM Copy the remote server configuration
echo Copying MCP configuration...
copy "mcp.json" "%CURSOR_CONFIG%\mcp.json"

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ✅ Configuration copied successfully!
    echo.
    echo Next steps:
    echo 1. Restart Cursor
    echo 2. You'll be prompted for your GitHub Personal Access Token
    echo 3. Try the test prompts from the setup guide
    echo.
    echo Configuration location: %CURSOR_CONFIG%\mcp.json
) else (
    echo.
    echo ❌ Error copying configuration file
    echo Please check that mcp.json exists in this directory
)

echo.
pause
