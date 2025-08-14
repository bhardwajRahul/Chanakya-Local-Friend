# Configuration

Chanakya is configured using two main files: `.env` for environment variables and `mcp_config_file.json` for tool configuration.

## Environment Variables (`.env`)

Create a `.env` file in the root of the project (you can copy `.env.example`). This file contains the core configuration for Chanakya.

| Variable                    | Description                                                                                         | Example                                                      |
| --------------------------- | --------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| `OLLAMA_ENDPOINT`           | The URL of your main Ollama LLM endpoint.                                                           | `http://localhost:11434`                                     |
| `OLLAMA_MODEL_NAME`         | The name of the Ollama model to use for the main agent.                                             | `hf.co/unsloth/Qwen3-Coder-30B-A3B-Instruct-GGUF:UD-Q4_K_XL` |
| `OLLAMA_NUM_CTX`            | The context window size for the main LLM.                                                           | `18000`                                                      |
| `OLLAMA_ENDPOINT_SMALL`     | The URL of your secondary Ollama LLM endpoint (can be the same as the main one).                    | `http://localhost:11434`                                     |
| `OLLAMA_MODEL_NAME_SMALL`   | The name of the Ollama model to use for query refinement.                                           | `hf.co/unsloth/Qwen3-Coder-30B-A3B-Instruct-GGUF:UD-Q4_K_XL` |
| `OLLAMA_NUM_CTX_SMALL`      | The context window size for the small LLM.                                                          | `8000`                                                       |
| `STT_SERVER_URL`            | The URL of your Speech-to-Text (STT) server.                                                        | `http://localhost:8000/v1/audio/transcriptions`              |
| `TTS_ENGINE`                | The Text-to-Speech (TTS) engine to use. Can be`coqui` or `piper`.                                   | `coqui`                                                      |
| `TTS_SERVER_URL`            | The URL of your Text-to-Speech (TTS) server.                                                        | `http://localhost:5002/api/tts`                              |
| `DATABASE_PATH`             | The path to the SQLite database file for long-term memory.                                          | `database/long_term_memory.db`                               |
| `WAKE_WORD`                 | The wake word for the voice assistant. Defaults to "Chanakya".                                      | `Chanakya`                                                   |
| `APP_SECRET_KEY`            | A secret key for the Flask application. If not provided, a new one will be generated on each start. | `a_very_secret_key`                                          |
| `CLIENT_INACTIVE_THRESHOLD` | The time in seconds after which an inactive client is removed from the active clients list.         | `10`                                                         |
| `CLIENT_SAVE_INTERVAL`      | The interval in seconds at which the active client count is saved to a file.                        | `10`                                                         |
| `CLIENT_COUNT_FILE`         | The name of the file to save the active client count to.                                            | `client_count.txt`                                           |

## Tool Configuration (`mcp_config_file.json`)

Create an `mcp_config_file.json` file in the root of the project (you can copy `mcp_config_file.json.example`). This file defines the external tools that Chanakya can use through the Model Context Protocol (MCP).

The file contains a single JSON object with a key `mcpServers`. This key holds an object where each key is the name of a tool and the value is an object describing how to run the tool's server.

### Tool Server Configuration

Each tool server configuration object has the following properties:

| Key       | Description                                                                                                             |
| --------- | ----------------------------------------------------------------------------------------------------------------------- |
| `command` | The command to execute to start the tool server (e.g.,`npx`, `uvx`, `python`).                                          |
| `args`    | An array of arguments to pass to the command.                                                                           |
| `env`     | (Optional) A JSON object of environment variables to set for the tool's process. This is where you should put API keys. |

### Example

Here is an example snippet from `mcp_config_file.json`:

```json
{
  "mcpServers": {
    "fetch": {
      "command": "uvx",
      "args": ["mcp-server-fetch"]
    },
    "brave-search": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-brave-search"],
      "env": {
        "BRAVE_API_KEY": "YOUR_BRAVE_SEARCH_API_KEY_HERE"
      }
    },
    "weather": {
      "command": "npx",
      "args": ["-y", "@timlukahorstmann/mcp-weather"],
      "env": {
        "ACCUWEATHER_API_KEY": "YOUR_ACCUWEATHER_API_KEY_HERE"
      }
    }
  }
}
```

In this example:

- The `fetch` tool is run using `uvx`.
- The `brave-search` tool is run using `npx`, and it requires a `BRAVE_API_KEY` environment variable.
- The `weather` tool is also run using `npx` and requires an `ACCUWEATHER_API_KEY`.

You will need to edit this file to provide your own API keys and to add or remove tools as needed. For more information on available MCP tools, please refer to the [Model Context Protocol Servers]([modelcontextprotocol/servers: Model Context Protocol Servers](https://github.com/modelcontextprotocol/servers)). You can also create your own server.

## Fix mcp tool related problems

The MCP servers share a list and description of tools with the MCP clientto ensure proper communication. However, the tool descriptions are sometimes incomplete. In such cases, you can provide instructions directly to the Tool Agent by modifying the `tool_specific_instructions.txt` file.
Use [Rishabh-Bajpai/testmcp](https://github.com/Rishabh-Bajpai/testmcp) to see tools descriptions


