from crops_webhook import WebhookApp
from flask import Flask
app = WebhookApp(Flask(__name__)).app
