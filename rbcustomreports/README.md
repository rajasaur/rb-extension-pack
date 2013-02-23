## Custom Reports Extension for ReviewBoard

This extension adds custom reports to Reviewboard. These appear in the dashboard page of every user. Currently the reports avialable are
* Review Requests not Reviewed by anyone
* Review Requests that are not Reviewed by me
* Review Requests that have a Ship-It but not Submitted.
* Filter ReviewRequests by Repositories that a user has access to.

#### Features
* Administrator has the capability to select which reports will be available for all users of Reviewboard
* Dashboard contains the reports selected by the administrator
* Filter by Repository reports show list of repositories a user has access to and the review requests against that repository
* Available in the Dashboard so all customizable columns for Review requests are available for these reports too.
* Supported from Reviewboard 1.7 onwards

#### Roadmap
* Other reports (Please file an issue for what types of reports are required)
* Show counts of review requests next to the names of the reports.

#### How to install
* Clone this git repository
* cd rb-extension-pack/rbcustomreports
* python setup.py install
* Go into Reviewboard's Extensions page (Reviewboard Admin has an Extensions navigation bar link) and "Enable" the RB-Custom-Reports Extension
* Click on the Configure link and select the list of reports that you want to appear on everyone's dashboard. This is multi-selectable
* Enjoy! Your Dashboard should now have the reports.

#### Screenshots
<div>
<b>Administration screen allowing selection of reports to appear in dashboard</b>
<img src="http://rajasaur.github.com/rb-extension-pack/screenshots/rbcustomreports/reports_configure.png" width=800 height=500" /> 
</div>
<hr />
<div>
<b>Dashboard with all reports configured</b>
<img src="http://rajasaur.github.com/rb-extension-pack/screenshots/rbcustomreports/dashboard_with_all_reports.png" width=800 height=500" />
</div>
<hr />
<div>
<b>Dashboard with only some reports configured</b>
<img src="http://rajasaur.github.com/rb-extension-pack/screenshots/rbcustomreports/dashboard_with_configured_reports.png" width=800 height=500" />
</div>
