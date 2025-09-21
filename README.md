# Singularity Documentation Search Server

A Model Context Protocol (MCP) server that provides intelligent documentation search capabilities across multiple popular Python libraries and frameworks.

## Features

- 🔍 **Multi-Library Search**: Search across documentation for popular libraries including:
  - LangChain
  - LlamaIndex  
  - OpenAI
  - Anthropic
  - FastAPI
  - Django
  - Flask
  - PyTorch
  - TensorFlow

- 🛡️ **Security**: Uses environment variables for API keys (no hardcoded secrets)
- 📝 **Comprehensive Logging**: Detailed logging for debugging and monitoring
- 🚀 **Error Handling**: Robust error handling with graceful fallbacks
- 🎯 **Content Optimization**: Intelligent text extraction and content limiting

## Installation

1. Install required dependencies:
```bash
pip install fastmcp python-dotenv httpx beautifulsoup4
```

2. Set up your environment variables:
```bash
# Create a .env file
SERPER_API_KEY=your_serper_api_key_here
```

3. Run the server:
```bash
python main.py
```

## Usage

The server provides two main tools:

### get_docs(query, library)
Search documentation for a specific library:
```python
# Example: Search for authentication in FastAPI docs
get_docs("authentication", "fastapi")

# Example: Search for vector stores in LangChain docs  
get_docs("vector stores", "langchain")
```

### list_supported_libraries()
Get a list of all supported documentation libraries and their URLs.

## API Integration

This server uses the [Serper API](https://serper.dev) for web search capabilities. You'll need to:

1. Sign up for a Serper API account
2. Get your API key
3. Add it to your `.env` file as `SERPER_API_KEY`

## Recent Improvements

- ✅ Removed hardcoded API keys for better security
- ✅ Added comprehensive error handling and logging
- ✅ Expanded support to 9 documentation libraries
- ✅ Improved content extraction and formatting
- ✅ Added proper HTTP headers and rate limiting
- ✅ Limited response sizes to prevent overwhelming outputs

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is part of the Singularityent organization.
