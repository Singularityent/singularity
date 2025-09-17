# GitHub MCP Setup for Windows Cursor

This guide will help you set up GitHub MCP (Model Context Protocol) integration with Cursor on your Windows computer.

## Prerequisites

- Windows 10/11
- Cursor IDE installed
- GitHub account
- (Optional) Docker Desktop for local server setup

## Setup Options

### Option 1: Remote Server (Recommended - Simplest)

This uses GitHub's hosted MCP server and is the easiest to set up.

#### Steps:

1. **Create GitHub Personal Access Token**
   - Go to GitHub.com → Settings → Developer settings → Personal access tokens → Tokens (classic)
   - Click "Generate new token (classic)"
   - Select scopes: `repo`, `read:org`, `read:user`
   - Copy the token (you won't see it again!)

2. **Configure Cursor**
   - Open File Explorer and navigate to: `%APPDATA%\Cursor\User`
   - Create the file `mcp.json` (if it doesn't exist)
   - Copy the contents from `mcp.json` in this folder
   - Restart Cursor

3. **Test the Setup**
   - Open Cursor
   - You'll be prompted for your GitHub token
   - Try these test prompts:
     - "List my repositories"
     - "Show me recent pull requests in [your-repo]"
     - "What are the latest issues in [your-repo]?"

### Option 2: Local Docker Server

If you prefer running the MCP server locally using Docker.

#### Steps:

1. **Install Docker Desktop**
   - Download from [docker.com](https://www.docker.com/products/docker-desktop/)
   - Install and start Docker Desktop

2. **Configure Cursor**
   - Use the `mcp-docker.json` configuration
   - Copy it to `%APPDATA%\Cursor\User\mcp.json`
   - Restart Cursor

3. **Test the Setup**
   - Same test prompts as Option 1

### Option 3: Local Binary Server

For advanced users who want to run the MCP server as a local binary.

#### Steps:

1. **Download GitHub MCP Server Binary**
   - Go to [GitHub MCP Server releases](https://github.com/github/github-mcp-server/releases)
   - Download the Windows binary
   - Extract to `C:\Program Files\GitHub\`

2. **Configure Cursor**
   - Use the `mcp-binary.json` configuration
   - Copy it to `%APPDATA%\Cursor\User\mcp.json`
   - Restart Cursor

## Configuration Details

### Environment Variables

You can customize the MCP server behavior by adding these environment variables:

- `GITHUB_READ_ONLY`: Set to "1" for read-only access
- `GITHUB_TOOLSETS`: Limit available tools (e.g., "repos,issues,pull_requests,actions")
- `GITHUB_HOST`: For GitHub Enterprise Server (e.g., "https://your-ghes-domain")

### Security Best Practices

1. **Use Fine-Grained Tokens**: Create tokens with minimal required permissions
2. **Read-Only First**: Start with read-only access while testing
3. **Scope Limitation**: Limit toolsets to only what you need
4. **Regular Rotation**: Rotate your tokens regularly

## Troubleshooting

### Common Issues

1. **Cursor can't see the server**
   - Verify the JSON file is in the correct location: `%APPDATA%\Cursor\User\mcp.json`
   - Check JSON syntax is valid
   - Restart Cursor completely

2. **Authentication errors**
   - Verify your PAT has the correct permissions
   - Ensure the token is scoped to the target repository/organization
   - Check if the token has expired

3. **Docker issues**
   - Ensure Docker Desktop is running
   - Check if the GitHub MCP server image can be pulled
   - Verify proxy settings if behind corporate firewall

4. **Corporate proxy**
   - For Docker: Inherit proxy environment variables
   - For remote HTTP: Ensure the GitHub API URL isn't blocked

### Testing Commands

Try these prompts in Cursor to verify everything is working:

```
List my repositories in the organization Singularityent
Show me the last 3 workflow runs for [repository-name]
Create a new branch called 'mcp-test' in [repository-name]
Show recent pull requests in [repository-name]
```

## File Locations

- **Cursor MCP Config**: `%APPDATA%\Cursor\User\mcp.json`
- **Alternative location**: `%USERPROFILE%\.cursor\mcp.json`

## Next Steps

Once setup is complete, you can:
- Browse repositories and issues
- Create and manage pull requests
- Monitor GitHub Actions workflows
- Search code and commits
- Manage repository settings

For more advanced usage, refer to the [GitHub MCP Server documentation](https://github.com/github/github-mcp-server).
