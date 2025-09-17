@echo off
echo Setting up GitHub MCP for Cursor (Docker Server)
echo ================================================

REM Check if Docker is running
echo Checking Docker status...
docker version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo ❌ Docker is not running or not installed
    echo Please install Docker Desktop and start it, then run this script again
    echo Download from: https://www.docker.com/products/docker-desktop/
    pause
    exit /b 1
)

echo ✅ Docker is running

REM Create Cursor config directory if it doesn't exist
set "CURSOR_CONFIG=%APPDATA%\Cursor\User"
if not exist "%CURSOR_CONFIG%" (
    echo Creating Cursor config directory...
    mkdir "%CURSOR_CONFIG%"
)

REM Copy the Docker server configuration
echo Copying MCP configuration...
copy "mcp-docker.json" "%CURSOR_CONFIG%\mcp.json"

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
    echo.
    echo Note: This setup uses Docker to run the MCP server locally
) else (
    echo.
    echo ❌ Error copying configuration file
    echo Please check that mcp-docker.json exists in this directory
)

echo.
pause
