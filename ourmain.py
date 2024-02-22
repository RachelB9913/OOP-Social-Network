from SocialNetwork import SocialNetwork


def main():
    # Creating the network
    print("The social network Twitter was created!")
    network = SocialNetwork("Twitter")
    print()

    print("***shouldn't creat new network **")
    network2 = SocialNetwork("Facebook")
    print()

    u1 = network.sign_up("Alice", "pass1")
    u2 = network.sign_up("Bob", "pass2")
    u3 = network.sign_up("Charlie", "pass3")
    u4 = network.sign_up("David", "pass4")
    u5 = network.sign_up("Eve", "pass5")

    print("Alice started following Bob")
    u1.follow(u2)
    print()

    print("Bob started following Alice")
    u2.follow(u1)
    print()
    print("Bob unfollowed Alice")
    u2.unfollow(u1)
    print()
    # cant unfollow yourself
    # print("error : ")
    # u2.unfollow(u2)
    print()
    # cant unfollow u3 if you are not follow u3
    # print("error :")
    # u2.unfollow(u3)
    print()

    print("Charlie disconnected")
    network.log_out("Charlie")
    print()
    # cant do follow if you are dis connected
    # print("error :")
    # u3.follow(u4)
    print()
    # you cand follow to user how is not connected
    print("Davide started following Charlie")
    u4.follow(u3)
    print()

    print("David started following Eve")
    u4.follow(u5)
    print()

    print("Charlie connected")
    network.log_in("Charlie", "pass3")
    print()
    p1= u1.publish_post("Text", "Hello World")
    print()

    p1.like(u1)
    p1.comment(u1, "hei this is me")
    p1.like(u2)
    p1.like(u2)
    print()
    print("this is p1 likes list")
    print("***make sure that Alice is in the list  && Bob not appear 2 times")
    # for like in p1.likes:
    #     print(like.get_name())

    print()
    p1.comment(u2, "hei this is BOb")
    p1.comment(u2, "hei this is BOb")
    print()
    print("this is p1 comments list")
    print("***make sure that Alice is in the list  && Bob appear 2 times")
    # for comment in p1.comments:
    #     print(comment)

    print()
    print("*** make sure that Alice is not in the list as like and as comment")
    u1.print_notifications()
    print()
    p2 = u3.publish_post("Sale", "Toyota prius 2012", 42000, "Haifa")
    #the pasword is not correct
    # print("error :")
    # p2.sold("pass")
    # print("error :")
    # p2.discount(15, "pass")
    # print(" *** if the toyota sold 2 times it is error")
    # print("sold")
    # p2.sold("pass3")
    # print()
    # print("error :")
    # p2.sold("pass3")

    # print("error :") # pasword to short
    # u7 = network.sign_up("Alice1", "p")

    # print("error :")  # pasword to long
    # u7 = network.sign_up("Alice1", "123456789123")
    print()
    network.log_out("Charlie")
    print()
    # print("error :")  # cant to discount when disconnected
    # p2.discount(15, "pass3")
    print()
    # print("error :")
    # p5 = u3.publish_post("Text", "try to trick you")
    print("error :")
    # p1.like(u3)
    print("error :")
    # p1.comment(u3, "i can't do nothing i am disconnected")
    print()

    p1.comment(u1, "you are not connected but i am")
    print("***Alice commente on your post should be in the note's")
    print()
    network.log_in("Charlie", "pass3")
    print()

    # print("error :")  # username taken
    # u7 = network.sign_up("Alice", "p12345")
    print()
    u2.follow(u5)
    u3.follow(u5)
    u1.follow(u5)
    # u1.follow(u5)
    print()
    print("***this is eve's followers make sure that Alice is there && only 1 time appear")
    for user in u5.get_followers_list():
        print(f"{user.get_username()}")
    print()

    u1.unfollow(u5)
    print("***this is eve's followers make sure that Alice is NOT there")
    for user in u5.get_followers_list():
        print(f"{user.get_username()}")
    print()
    u1.follow(u5)
    print("***this is eve's followers make sure that Alice is there && only 1 time appear")
    for user in u5.get_followers_list():
        print(f"{user.get_username()}")
    print()


if __name__ == '__main__':
    main()