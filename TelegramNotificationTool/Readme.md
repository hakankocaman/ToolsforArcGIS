Description
  The Telegram Notification Tool allows users to send a notification message to a specific Telegram chat using the Telegram Bot API. This tool can be used as a standalone geoprocessing tool or integrated into ModelBuilder workflows. It is particularly useful for notifying task completion or providing updates during long-running geoprocessing workflows.

Usage
  The tool is designed to send a message to a Telegram user, group, or channel. Users need to provide the following:
    1. A valid Telegram Bot API Token (created via BotFather).
    2. The Chat ID of the Telegram recipient (user, group, or channel). 
    3. A custom message to be sent as a notification.
This tool can be used in any geoprocessing workflow or as a standalone tool in ArcGIS Pro.
              
Tags
  Telegram, Notification, Task Completion, ModelBuilder, Geoprocessing, Automation, Messaging

Credits
  The Telegram Notification Tool is developed for use in ArcGIS Pro workflows and is maintained by Hakan KOCAMAN ( www.hakankocaman.com ). The tool integrates Telegram’s messaging API for automated notifications.

Use limitations
  • This tool requires a working internet connection to send messages via the Telegram Bot API.
  • Ensure your Telegram bot is properly configured and has access to the chat where messages are being sent.
  • Users are responsible for the security of their API Token and should not share it publicly.
