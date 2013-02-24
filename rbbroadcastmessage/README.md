## Broadcast Messages for ReviewBoard

This extension allows an administrator to publish broadcast messages to the users of reviewboard. These messages are configurable through the Extensions' Administration and will be shown in every page. You could also clear out the message to remove a broadcast message.

#### Features
* Adds the capability to publish Broadcast messages to the users of the system
* Maximum length of the message is 128 characters and only allows plain text
* Clearing the message removes the broadcast. 
* Supported from Reviewboard 1.7 onwards

#### How to install
* Clone this git repository
* cd rb-extension-pack/rbbroadcastmessage
* python setup.py install
* Go into Reviewboard's Extensions page (Reviewboard Admin has an Extensions navigation bar link) and "Enable" the RB-BroadcastMessage Extension
* Click on the "Configure" link in the extension, which allows you to enter a Broadcast message. Enter the message and Save.
* Enjoy! All pages of the Reviewboard installation should have the Broadcast message.

#### Troubleshooting
In case you get a TemplateNotFound on rbbroadcastmessage/message.html **immediately** after enabling the extension, there is a transient bug thats causing it to happen. Please restart the server and it should start working from them on.I will update if this bug gets resolved by then. 

#### Screenshots
<div>
<b>Configuration of Broadcast Message in Extensions Administration</b>
<img src="http://rajasaur.github.com/rb-extension-pack/screenshots/rbbroadcastmessage/broadcast_configure.png" width=800 height=500" /> 
</div>
<hr />
<div>
<b>Broadcast message in Dashboard page</b>
<img src="http://rajasaur.github.com/rb-extension-pack/screenshots/rbbroadcastmessage/broadcast_dashboard.png" width=800 height=500" />
</div>

