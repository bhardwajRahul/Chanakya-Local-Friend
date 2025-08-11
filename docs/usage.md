# How to Use Chanakya

This guide explains how to interact with the Chanakya voice assistant through its web interface.

## Accessing the Interface

Once Chanakya is running, open your web browser and navigate to the appropriate URL:
-   If running locally with a self-signed certificate: `https://localhost:5001`
-   If running locally without HTTPS: `http://localhost:5001`
-   If running on a different machine or with a reverse proxy, use the appropriate IP address or domain name.

## Main Interface Overview

The main interface consists of a central animation area, a status indicator, a chat history panel, and a control bar at the bottom.

![Chanakya UI](placeholder.png)  <!-- You can replace this with a real screenshot -->

### Control Buttons

The bottom control bar provides several buttons for interacting with the assistant:

| Button | Icon | Description                                                                                                                                                             |
| ------ | :--: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Send Text** |  ✉️  | Sends the text currently in the message input box to the assistant. You can also press `Enter` in the input box.                                                  |
| **Manual Record** |  🎤  | Manually starts and stops recording your voice. Click once to start, and click again to stop. The recorded audio will be sent as your command.                    |
| **Play Last Response** |  🔊  | Plays the assistant's last spoken response again.                                                                                                       |
| **Call Mode** |  📞  | Toggles "Call Mode". In this mode, the assistant uses Voice Activity Detection (VAD) to listen for your voice continuously, allowing for a more natural back-and-forth conversation. Click the "🛑" button to end the call. |
| **Toggle Keyword Listening** |  👂  | Toggles the wake word detection. When active, the assistant will listen for "Hey Chanakya" or "Hi Chanakya" to activate.                                    |

### Top Bar Controls

| Button | Icon | Description                                                                                                                                                             |
| ------ | :--: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Toggle Chat View** |  💬  | Shows or hides the chat history panel on the right side of the screen.                                                                                    |
| **Manage Memories** |  🧠  | Navigates to the Memory Management page, where you can view, add, and delete the assistant's long-term memories.                                            |
| **Dark Mode** |  🌙  | Toggles between light and dark mode for the user interface.                                                                                                     |

## Basic Interaction Flow

1.  **Unlock Audio:** When you first load the page, you may need to click anywhere on the page to enable audio. This is a security feature in modern browsers.
2.  **Activate the Assistant:** After unlocking audio, you can activate the assistant using one of the methods below.

### Activation Keywords

You can activate Chanakya using your voice if "Keyword Listening" is enabled (toggled with the 👂 button). There are several keywords, each with a slightly different function:

-   **"Hey Chanakya"** or **"Hi Chanakya"**: These are the primary wake words. After you say one of these, the assistant will start listening for your command. This is useful for standard, single-turn commands.
-   **"Chanakya"**: Saying the name "Chanakya" by itself at the end of a sentence will also activate the assistant. This triggers a shorter recording window and is useful for quick, single-word commands or short phrases.

### In-Call Keywords (Stop & Bye)

When you are in the continuous "Call Mode" (activated by the 📞 button), you can use the following keywords to control the conversation:

-   **"Stop"**: If the bot is currently speaking, you can say "stop" to interrupt it. This allows you to immediately "barge-in" and start speaking your next command without waiting for the bot to finish its sentence.
-   **"Bye"**: Saying "bye" (or variations like "goodbye") will end the call. The assistant will give a final response and the call mode will be deactivated.

**Note:** There is no spoken keyword to stop a manual recording. This must be done by clicking the "🛑" button.

### Manual Activation

-   **Manual Record Button (🎤):** You can click this button to manually start and stop recording. Click once to start, and click again to stop. This gives you full control over the recording duration.
-   **Call Mode Button (📞):** For a more continuous conversation, you can use Call Mode. In this mode, the assistant uses Voice Activity Detection (VAD) to listen continuously, allowing for a natural back-and-forth exchange without needing to use a wake word for each turn.

3.  **Give Your Command:** After activation, the status indicator will change to show that it's listening. Speak your command or question clearly.
4.  **Receive Response:** The assistant will process your command, and you will hear the spoken response. The conversation will also appear in the chat panel.

## Managing Memories

Chanakya can store information across conversations to provide a personalized experience. You can manage this memory through the web interface.

For a detailed guide on how to view, add, delete, and effectively use memories, please see the [Managing Memories](./memory-management.md) documentation.
