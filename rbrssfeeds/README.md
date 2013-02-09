## RSS Feeds Extension for ReviewBoard

This extension adds RSS Feed (RSS 2.01 and Atom 1) support to Reviewboard. You can get RSS Feeds for yourself or for any user using this extension. It is also possible to get an RSS Feed (Only RSS 2.01 support) for all review requests.

#### Features
* Adds RSS 2.01 and Atom 1 support for User Feeds
* Dashboard points to the current users' feed
* Use the format /feeds/feed/<username> to get to another users' feed. Add Query string of "type=atom" to get an Atom Feed. For e.g. to get to userX's atom feed, use /feeds/feed/userX?type=atom and to get to userX's RSS feed, use /feeds/feed/userX
* Dashboard also points to RSS Feed for all Review Requests 
* Supported from Reviewboard 1.7 onwards

#### How to install
* Clone this git repository
* cd rb-extension-pack/rbrssfeeds
* python setup.py install
* Go into Reviewboard's Extensions page (Reviewboard Admin has an Extensions navigation bar link) and "Enable" the RB-RSSFeeds Extension
* Enjoy! Your Dashboard should now have Links.

#### Screenshots
<div>
<b>Screenshot of Dashboard With the Extension installed</b>
<img src="http://rajasaur.github.com/rb-extension-pack/screenshots/rbrssfeeds/feeds_dashboard.png" width=800 height=500" /> 
</div>
<hr />
<div>
<b>Using a Liferea Client on Ubuntu with a feed obtained using this Extension</b>
<img src="http://rajasaur.github.com/rb-extension-pack/screenshots/rbrssfeeds/liferea_feedpage.png" width=800 height=500" />
</div>

#### Authors
* Dolanor Tharivae - for the original source to the RSS Feed
* Raja Venkataraman
