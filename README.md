# DisqusDump

This little Python code saves Disqus user comments with some statistics.

## Usage

Run in terminal:
<pre><code>python2 disqusdump.py</code></pre>

You need to provide your API public and secret keys in config.py file:
<pre><code>public_key = "YOUR_KEY"
secret_key = "YOUR_SECRET"
</code></pre>

The username who is targeted by the dump:
<pre><code>user = "username"
</code></pre>

Change some config values or leave default.

The output are two files in dump/ dir one with dumped messages second is with some statistics.

**Statistics saved by this script:**
 - Order and save by most liked messages
 - Most popular partners of user ordered by reply number
 - Hour, Weekday and month occurrence of messages
 - Total chars and messages number
 
**Disqus-python API is mandatory:**\
[https://github.com/disqus/disqus-python](https://github.com/disqus/disqus-python)\
⚠ Be aware this is for Python2.7 and the current release is not runnable. Check the issues tab.
