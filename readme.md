# Email splicer
> *Email splicer and username lookup tool*

This tool attempts to find accounts associated with this tool by looking up the first part of the target email which may be a username on some sites.

# How it works

It attempts to get the profile page of a website, if it fails it will normally return a 400 or 404 request showing it failed, I use this and if the status code is 400 or 404 it does not print that link otherwise it prints found on `link`

# Install

1. Run `pip install -r requirements` to install the requirements necessary to run this\
2. Run `python E-S.py` to run the script
3. Input and email and watch the magic happen

# How to add more emails

1. You will need to find the user profile site for the page and have the status code for when it fails\
2. Add the site to the list of sites called `sites` and add the fail request to the `bad_requests` list\
3. You are also able to add more email extensions in the `emaillist` list (you only need the name not the .{something})