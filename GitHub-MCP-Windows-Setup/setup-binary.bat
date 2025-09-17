@echo off
echo Setting up GitHub MCP for Cursor (Binary Server)
echo ================================================

REM Check if the binary exists
set "BINARY_PATH=C:\Program Files\GitHub\github-mcp-server.exe"
if not exist "%BINARY_PATH%" (
    echo ❌ GitHub MCP Server binary not found at: %BINARY_PATH%
    echo.
    echo Please download the binary first:
    echo 1. Go to: https://github.com/github/github-mcp-server/releases
    echo 2. Download the Windows binary
    echo 3. Extract to: C:\Program Files\GitHub\
    echo 4. Run this script again
    echo.
    pause
    exit /b 1
)

echo ✅ GitHub MCP Server binary found

REM Create Cursor config directory if it doesn't exist
set "CURSOR_CONFIG=%APPDATA%\Cursor\User"
if not exist "%CURSOR_CONFIG%" (
    echo Creating Cursor config directory...
    mkdir "%CURSOR_CONFIG%"
)

REM Copy the binary server configuration
echo Copying MCP configuration...
copy "mcp-binary.json" "%CURSOR_CONFIG%\mcp.json"

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
    echo Binary location: %BINARY_PATH%
    echo.
    echo Note: This setup runs the MCP server as a local binary
) else (
    echo.
    echo ❌ Error copying configuration file
    echo Please check that mcp-binary.json exists in this directory
)

echo.
pause
