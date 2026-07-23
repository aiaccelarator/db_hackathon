Welcome to the 2026 TDI Global Hackathon!
Hello and welcome to the TDI Global Hackathon 2026. You have access to a repo in this organisation for your team. Please locate it and read the README before doing anything else.

If you have any access problems for Azure, GCP, GitHub, HCP Terraform or OpenShift, please raise an issue here.

Good luck!

What's here? 📜
Your Hackathon Environment 🍬
Login 🚪
Microsoft Azure ☁️
Google Cloud Platform ☁️
GitHub 📑
Terraform Cloud 🔨
RedHat OpenShift 🚀
Microsoft Teams 💬
Additional useful guides
When the time comes 💔
Your Hackathon Environment 🍬
Your hackathon environment consists of the following components:

A Google Cloud project for your team, see here which allows you to consume Google Cloud (within a pre-set budget). ☁️
A Microsoft Azure resource group for your team, see here which allows you to consume Azure. ☁️
This GitHub repository which you can use to store your code. 📑
A Terraform Cloud workspace see here allowing you to deploy with Terraform into GCP. 🔨
A namespace in a shared RedHat Openshift cluster see here which can be used to deploy into Azure. 🚀
A Microsoft Teams instance with a global support team and a dedicated MS Team for each hackathon team. 💬
You have considerable interactive access to your GCP project and Azure resource group. Using the GitHub repository, the Terraform Cloud workspace and RedHat OpenShift cluster are entirely optional but may aid you.

Login 🚪
Caution

Do not attempt logins, follow links, or otherwise conduct hackathon activity from a DB device. The whole event is designed to run off DB's corporate infrastructure. The instructions below are alternatively available on Confluence inside the DB network. It is entirely possible to follow these instructions from a mobile device running iOS or Android or a laptop.

Tip

If you participated in the hacakthon last year with the same personal email, you may have saved your password for your SSO account (that will be the same format). Last year's password won't work on the initial login., you have a new Entra account (even with the same ID).

How do I login? 🎥
(The following is split into 3 videos due to a file size restrction of 100MB in GitHub per video)

 participants-1.mp4 
 participants-2.mp4 
 participants-3.mp4 
Register in the Plus You registration portal 📋
Prior to the event you will have registered via the Plus You portal.

Ensure your personal email, team, location and GitHub handle are correctly entered in the user registration portal (accessible only from within the DB network).

You can update your own details. If you do not have a GitHub handle, you can create one for free.

This is the golden source for the configuration of the hackathon environment. We will take periodic updates from this in the opening hours of the event.

All registered users will get access to Azure, GCP, HCP Terraform and OpenShift, but only those that have listed a valid GitHub handle will gain access to GitHub.

Your Single Sign On (SSO) ID 🛂
Most of this year's tooling is connected to a central Identity Provider (IdP), Entra ID (formerly Azure Active Directory).

Your ID in the IdP is not the personal email address that you signed up with, but rather a transformation of it.

To determine your ID, take the personal email you signed up with, replace the @ with a . and add the suffix @db-hackathon.com.

For example, foo@bar.com becomes foo.bar.com@db-hackathon.com.

This is the email/ID you should use when prompted for SSO login via Microsoft Entra ID.

Login 🔗
Microsoft Azure ☁️
Start with Microsoft Azure and use the SSO ID described above (e.g foo.bar.com@db-hackathon.com)

Use the initial password given in your briefing. Your team lead can remind you of it.

You will be prompted to change it on first login and additionally set up two factor authenication. Please do so immediately.

Google Cloud Platform ☁️
For Google Cloud Platform, when logged in, you should be able to see a project named after your team prefixed with hack-team- and a project named hackathon-seed-2026 which contains a storage bucket with shared materials for your consideration.

GitHub 📑
For GitHub, only participants who registered with a GitHub handle will be invited to the GitHub organisation. These participants will receive an email at their registered personal email address with a convenient direct link to accept the invitation.

Attempt to login to GitHub via your SSO identity first (e.g foo.bar.com@db-hackathon.com). When prompted, you can then sign-in to GitHub with the handle/account you registered with (e.g foo-bar). Once logged in, you will need to accept the invitation to the organisation db-hackathon.

Tip

Some users report that they need to re-open the link from the email after the first GitHub and SSO log-in in order to see the invitation.

Tip

You may not see the repository when you first log-in. Try again after one hour (as it may take some time for your user to propagate through).

Terraform Cloud 🔨
For Terraform Cloud, when prompted for Organization Name use db-hackathon-2026.

If you do not already have a HCP Terraform account associated with the email address you used to register for this event, you will be prompted to create one and link it to the above SSO ID.

Alternatively, if you do already have HCP Terraform account, follow the option to Link to existing HCP Terraform account.

Once logged in, you should be able to see a workspace named after your team prefixed with hack-team-.

Redhat OpenShift 🚀
Visit the OpenShift Console, and selected Log in with AAD (Azure Active Directory a.k.a Entra).

Microsoft Teams 💬
For Microsoft Teams, you can access via a browser or via the desktop app.

Tip

The full desktop app is notably better for video calls and screen sharing, but all other facilities are equal.

Getting Help 🩹
If you have difficulty with any of these steps:

Prior to the event:

You can seek help inside the DB network on a best-efforts basis in the DB Teams channel advertised in your briefing.
During the event:

Preferably please raise an issue in the support repo, (or ask a team member to do so on your behalf if you don't have access to GitHub). This will be the fastest route to resolution.
If you are in person at a location, look out for the Global Enterprise Engineers (GEE's) or other support staff.
Alternatively, raise it in the event Microsoft Teams support channel, (or ask a team member to do so on your behalf).
Additional useful guides
Hackathon Briefing Pack
When the time comes 💔
It's sad to think about the end of the event but when the time does come, you will have two hours from the end of the closing ceremony to export anything from GCP that you wish to retain.

After this time we will deactivate the billing link on your project and all of your resources will instantly be torn down.

Your GitHub repository will remain available until the end of the day on 25th July.

If you wish to retain its contents, please clone it before this time.

PinnedLoading
 support Private
Help and support for the TDI Global Hackathon 2025

 Python  2

 Repositories
Find a repository…
Loading
Showing 3 of 3 repositories
test2026 Internal
 Python  1  0  0  0 Updated
