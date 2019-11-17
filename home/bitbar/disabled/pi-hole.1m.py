#!/usr/bin/python
# -*- coding: utf-8 -*-
# <bitbar.title>Pi-hole status</bitbar.title>
# <bitbar.version>v1.0</bitbar.version>
# <bitbar.author>Siim Ots</bitbar.author>
# <bitbar.author.github>siimots</bitbar.author.github>
# <bitbar.desc>Show your Pi-Hole (Raspberry Pi adblocker) status. Todays blocked ads, DNS queries and number of domains in block list.</bitbar.desc>
# <bitbar.image>http://gis.ee/files/pihole-bitbar.png</bitbar.image>
# <bitbar.dependencies>pi-hole,python</bitbar.dependencies>


# NOTE from @hpcodecraft
# This is a modified version of the original Pi-Hole script found in the official plugins repo
# It adds the Pi-Hole icon to the status bar and gives more information if Pi-Hole can't be found

import urllib2
import json

# If you have UTF-8 problems then uncomment next 3 lines
#import sys
#reload(sys)
#sys.setdefaultencoding("utf-8")

# Change to Your Pi-Hole Admin Console URL
#pihole = "http://pi.hole/admin/"
pihole = "http://192.168.0.2/admin/"


pihole_connected_image = "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAABGdBTUEAALGPC/xhBQAAAAFzUkdCAK7OHOkAAAHyUExURQAAAHwCABsAAAcAAG4BAJwBAI0CAExpcQEAAAkAAOEAAI4CALQBAMYAAGUCACUAAEwBAGwAAACFAKIAAHwCAKoBAGwBAGIBAFsCAAHKAYMCAFABAAEHAf0AAP8AAAGlAfMAAL8BAA4DAJQCAKACAP4AAMcBAG4DAJYCAMEBAKsEAPoAAP0AAJoCAJ4CAP8AAJgCAJcCAAAGAMYBAMoBAJkCAAAAAJ4BAI4CAJgCAJECAADKA5kCAKICAAD4ANUBAP8AAP4AAMkEACoQANcBAMwBAP8AAJcCAPEAAApxCv8AAK4CAIBTB5ACAAD7AN0BAKsCAJcCAP8AAMEBAP8AAJMCAJkCAP8AAP8AAA6TCgqNCpgCAJACALcBAP0AAP8AANwUAbwBAJoCAJkCAP8AAP8AAP4AAO8AAJQCAJQCAAD6AAACAP8GAPwBAA2RDQLzAgOsAwb4Av8AAP4AAPsCAP4AAA2NDfEMAAHoBvYHAAD6BQP0AgDwCgfhBxGvERW9DAXqBO4PAQ+9DxG0EQnVCQaNBgvQCw+8DwvLCw3VCRlpGQzOCxG0EQvPCw3FDQ3GDQ+7DwnXCQjUC/8AAJgCAJUCAJkCAP0AAL0BAJQCAI8CAM4BAJoCAP4AAMoBAP4CAAL1AgfoBP4BAA3GDQ3FDRC7ECXz2z8AAACTdFJOUwEBAQEBAgQAAQEEAwMCAQECAgICBAQDAwMFAgIBGxkDGBYBCSzBKyop0wTS0Qyh1JDMAQkVuQkCu77mAuWsLuQV/L0B+9DQ49MC/skF7ILN1zf7QeHM+vXWAwRU/jX+3xgq/f0vU/056PImAQP5BTQDLYX70foForraru5kgxpBlxVckiED9+8axQHna+HvlvGyvhTq8ecAAAD4SURBVBjTHc7TdgRhFITRP/wysW3btm3btm1b3ZOJnfdMT5/Lvc6qKjGxzMHtzSlHsyDUm+by7+fqkPOZbOz1UMb2yfXxHbuf1bjpIb6d/d+Ls62vjXF89OAp2ti531xdnyMDNcefSvZW1uYnC1JU0BBO7+L3wkd+Mu4KmAkHcovflqbq31MTMFA+7Egseilt0TXWapMCMBaGrmRpn5tGhhrGBuRYTIUtUSVy/0MdHa/NchzWwsaDNPlhtG+wq6rzKRoLIVwIzdRWtOp6ah7D/DBRWpwJTC8s7x6WYryxUlqMcCQkR8qTIn2xVJdqcCI4QgrywlxZ+g8gQTzXGAqZFgAAAABJRU5ErkJggg=="

pihole_disconnected_image = "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyhpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuNi1jMTM4IDc5LjE1OTgyNCwgMjAxNi8wOS8xNC0wMTowOTowMSAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENDIDIwMTcgKE1hY2ludG9zaCkiIHhtcE1NOkluc3RhbmNlSUQ9InhtcC5paWQ6ODlFQTUzMDcwMDBEMTFFN0E0RENCMzkyNDkxNTY0OEEiIHhtcE1NOkRvY3VtZW50SUQ9InhtcC5kaWQ6ODlFQTUzMDgwMDBEMTFFN0E0RENCMzkyNDkxNTY0OEEiPiA8eG1wTU06RGVyaXZlZEZyb20gc3RSZWY6aW5zdGFuY2VJRD0ieG1wLmlpZDpDNkNBMTM5QzAwMDgxMUU3QTREQ0IzOTI0OTE1NjQ4QSIgc3RSZWY6ZG9jdW1lbnRJRD0ieG1wLmRpZDo4OUVBNTMwNjAwMEQxMUU3QTREQ0IzOTI0OTE1NjQ4QSIvPiA8L3JkZjpEZXNjcmlwdGlvbj4gPC9yZGY6UkRGPiA8L3g6eG1wbWV0YT4gPD94cGFja2V0IGVuZD0iciI/PpYHe+8AAALZSURBVHjaVJNNSJNxHMf/z/95pps2N90cU1C3qYdRm4faukRQWF4ECXqBJLsGEXTpEkSHgs51qJO3Xi5JGAhhQhB46larDjvYcHNO3QtuqHN7nvX5r01s8Nv/7fv7/r6/l0fT+E1PTxs+n68mhHghpbxts9necP304OBgI5vN6j09PaK7u9vkXczPz2vi2E/HtHA4LLu6uiz2IQiuYDFd1691dnYuYoV0Oi3AnHE6nd7x8fFcX1+fXFtbaxJI9VcsFpvspml+YCk1Go0SCnzYc3Ufj8dfsv8G8VV1Hh0d1dsKmgSrq6uNXC5nEHWD4z3MrUhYPb29vU9Y73AuYq8VPp/PW20ClY9mGIao1+tiZmZGer1eE6ILDofjEXm/rdVq19lXwD3OZDI/eJMotf5ToJztdrtQzqVSyQbgC843kH2eGgSQ/hvHX0tLSxpKj9fwHwFVF7Ozs41yuWy43e6ay+Xyo2oFu4VjEOkPKeTy5uamnSAWBZRHBEQRyBSFQkFS5frQ0FA/bfvEfZT3Gs4W+zr7i1NTUx9ZHcFg0Eomk9pRG6myFggELKT2VyqVz9hER0dHAgUu3u0QICCdJbX43t5ebHd3d2FkZKSWSCQ0Qw0JA9Nk29nZeXV4eDgBUKyvr1ej0egktRlMpVIFSBdJx0LRZQI9A36fdHXp9/u1WCxmbm1tnSCVsyolamIBPk0EC6KF7e1tD2enGpVW6udaAU1JTxvMgWSUVauS7dqgQk1cmZpMECkFeR4zLMsSkP1UIAoqDQjE8PBwMwXk3UXeCqBBCpoKhULvuQuPjY398Xg8KVrs4T3B3QOFp8UN9S1pXKhxlZFIxITwVLVaXWZc+4mgqzfFDUy1TkW+RFrZ1ghYUgHUJCpnWmMQKcG3Mcl9rjWpqo0K950CTyrn/f191T3raJTbwzQ3N9egRaozdZxODgwMvCPfCM5fgdyklRneDDD19iD9FWAA8mheUd+JxU0AAAAASUVORK5CYII="

try:
    url = pihole + "api.php"
    result = urllib2.urlopen(url, timeout = 5).read()
    json = json.loads(result)
    print "|image=" + pihole_connected_image
    print "---"
    print "Ads blocked:"
    print str(json['ads_blocked_today']) + "| href=" + pihole
    print "DNS queries:"
    print str(json['dns_queries_today']) + "| href=" + pihole
    print "Domain list size:"
    print str(json['domains_being_blocked']) + "| href=" + pihole

except:
    print "|image=" + pihole_disconnected_image
    print "---"
    print "Pi-Hole not found | color=red"
    print "Please update Pi-Hole location in plugin script"

print "---"
print "Refresh|refresh=true"
print "---"
