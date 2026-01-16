# MCP Server

A simple Model Context Protocol (MCP) server implementation in Python.

## Overview

This is a basic MCP server that provides a "hello" tool as an example. You can extend it with your own custom tools to integrate with AI assistants like Perplexity/Comet, ChatGPT, and other AI assistants

## Features

- ✅ Simple "hello" greeting tool
- ✅ Built with the official MCP Python SDK
- ✅ Easy to extend with custom tools
- ✅ Ready for deployment

## Installation

1. Clone this repository:
```bash
git clone https://github.com/dbrooks61785/mcp-server.git
cd mcp-server
```

2. Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Mac/Linux
# or
venv\\Scripts\\activate  # On Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Running the Server

Run the server directly:
```bash
python server.py
```

### Connecting to AI Assistants (Perplexity/Comet & ChatGPT)


This MCP server can be deployed and connected to AI assistants that support the Model Context Protocol.

#### For ChatGPT with MCP Support

ChatGPT is adding MCP support. Once available, you'll be able to:
1. Deploy this server to a hosting platform (Replit, Railway, etc.)
2. Get the server URL
3. Connect it in ChatGPT's MCP settings

#### For Perplexity/Comet

Perplexity's Comet browser assistant supports MCP servers:
1. Deploy your server to a public URL or run it locally
2. Configure Comet to connect to your MCP server endpoint
3. Your custom tools will be available in Comet conversations

#### Local Development

For local development and testing:
```bash
python server.py
```

The server runs on stdio and can be tested with any MCP-compatible client.

## Available Tools

### hello
A simple greeting tool that welcomes a person by name.

**Parameters:**
- `name` (string, required): Name of the person to greet

**Example:**
```json
{
  "name": "Alice"
}
```

**Response:**
```
Hello, Alice! Welcome to the MCP server.
```

## Adding Your Own Tools

To add custom tools, edit `server.py`:

1. Add a new tool to the `list_tools()` function
2. Implement the tool logic in the `call_tool()` function
3. Restart the server

## Project Structure

```
mcp-server/
├── server.py          # Main MCP server implementation
├── requirements.txt   # Python dependencies
├── .gitignore        # Git ignore rules
└── README.md         # This file
```

## Requirements

- Python 3.10 or higher
- MCP SDK (mcp >= 0.9.0)

## Troubleshooting

### Server won't start
- Make sure you've activated the virtual environment
- Verify all dependencies are installed: `pip install -r requirements.txt`
- Check Python version: `python --version` (should be 3.10+)

### AI Assistant can't connect
- Verify the server URL is accessible
- Check that the server is running
- Ensure your AI assistant supports MCP protocol

## License

MIT License - feel free to use and modify as needed.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## Resources

- [MCP Documentation](https://modelcontextprotocol.io/)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Perplexity](https://www.perplexity.ai/)
