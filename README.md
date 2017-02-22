# Packt Press Claim

Claims the current daily free ebook from https://www.packtpub.com/packt/offers/free-learning for the account configured in the script. I was frustrated that I missed several excellent books when on vacation and wanted to automate the process of processing the claim on the web page. The excellent script by Mikhail Plekhanov worked until recently. This is a quick rewrite. The packt.py script borrows heavily from:
 * https://github.com/movb/packt-grabber
 * https://github.com/igbt6/Packt-Publishing-Free-Learning
 * https://github.com/niqdev/packtpub-crawler

## Dependencies

The script requires at minimum the python packages:

```sh
pip install requests beautifulsoup4
```

It is confirmed to run on both Python 2.7 and 3.4 from my local testing on Ubuntu 12.04, 14.04 and 16.04. I see no reason it will not run on Windows, Mac or other Linux variants.

## Configure

Edit 31 and 32 lines, and enter your credentials for your packtpub account.

```python
email    = 'CHANGE_ME@google.com'
password = 'CHANGE_ME_TOO'
```

## Run daily

Add this lines to your crontab (run _crontab -e_) to run this script every day at midnight:
```
0 0 * * * python /path/to/packt-press-claim/packt.py &>/dev/null
```

## Feedback

I welcome feedback. This is not the most elegant code.
