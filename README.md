# Dropbot
 
Dropbot is WhatsApp chatbot that will help you to save media from your phone to 
a dropbox file.

Functions:
1. Save media in your phone to a folder created for your using your cell number
2. Save selfies and live videos instantly
3. Record audios into your Dropbox folder
4. Get a web link to view your folder
5. Get a list of files in your whatsapp chat
6. Contact us for support if you need help

It uses Dropbox APIs, NGROK, Flask, Twilio and Python. You can host anywhere you want like AWS etc.
1. To test, download repository to your machine: https://github.com/mcwilton/dropbox-app.git
2. Install Python and configure the environment
3. Register and get a free trial account with Twilio
4. Register and get an api key to access DropBox
4. Run Ngrok.exe, and run this command: ngrok http 5000
5. Copy the webhook with https:// and past that in your Twilio whatsapp sandbox
6. Run the requirements file to install the dependancies: pip install -r requirements.txt
7. Run this command: set FLASK_APP=app.py
8. To run your script: python -m flask run
9. Test the bot and have fun

For an already installed demo, 
1. Save this number +1 (415) 523-8886 as Dropbot in your phone.
2. Send this WhatsApp message to the number: join here-mathematics
3. You are ready to test. Type Hi

Demo is hosted on AWS.***

Whats next
1. Ability to upload texts
2. Ability to upload documents
3. Ability to create own folders
4. Ability to extract file links
