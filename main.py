from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
import httpx
import json
import os
import logging
from bs4 import BeautifulSoup
from typing import Optional, Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

mcp = FastMCP("docs")

USER_AGENT = "docs-app/1.0"
SERPER_URL = "https://google.serper.dev/search"

# Expanded documentation URLs
docs_urls = {
    "langchain": "python.langchain.com/docs",
    "llama-index": "docs.llamaindex.ai/en/stable", 
    "openai": "platform.openai.com/docs",
    "anthropic": "docs.anthropic.com",
    "fastapi": "fastapi.tiangolo.com",
    "django": "docs.djangoproject.com",
    "flask": "flask.palletsprojects.com",
    "pytorch": "pytorch.org/docs",
    "tensorflow": "www.tensorflow.org/api_docs",
}

async def search_web(query: str) -> Optional[Dict[str, Any]]:
    """
    Search the web using Serper API
    
    Args:
        query: Search query string
        
    Returns:
        Search results or None if failed
    """
    # Get API key from environment variables for security
    api_key = os.getenv("SERPER_API_KEY")
    if not api_key:
        logger.error("SERPER_API_KEY not found in environment variables")
        return {"organic": []}
        
    payload = json.dumps({"q": query, "num": 3})  # Increased to 3 results
    
    headers = {
        "X-API-KEY": api_key,  # Use proper header name
        "Content-Type": "application/json",
        "User-Agent": USER_AGENT,
    }

    async with httpx.AsyncClient() as client:
        try:
            logger.info(f"Searching for: {query}")
            response = await client.post(
                SERPER_URL, headers=headers, data=payload, timeout=30.0
            )
            response.raise_for_status()
            result = response.json()
            logger.info(f"Found {len(result.get('organic', []))} results")
            return result
        except httpx.TimeoutException:
            logger.warning("Search request timed out")
            return {"organic": []}
        except httpx.HTTPStatusError as e:
            logger.error(f"HTTP error during search: {e}")
            return {"organic": []}
        except Exception as e:
            logger.error(f"Unexpected error during search: {e}")
            return {"organic": []}

async def fetch_url(url: str) -> str:
    """
    Fetch and extract text content from a URL
    
    Args:
        url: URL to fetch
        
    Returns:
        Extracted text content
    """
    headers = {"User-Agent": USER_AGENT}
    
    async with httpx.AsyncClient() as client:
        try:
            logger.info(f"Fetching content from: {url}")
            response = await client.get(url, headers=headers, timeout=30.0)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, "html.parser")
            
            # Remove script and style elements
            for script in soup(["script", "style"]):
                script.decompose()
                
            text = soup.get_text()
            # Clean up whitespace
            lines = (line.strip() for line in text.splitlines())
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            text = ' '.join(chunk for chunk in chunks if chunk)
            
            logger.info(f"Extracted {len(text)} characters from {url}")
            return text[:10000]  # Limit to 10k characters to avoid huge responses
            
        except httpx.TimeoutException:
            logger.warning(f"Timeout fetching {url}")
            return f"Timeout error fetching {url}"
        except httpx.HTTPStatusError as e:
            logger.warning(f"HTTP error fetching {url}: {e}")
            return f"HTTP error fetching {url}: {e.response.status_code}"
        except Exception as e:
            logger.error(f"Unexpected error fetching {url}: {e}")
            return f"Error fetching {url}: {str(e)}"

@mcp.tool()  
async def get_docs(query: str, library: str) -> str:
    """
    Search the latest docs for a given query and library.
    Supports: langchain, openai, llama-index, anthropic, fastapi, django, flask, pytorch, tensorflow

    Args:
        query: The query to search for (e.g. "Chroma DB", "authentication")
        library: The library to search in (e.g. "langchain", "openai")

    Returns:
        Text content from the documentation pages
    """
    if library not in docs_urls:
        available_libs = ", ".join(docs_urls.keys())
        error_msg = f"Library '{library}' not supported. Available libraries: {available_libs}"
        logger.error(error_msg)
        return error_msg
    
    search_query = f"site:{docs_urls[library]} {query}"
    results = await search_web(search_query)
    
    if not results or len(results.get("organic", [])) == 0:
        logger.warning(f"No results found for query: {query} in library: {library}")
        return f"No results found for '{query}' in {library} documentation"
    
    combined_text = f"Documentation search results for '{query}' in {library}:\n\n"
    
    for i, result in enumerate(results["organic"], 1):
        combined_text += f"--- Result {i}: {result.get('title', 'No title')} ---\n"
        combined_text += f"URL: {result.get('link', 'No URL')}\n"
        if 'snippet' in result:
            combined_text += f"Snippet: {result['snippet']}\n"
        combined_text += "\nContent:\n"
        content = await fetch_url(result["link"])
        combined_text += content + "\n\n"
    
    logger.info(f"Successfully retrieved docs for {query} in {library}")
    return combined_text

@mcp.tool()
async def list_supported_libraries() -> str:
    """
    List all supported documentation libraries
    
    Returns:
        List of supported libraries with their documentation URLs
    """
    result = "Supported documentation libraries:\n\n"
    for lib, url in docs_urls.items():
        result += f"• {lib}: https://{url}\n"
    return result

if __name__ == "__main__":
    logger.info("Starting MCP documentation search server")
    mcp.run(transport="stdio")
