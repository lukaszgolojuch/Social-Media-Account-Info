from bs4 import BeautifulSoup
import requests
import urllib

#on this module we get info about twitter profile

def number_of_followers(twitter_user):
    #find number of followers on twitter account and return it
    url="https://mobile.twitter.com/"+twitter_user+"/followers"
    twitter_url = urllib.urlopen(url)
    soup = BeautifulSoup(twitter_url.read(),"html.parser")

    try:
        followers = soup.find('span', class_ = 'count').get_text()
        return followers
    except:
        return 'Account name not found...'

def number_of_following(twitter_user):
    #find number of following on twitter account and return it
    url="https://mobile.twitter.com/"+twitter_user+"/following"
    twitter_url = urllib.urlopen(url)
    soup = BeautifulSoup(twitter_url.read(),"html.parser")
    
    try:
        following = soup.find('span', class_ = 'count').get_text()
        return following
    except:
        return 'Account name not found...'
