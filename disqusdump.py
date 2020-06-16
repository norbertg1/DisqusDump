from disqusapi import DisqusAPI
import time
import sys
from datetime import datetime
import config

most_likes = 100
limit_nr = 100 #lekerdezett posztok száma
top_replies_nr = 100
disqus = DisqusAPI(config.secret_key, config.public_key)
listPosts_results=[]

user = ""
username="username:" + user


f = open(user, "w")

class CountLikesDislikes:
    def __init__ (self):
        time.sleep(0.1)
        self.likes = {}
        self.dislikes = {}
        while True:
            try:
                post=disqus(method='GET', endpoint="users/listPosts", user=username, limit = 1, cursor="")[0]
                break
            except:
                except_handler(sys.exc_info()[0])
        for x in range (0, most_likes):
            self.likes[x] = post
            self.dislikes[x] = post

    def update(self, key):
        #↓↓↓↓↓ update likes ↓↓↓↓↓
        for x in range (0, most_likes):
            if key.get("likes") > self.likes[x].get("likes"):
                self.likes[x] = key
                break
        #↓↓↓↓↓ update dislikes ↓↓↓↓↓
        for x in range (0, most_likes):    
            if key.get("dislikes") > self.dislikes[x].get("likes"):
                self.dislikes[x] = key
                break

    def write_to_file(self, f):
        s = "\n\n\n Most likes:\n"
        for x in range (0, most_likes):
            while True:
                try:
                    thread = disqus(method='GET', endpoint="threads/details", thread=self.likes[x].get("thread"))
                    break
                except:
                    except_handler(sys.exc_info()[0])
            s += (self.likes[x].get("createdAt")).encode('utf-8') + " likes: " + str(self.likes[x].get("likes")) + " dislikes: " + str(self.likes[x].get(" dislikes ")) + "\n" + (self.likes[x].get("raw_message")).encode('utf-8') + "\nThread: " +str(self.likes[x].get("thread"))+"\n" + (thread.get("clean_title")).encode('utf-8') + thread.get("link").encode('utf-8') + "\n"
            s += "\n-----------------------------------\n"
        s += " \n\n Most dislikes:\n"
        for x in range (0, most_likes):
            while True:
                try:
                    thread = disqus(method='GET', endpoint="threads/details", thread=self.dislikes[x].get("thread"))
                    break
                except:
                    except_handler(sys.exc_info()[0])            
            s += (self.dislikes[x].get("createdAt")).encode('utf-8') + " likes: " + str(self.dislikes[x].get("likes")) + " dislikes: " + str(self.dislikes[x].get(" dislikes ")) + "\n" + (self.dislikes[x].get("raw_message")).encode('utf-8') + "\nThread: " +str(self.dislikes[x].get("thread")) +"\n" + (thread.get("clean_title")).encode('utf-8') + thread.get("link").encode('utf-8') + "\n"
            s += "\n-----------------------------------\n"
        f.write(s)
        
    def __getitem__(self, key):
        return self.likes[key]

    def __getitem__(self, key):
        return self.dislikes[key]
    
    def __setitem__(self, key, value):
        self.likes[key] = value

    def __setitem__(self, key, value):
        self.dislikes[key] = value

class CountReplies:
    def __init__ (self):
        self.users = {}

    def update(self, user):
        if (self.users.has_key(user)):
            self.users[user] = self.users[user]+1
        else:
            self.users[user]=1

    def write_to_file(self, f):
        a=sorted(self.users.items(), key=lambda x: x[1], reverse=True)
        s = "\n\nMost replies:\n"
        lenght=top_replies_nr
        if lenght < len(self.users.items()):
            for x in range(lenght):
                s += a[x][0].encode('utf-8') + " " + str(a[x][1]) + "\n"
        else:
            for x in range(len(self.users.items())):
                s += a[x][0].encode('utf-8') + " " + str(a[x][1]) + "\n"
            print s
        f.write(s)

class CheckEnd:
    def __init__ (self):
        self.cursor=""
        
    def check_end(self, cursor):
        if cursor == self.cursor:
            return 1
        self.cursor=cursor
        return 0

class CountDateTime:
    def __init__ (self):
        time.sleep(0.1)
        while True:
            try:
                t = disqus(method='GET', endpoint="users/listPosts", user=username, limit = 1, cursor="")[0].get("createdAt")
                break
            except:
                except_handler(sys.exc_info()[0])
        t = datetime.strptime(t, '%Y-%m-%dT%H:%M:%S')
        t = utc2local(t)
        t = datetime.strptime(str(t.year) + str(t.month), '%Y%m')
        self.count_months = {t:0}
        self.count_hours = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0,17:0,18:0,19:0,20:0,21:0,22:0,23:0}
        self.count_weekdays = {1:0,2:0,3:0,4:0,5:0,6:0,7:0}

    def update(self, t):
        t = datetime.strptime(t, '%Y-%m-%dT%H:%M:%S')
        t = utc2local(t)
        self.count_hours[t.hour] = self.count_hours[t.hour] + 1
        self.count_weekdays[t.isoweekday()] = self.count_weekdays[t.isoweekday()] + 1
        if self.count_months.has_key(datetime.strptime(str(t.year) + str(t.month), '%Y%m')):
            self.count_months[datetime.strptime(str(t.year) + str(t.month), '%Y%m')] = self.count_months[datetime.strptime(str(t.year) + str(t.month), '%Y%m')] +1
        else:
            self.count_months[datetime.strptime(str(t.year) + str(t.month), '%Y%m')]=1

    def write_to_file(self, f):
        s = "\n\nHour_occurance:\n"
        for item in self.count_hours:
            s += str(item) + "," + str(self.count_hours[item]) + "\n"
        s += "\n\nWeekday_occurance:\n"
        for item in self.count_weekdays:
            s += str(item) + "," + str(self.count_weekdays[item]) + "\n"
        s +="\n\nMonth occurance:\n"
        for item in self.count_months:
            s += str(item.year) + "-" + str(item.month)  + " , " + str(self.count_months[item]) + "\n"
        s +="\n\nMonth occurance with day 1.:\n"
        for item in self.count_months:
            s += str(item.year) + "-" + str(item.month) + "-1" + " , " + str(self.count_months[item]) + "\n"
        f.write(s)

    def __getitem__(self, key):
        return self.count_months[key]

class AverageChars:
    def __init__ (self):
        self.total_chars = 0
        self.messages_num = 0

    def update(self, message):
        self.messages_num = self.messages_num + 1
        self.total_chars = self.total_chars + len(message)

    def write_to_file(self, f):
        avarage = self.total_chars/self.messages_num 
        s = "\n\n\n Total characters:\n"
        s += str(self.total_chars)
        s += "\nMessages number:\n"
        s += str(self.messages_num)
        s += "\nAvarage characters:\n"
        s += str(avarage)
        f.write(s)

def utc2local (utc):
    epoch = time.mktime(utc.timetuple())
    offset = datetime.fromtimestamp (epoch) - datetime.utcfromtimestamp (epoch)
    return utc + offset

def except_handler(error):
        print error
        print(datetime.now())
        print "error, entering sleep"
        time.sleep(1)

#Ha alul kikommentezem a thread sort akkor lehivasonként 100 üzenetet tudok elmenteni. Ha nincs kikommentezve a plussz infók üzenetenként egy két lehivasba kerülnek
thread = 0
time_occurrences=CountDateTime()
likesdislikes=CountLikesDislikes()
replies=CountReplies()
end=CheckEnd()
Avarage=AverageChars()
while True:
    try:
        i=0
        while True:
            listPosts = disqus(method='GET', endpoint="users/listPosts", user=username, limit = limit_nr, cursor = end.cursor)
            if (len(listPosts) == limit_nr) or listPosts.cursor["hasNext"] == "False" or i>5:
                break
            else:
                print ("listPosts length shorter thank exected:", len(listPosts))
                i=i+1
        listPosts_results.append(len(listPosts))
        if end.check_end(listPosts.cursor["next"]):
            break
        for key in listPosts:
            likesdislikes.update(key)
            time_occurrences.update(key.get("createdAt"))
            Avarage.update(key.get("raw_message"))
            #↓↓↓↓↓ egyutt kommentelni ↓↓↓↓↓
            thread = disqus(method='GET', endpoint="threads/details", thread=key.get("thread"))    #Ha ez nincs kikommentevel akkor plussz infók mentődnek el de két lehívásba kerül üzenetenként
            s = (key.get("createdAt")).encode('utf-8') + " likes: " + str(key.get("likes")) + " dislikes: " + str(key.get(" dislikes ")) + "\n" + (key.get("raw_message")).encode('utf-8') + "\nThread: " +str(key.get("thread")) +"\n" + (thread.get("clean_title")).encode('utf-8') + thread.get("link").encode('utf-8') + "\n"
            #↑↑↑↑↑ egyutt kommentelni ↑↑↑↑↑
            #s = (key.get("createdAt")).encode('utf-8') + " likes: " + str(key.get("likes")) + " dislikes: " + str(key.get(" dislikes ")) + "\n" + (key.get("raw_message")).encode('utf-8') + "\nThread: " +str(key.get("thread"))
            if(key.get("parent") and thread):   #ez csak akkor futattódik le ha a thread sor kettővel fejebb nincs kikommentelve és valasz postról van szó
                post = disqus(method='GET', endpoint="posts/details", post=key.get("parent"))
                if post.get("author").has_key("username"):
                    s += str(post.get("author")["username"]) +"\n"
                s += (post.get("author")["name"]).encode('utf-8') + "\n"
                replies.update((post.get("author")["name"]))
            s += "\n-----------------------------------\n"
            f.write(s)
        time.sleep(0.1)
        print listPosts.cursor["next"]
        print listPosts[0].get("createdAt")
        print len(listPosts)
    except KeyboardInterrupt:
        time.sleep(1)
        break
    except:
        except_handler(sys.exc_info()[0])

replies.write_to_file(f)
likesdislikes.write_to_file(f)
time_occurrences.write_to_file(f)
Avarage.write_to_file(f)
f.write(str(listPosts_results))
f.close()
time.sleep(1)
while(1):
    print "end of program... sleeping"
    time.sleep(3600)
