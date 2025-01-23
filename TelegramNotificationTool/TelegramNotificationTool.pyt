import arcpy
import requests
import os

class TelegramNotificationTool(object):
    """A tool to send a Telegram message after a process is completed."""
    def __init__(self):
        self.label = "Telegram Notification Tool"
        self.description = (
            "The Telegram Notification Tool allows users to send a notification "
            "message to a specific Telegram chat using the Telegram Bot API."
        )
        self.canRunInBackground = True
        
        # Help file is assumed to be in the same directory as the .pyt file
        self.helpFile = os.path.join(os.path.dirname(__file__), "TelegramNotificationTool.xml") # Help file path


class Toolbox(object):
    """Python Toolbox for sending Telegram notifications."""
    def __init__(self):
        self.label = "Telegram Notification Tool"
        self.alias = "telegram_toolbox"

        # Tools in the toolbox
        self.tools = [TelegramNotificationTool]

class TelegramNotificationTool(object):
    """A tool to send a Telegram message after a process is completed."""
    def __init__(self):
        self.label = "Telegram Notification Tool"
        self.description = (
            "Sends a Telegram notification using Telegram Bot API. "
            "This tool can be used at the end of a geoprocessing model in ModelBuilder "
            "or as a standalone tool to notify about task completion."
        )
        self.canRunInBackground = True  # Allows running in the background.

    def getParameterInfo(self):
        """Defines tool parameters."""
        params = []

        # 1. Telegram Bot API Token
        param_telegram_api = arcpy.Parameter(
            displayName="Telegram API Token",
            name="telegram_api_token",
            datatype="GPString",
            parameterType="Required",
            direction="Input"
        )
        param_telegram_api.description = (
            "The API token provided by BotFather when you create a Telegram bot."
        )
        params.append(param_telegram_api)

        # 2. Telegram Chat ID
        param_chat_id = arcpy.Parameter(
            displayName="Telegram Chat ID",
            name="chat_id",
            datatype="GPString",
            parameterType="Required",
            direction="Input"
        )
        param_chat_id.description = (
            "The chat ID where the message will be sent. This can be your user ID, "
            "a group ID, or a channel ID."
        )
        params.append(param_chat_id)

        # 3. Notification Message
        param_message_text = arcpy.Parameter(
            displayName="Notification Message",
            name="message_text",
            datatype="GPString",
            parameterType="Required",
            direction="Input"
        )
        param_message_text.value = "The geoprocessing task has been successfully completed!"
        param_message_text.description = (
            "The text message to be sent to the specified Telegram chat. "
            "You can use this to notify about task completion or add custom information."
        )
        params.append(param_message_text)

        return params

    def execute(self, parameters, messages):
        """Main logic for sending the Telegram message."""
        # Retrieve parameter values
        telegram_api_token = parameters[0].valueAsText
        chat_id = parameters[1].valueAsText
        message_text = parameters[2].valueAsText

        # Define the Telegram API URL
        url = f"https://api.telegram.org/bot{telegram_api_token}/sendMessage"
        payload = {"chat_id": chat_id, "text": message_text}

        # Attempt to send the message
        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()  # Raise an exception for HTTP errors
            messages.addMessage(f"Telegram message sent successfully: {response.json()}")
        except requests.exceptions.RequestException as e:
            messages.addErrorMessage(f"Failed to send Telegram message: {e}")
            raise

        return