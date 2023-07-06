import os
from twilio.rest import Client


class NotificationManager:
    """
    This class is responsible for sending notifications with the deal flight details."""
    def __init__(self):
        self.client = Client(os.environ['TWILLIO_SID'], os.environ['TWILLIO_TOKEN'])

    def send(self, message: str, from_number: str, to_number: str):
        """
        Sends a WhatsApp message
        Parameters
        ----------
        message
            Message to send.
        from_number
            Sender number.
        to_number
            Receiver number.

        Returns
        -------
            The status of the message.
        """
        message = self.client.messages.create(body=message, from_=f"whatsapp:{from_number}", to=f"whatsapp:{to_number}")
        return message
