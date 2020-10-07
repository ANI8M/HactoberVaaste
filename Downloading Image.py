#downloading an image from internet
import urllib.request

#copy the url
url= "https://miro.medium.com/max/3840/1*qztFAmxwmPy9pzRYo6x0QQ.png"

download = urllib.request.urlretrieve(url, "img.png")
