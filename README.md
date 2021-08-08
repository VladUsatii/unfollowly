# unfollowly

Get notified when someone unfollows you on social media.

This is something that I wish social media had. It would stimulate so much more usage of the platform (anxious usage, if any). This application will only notify you for any future unfollows from the time you activated our server to the time you turned it off.

## Installation

To download:

```bash
git clone https://github.com/VladUsatii/unfollowly.git
cd unfollowly
pip install -r requirements.txt
```

In a text editor, you must add your username and password into the code. To do so:

```bash
cd unfollowly # there is a second unfollowly folder inside the folder
vi views.py # if you use vim, otherwise use 'code views.py' for VSCode.

# ...
# vim

# in the area where there are two variables username and password, change the string to your username and password.
:w:q
cd ..
```

To run:

```bash
chmod +x pub.sh
./pub.sh
```

This will take thirty to forty seconds. The Instagram server is receiving hundreds of requests and must allocate storage and retrieval space. In order for the server to retrieve data, load ```localhost:5000``` or your specified port. If you aren't sure of your port, the terminal output explains where to open the Flask server.

And you're done. Now, keep the server running and it will update every hour to check if someone has unfollowed you. If so, it will make a diff file on the unfollower and the amount of unfollows. Then, it will notify you of who and how many people unfollowed you. The notification will pop up in the terminal output, as well as in an on-page HTML notification.

## Supported Apps

* Instagram
TODO: Add support for Twitter and YouTube (Twitter is much more leniant on requests to their API).

---
Created by Vlad Usatii @ [youshould.readproduct.com](http://youshould.readproduct.com)
