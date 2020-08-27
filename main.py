import getinfo_ig #get info about followers/following/posts on Instagram
import getinfo_tw #get info about followers/following on Twitter
import getinfo_fb #get info about number of likes on facebook
import sys
import os

def ig_link_generator():
    print("--------------------------------------------------------------------")
    #generating link for instagram account and return it
    instagram_user=raw_input("[*] Name of instagram user: ")
    return instagram_user

def fb_link_generator():
    print("--------------------------------------------------------------------")
    #generating link for facebook account and return it
    facebook_user=raw_input("[*] Name of facebook fanpage: ")
    return facebook_user

def tw_link_generator():
    print("--------------------------------------------------------------------")
    #generating link for twitter account and return it
    twitter_user=raw_input("[*] Name of twitter profile: ")
    print("--------------------------------------------------------------------")
    return twitter_user

def main():

    print("--------------------------------------------------------------------")
    #we get name of user 
    print("Hello " + os.getlogin())
    print("We will need some info about you: ")

    instagram_user = ig_link_generator() #get instagram user name
    facebook_user = fb_link_generator() #get facebook user name
    twitter_user = tw_link_generator() #get twitter user name

    print("MENU")
    print("1. Check actual number of followers, following and number of posts")
    print("2. Exit")
    print("--------------------------------------------------------------------")
    answ = input("[*] Your choice: ")

    #if/elif for main menu
    if answ == 1:
        print("\n[*] Processing... \n")
        
        followers_number_ig = getinfo_ig.number_of_followers(instagram_user) #followers on ig
        following_number_ig = getinfo_ig.number_of_following(instagram_user) #following on ig
        posts_number_ig = getinfo_ig.number_of_posts(instagram_user) #number of posts on ig

        likes_fb = getinfo_fb.number_of_likes(facebook_user) #number of likes on fb page

        followers_number_tw = getinfo_tw.number_of_followers(twitter_user) #number of followers on twitter
        following_number_tw = getinfo_tw.number_of_following(twitter_user) #number of following on twitter

        #print all output data about accounts
        print("--------------------------------------------------------------------")
        #instagram account
        print("INSTAGRAM")
        print("Account name: " + instagram_user)
        print("Followers number: " + followers_number_ig)
        print("Following number: " + following_number_ig)
        print("Number of posts " + posts_number_ig)
        print("--------------------------------------------------------------------")

        #facebook account
        print("FACEBOOK")
        print("Account name: " + facebook_user)
        print("Number of likes: " + likes_fb)
        print("--------------------------------------------------------------------")

        #twitter account
        print("TWITTER")
        print("Account name: " + twitter_user)
        print("Followers number: " + followers_number_tw)
        print("Following number: " + following_number_tw)
        print("--------------------------------------------------------------------")

        main()

    elif answ == 2:
        #exit app
        print("Thank you for using my app...")
        os.sys.exit()
    else:
        #wrong input... other than 1/2
        print("Wrong input try again... ")
        main()

if __name__ == "__main__":
    print("\nWelcome in program...")
    main()

    