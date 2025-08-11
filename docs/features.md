# Features

Chanakya is built with a set of powerful features that make it a flexible and private voice assistant.

## Local First, Privacy Focused

The core design principle of Chanakya is to keep your data private. This is achieved by leveraging local services for the most sensitive parts of the AI pipeline.

-   **Local LLM Integration:** Chanakya uses [Ollama](https://ollama.com/) to run large language models on your own hardware. This means your conversations are not sent to third-party cloud providers. You have full control over which models you use.
-   **Local STT/TTS:** Speech-to-Text and Text-to-Speech are handled by local servers like Faster Whisper and Coqui TTS. Your voice data never leaves your network.

## ReAct Agent Architecture

Chanakya uses a **ReAct (Reason + Act)** agent architecture. This is a sophisticated approach that allows the language model to reason about a problem, decide on a course of action, and then use tools to execute that action.

This is different from a simple chatbot that just generates text. The ReAct agent can break down complex requests into smaller, manageable steps.

**How it works:**

1.  The user gives a command (e.g., "What's the weather in London and can you search for the best fish and chips there?").
2.  The LLM **reasons** that it needs to perform two tasks: get the weather and then perform a web search.
3.  It formulates a **thought**: "I need to get the weather first."
4.  It chooses an **action**: Use the `weather` tool with the input "London".
5.  The system executes the tool and gets the weather information.
6.  The agent receives the result and formulates a new **thought**: "Now I need to search for fish and chips."
7.  It chooses another **action**: Use the `brave-search` tool with the input "best fish and chips in London".
8.  The system executes the search.
9.  Finally, the agent combines the information from both tool outputs into a single, coherent **final answer** for the user.

This architecture makes Chanakya much more powerful and capable of handling multi-step tasks.

## Extensible Tool System (MCP)

Chanakya's tools are managed through the **Model Context Protocol (MCP)**. MCP is a standardized way for language models to discover and use external tools.

This means you can easily extend Chanakya's capabilities by adding new MCP-compatible tool servers.

-   **Configuration:** You can add any MCP tool server to the `mcp_config_file.json`. Chanakya will automatically load it on startup.
-   **Examples:** The default configuration includes tools for web searching, fetching web content, and getting the weather. Many more community-made tools are available.
-   **Custom Tools:** You can create your own tools by following the MCP specification.

This flexible system allows you to tailor Chanakya's abilities to your specific needs.

## Long-Term Memory

Chanakya has a long-term memory feature that allows it to remember information across conversations. This is achieved by storing facts in a local SQLite database.

-   **Automatic Retrieval:** When you ask a question, Chanakya first searches its memory for relevant information before consulting the LLM. This makes it faster and more knowledgeable about topics you've discussed before.
-   **Memory Management UI:** You can view, add, and delete memories through a simple web interface, giving you full control over what Chanakya knows. To access it, click the "🧠" icon on the main page.
-   **Query Refinement:** Chanakya uses a small, secondary LLM to refine your questions into keywords for more effective memory searching.

This feature allows Chanakya to learn and grow with you over time, creating a more personalized experience.

## Customizable UI

The web interface is clean and modern, with features designed for a good user experience.

-   **Dark Mode:** You can toggle between light and dark themes.
-   **Responsive Design:** The UI is designed to work on both desktop and mobile browsers.
-   **Real-time Feedback:** The status indicator and orb animation provide real-time feedback on what the assistant is doing (e.g., listening, processing, speaking).
