from module6.league.exceptions import DuplicateOid, DuplicateEmail
import yagmail


class Emailer:
    """This class is responsible for sending emails using yagmail"""

    # class variables:
    sender_address = None
    _sole_instance = None

    @classmethod
    def configure(cls, sender_address, sender_password):
        """sets the class variable sender_address as specified."""
        cls.sender_address = sender_address
        cls._sole_instance = yagmail.SMTP(sender_address, sender_password)

    @classmethod
    def instance(cls):
        """--return the only instance of this class."""
        if cls._sole_instance is None:
            raise ValueError("Emailer not configured. Please configure first")
        return cls._sole_instance

    def send_plain_email(self, recipients, subject, message):
        """ sends plain text email to the specified recipients."""
        if not isinstance(recipients, list):
            recipients = [recipients]

        self._sole_instance.send(to=recipients, subject=subject, contents=message)
        for recipient in recipients:
            print(f"Sent email to {recipient}")


# example
Emailer.configure("sellmynissan13@gmail.com", "n1ss4n$$")

# send email
emailer = Emailer.instance()
emailer.send_plain_email(
    recipients=['msf0034@auburn.edu'],
    subject="Hello Test Email",
    message="Hello Test Email sent using yagmail"
)
