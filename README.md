# DisqusDump

This little Python code saves Disqus user comments with some statistics.

You need to provide yours API public and secret keys in config.py file:\
<code>
public_key = "YOUR_KEY"\
secret_key = "YOUR_SECRET"
</code>

The username who is targeted by the dump:\
<code>
user = "username"
</code>

Or change some config values.

**Statistics that can be saved by this script:**
 - Order and save by most liked messages
 - Most popular partners of user ordered by reply number
 - Hour, Weekday and month occurrence of messages
 - Total chars and messages number
 
You need to install the disqus-python API:\
[https://github.com/disqus/disqus-python](https://github.com/disqus/disqus-python)\
⚠ Be aware this is for Python2.7 and the current release is not runnable. Check the issues tab.
