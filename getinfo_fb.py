import urllib
from bs4 import BeautifulSoup

#On this module we are looking for number of like on fb fanpage 

def number_of_likes(facebook_user):
    #find number of likes and return it
    url = 'https://www.facebook.com/'+ facebook_user
    twitter_url = urllib.urlopen(url)
    soup = BeautifulSoup(twitter_url.read(),"html.parser")

    try:
        #find div with number of likes
        f = soup.find('div', attrs={'class': '_4-u3 _5sqi _5sqk'})
        likes=f.find('span',attrs={'class':'_52id _50f5 _50f7'}) #finding span tag inside class
        return likes.text
    except:
        return 'Account name not found...'