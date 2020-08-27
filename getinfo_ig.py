import urllib
from bs4 import BeautifulSoup

def get_description(instagram_user):

    url="https://www.instagram.com/"+instagram_user
    instagram_url = urllib.urlopen(url)
    soup = BeautifulSoup(instagram_url.read(),"html.parser")

    #finding meta desc with name = description
    for tags in soup.find_all('meta'):
        if tags.get('name') == "description":
            meta_description=tags.get('content')

    return meta_description

def number_of_followers(instagram_user):

    meta_description=get_description(instagram_user)

    #searching meta desc. for word "Followers"
    end = meta_description.find('Followers') - 1 
    followers = meta_description[:end]

    #returning number of followers on instagram_user account
    return followers

def number_of_following(instagram_user):

    meta_description=get_description(instagram_user)

    #searching meta desc. for word "Following"
    beginning = meta_description.find('Followers') + 11
    end = meta_description.find('Following') - 1
    following = meta_description[beginning:end]

    #returning number of following on instagram_user account
    return following

def number_of_posts(instagram_user):

    meta_description=get_description(instagram_user)

    #searching meta desc. for word "Posts"
    beginning = meta_description.find('Following') +11
    end = meta_description.find('Posts') - 1
    posts = meta_description[beginning:end]

    #returning number of posts on instagram_user account
    return posts
