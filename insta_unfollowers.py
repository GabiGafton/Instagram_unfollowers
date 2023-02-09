import re

with open('followers.html', 'r') as file:
    text = file.read()
    #select all follower users
    followers = re.findall(r"(https:\/\/www\.instagram\.com/[a-z0-9._-]+)", text)
    followers_list = []
    for user in followers:
        followers_list.append(user)

# print(followers_list)
print("Number of people that follow me: {}\n------------------------------------".format(len(followers_list)))


with open('following.html', 'r') as file:
    text = file.read()
    #select all following users
    following = re.findall(r"(https:\/\/www\.instagram\.com/[a-z0-9._-]+)", text)
    following_list = []
    for user in following:
        following_list.append(user)

# print(following_list)
print("Number of people that I follow: {}\n------------------------------------".format(len(following_list)))

print("Number of people that don't follow me back: {}\n------------------------------------".format(len(set(following_list)-set(followers_list))))

print("List of people that don't follow me back: \n")
print(list(set(following_list)-set(followers_list)))

with open("list_of_unfollowers.txt", "w") as output:
    for user in list(set(following_list)-set(followers_list)):
        output.write(user+"\n")
