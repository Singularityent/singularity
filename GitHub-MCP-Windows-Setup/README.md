# GitHub MCP Setup for Windows

This package contains everything you need to set up GitHub MCP (Model Context Protocol) integration with Cursor on your Windows computer.

## Quick Start

1. **Choose your setup method:**
   - **Remote Server** (Recommended): Simplest setup using GitHub's hosted service
   - **Docker Server**: Run the MCP server locally using Docker
   - **Binary Server**: Run the MCP server as a local executable

2. **Run the appropriate setup script:**
   - Double-click `setup-remote.bat` for remote server
   - Double-click `setup-docker.bat` for Docker server  
   - Double-click `setup-binary.bat` for binary server

3. **Test your setup:**
   - Run `test-setup.bat` to verify configuration
   - Restart Cursor
   - Enter your GitHub Personal Access Token when prompted

## Files Included

### Configuration Files
- `mcp.json` - Remote server configuration
- `mcp-docker.json` - Docker server configuration  
- `mcp-binary.json` - Binary server configuration

### Setup Scripts
- `setup-remote.bat` - Automated remote server setup
- `setup-docker.bat` - Automated Docker server setup
- `setup-binary.bat` - Automated binary server setup
- `test-setup.bat` - Test and validate your configuration

### Documentation
- `Windows-Setup-Guide.md` - Detailed setup instructions
- `README.md` - This file

## Prerequisites

- Windows 10/11
- Cursor IDE installed
- GitHub account with Personal Access Token
- (For Docker setup) Docker Desktop installed
- (For Binary setup) GitHub MCP Server binary downloaded

## Getting Your GitHub Token

1. Go to GitHub.com → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Click "Generate new token (classic)"
3. Select scopes: `repo`, `read:org`, `read:user`
4. Copy the token (you won't see it again!)

## Test Prompts

Once setup is complete, try these prompts in Cursor:

```
List my repositories in the organization Singularityent
Show me recent pull requests in [your-repo]
What are the latest issues in [your-repo]?
Show the last 3 workflow runs for [your-repo]
Create a new branch called 'mcp-test' in [your-repo]
```

## Troubleshooting

If you encounter issues:

1. **Run `test-setup.bat`** to check your configuration
2. **Restart Cursor completely** after setup
3. **Check your GitHub token permissions** and expiration
4. **Read the detailed guide** in `Windows-Setup-Guide.md`

## Security Notes

- Start with read-only access while testing
- Use fine-grained tokens with minimal permissions
- Rotate your tokens regularly
- The configurations include read-only and limited toolset settings for security

## Support

For more information, see:
- [GitHub MCP Server Documentation](https://github.com/github/github-mcp-server)
- [Cursor MCP Documentation](https://cursor.sh/docs/mcp)
