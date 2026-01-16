# MCP Server

A simple Model Context Protocol (MCP) server implementation in Python.

## Overview

This is a basic MCP server that provides a "hello" tool as an example. You can extend it with your own custom tools to integrate with AI assistants like Claude Desktop.

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

### Connecting to Claude Desktop

To use this server with Claude Desktop, add the following configuration to your Claude Desktop config file:

**Mac**: `~/Library/Application Support/Claude/claude_desktop_config.json`

**Windows**: `%APPDATA%\\Claude\\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "hello-world-server": {
      "command": "python",
      "args": [
        "/path/to/your/mcp-server/server.py"
      ]
    }
  }
}
```

Replace `/path/to/your/mcp-server/` with the actual path to this repository.

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

### Claude Desktop can't connect
- Verify the path in your config file is correct
- Make sure to use the full absolute path to server.py
- Restart Claude Desktop after changing the config

## License

MIT License - feel free to use and modify as needed.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## Resources

- [MCP Documentation](https://modelcontextprotocol.io/)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Claude Desktop](https://claude.ai/desktop)
