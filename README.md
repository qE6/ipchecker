# IPChecker
IPChecker is small script for getting an IP information

# Screenshots



# Installation (Debian-based distro)
```
sudo apt install python3 python3-colorama python3-requests git
git clone https://github.com/qE6/ipchecker && cd ipchecker
```
Installation in one line:
```
sudo apt install python3 python3-colorama python3-requests git -y && git clone https://github.com/qE6/ipchecker && cd ipchecker
```

# Usage
```
python3 ipchecker.py <ip>
```

# Errors
```
[-] IP Format error - This error signals that your ip format is invalid. Maybe some nums bigger then 255 or IP contains letters.
[-] Answer error - This error signals about invalid answer from API. It will be shown when service will change its response. I will update, so I think you will never see this message.
[-] Something went wrong - This error signals about some errors with your network connection or with ip-api.com
[-] Failed. - This error signals that IP is invalid or IP unknown. This error show when ip-api returns "fail" in status
