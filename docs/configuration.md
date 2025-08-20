# Configuration

Chanakya is configured using two main files: `.env` for environment variables and `mcp_config_file.json` for tool configuration.

## Environment Variables (`.env`)

Create a `.env` file in the root of the project (you can copy `.env.example`). This file contains the core configuration for Chanakya.

| Variable                      | Description                                                                                                                                                   | Example                                           |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| `LLM_PROVIDER`              | The provider for your LLM. Can be `ollama` or `openai` (for any OpenAI-compatible API like LM Studio). Defaults to `ollama`.                            | `openai`                                        |
| `LLM_ENDPOINT`              | The URL of your main LLM endpoint. For Ollama, this is the server URL. For OpenAI-compatible APIs, this is the base URL. (Use /v1 for OpenAI-compatible APIs) | `http://localhost:1234/v1`                      |
| `LLM_MODEL_NAME`            | The name of the model to use for the main agent.                                                                                                              | `your-model-name`                               |
| `LLM_NUM_CTX`               | The context window size for the main LLM.                                                                                                                     | `4096`                                          |
| `LLM_API_KEY`               | Your API key for OpenAI-compatible endpoints. For local servers like LM Studio, this can often be left blank or set to a dummy value.                         | `sk-12345`                                      |
| `LLM_ENDPOINT_SMALL`        | (Optional) The URL for a secondary, smaller LLM for tasks like query refinement. If empty, defaults to `LLM_ENDPOINT`.                                      | `http://localhost:1234/v1`                      |
| `LLM_MODEL_NAME_SMALL`      | (Optional) The name of the smaller model. If empty, defaults to `LLM_MODEL_NAME`.                                                                           | `your-small-model-name`                         |
| `LLM_NUM_CTX_SMALL`         | (Optional) The context window size for the smaller model. If empty, defaults to `LLM_NUM_CTX`.                                                              | `2048`                                          |
| `STT_SERVER_URL`            | The URL of your Speech-to-Text (STT) server.                                                                                                                  | `http://localhost:8000/v1/audio/transcriptions` |
| `TTS_ENGINE`                | The Text-to-Speech (TTS) engine to use. Can be `coqui` or `piper`.                                                                                        | `coqui`                                         |
| `TTS_SERVER_URL`            | The URL of your Text-to-Speech (TTS) server.                                                                                                                  | `http://localhost:5002/api/tts`                 |
| `DATABASE_PATH`             | The path to the SQLite database file for long-term memory.                                                                                                    | `database/long_term_memory.db`                  |
| `WAKE_WORD`                 | The wake word for the voice assistant. Defaults to "Chanakya".                                                                                                | `Chanakya`                                      |
| `APP_SECRET_KEY`            | A secret key for the Flask application. If not provided, a new one will be generated on each start.                                                           | `a_very_secret_key`                             |
| `CLIENT_INACTIVE_THRESHOLD` | The time in seconds after which an inactive client is removed from the active clients list.                                                                   | `10`                                            |
| `CLIENT_SAVE_INTERVAL`      | The interval in seconds at which the active client count is saved to a file.                                                                                  | `10`                                            |
| `CLIENT_COUNT_FILE`         | The name of the file to save the active client count to.                                                                                                      | `client_count.txt`                              |

## Tool Configuration (`mcp_config_file.json`)

Create an `mcp_config_file.json` file in the root of the project (you can copy `mcp_config_file.json.example`). This file defines the external tools that Chanakya can use through the Model Context Protocol (MCP).

The file contains a single JSON object with a key `mcpServers`. This key holds an object where each key is the name of a tool and the value is an object describing how to run the tool's server.

### Tool Server Configuration

Each tool server configuration object has the following properties:

| Key         | Description                                                                                                             |
| ----------- | ----------------------------------------------------------------------------------------------------------------------- |
| `command` | The command to execute to start the tool server (e.g.,`npx`, `uvx`, `python`).                                    |
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
