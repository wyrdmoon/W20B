import mariadb
import dbcreds

print("WELCOME TO HACKER TOWN")
username = input("enter a cool username: ")
password = input("enter a hard to crack password: ")

conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, port=dbcreds.port, host=dbcreds.host, database=dbcreds.database)
cursor = conn.cursor()

cursor.execute("SELECT * FROM hackers WHERE alias =?",[username,])
user = cursor.fetchone()
if user:

    if password == user[2]:
        print("you are logged in")
    while 1:
        print("Please choose: ")
        print("1 add a new exploit")
        print("2 view my exploits")
        print("3 view others exploits")
        print("4 exit")
        option = input("choose")
        if option =="1":
            content = input("Enter the exploit: ")
            cursor.execute("INSERT INTO exploits (content, user_id)VALUES(?,?)",[content, user[0]])
            conn.commit()
            print("exploit is added successfully")
        elif option =="2":
            cursor.execute("SELECT * FROM exploits e INNER JOIN WHERE hackers h ON e.user_id =h.id ?",[user[0],])
            print("after query")
            posts = cursor.fetchall()
            print(posts)
            for post in posts:
                print("exploits id:" + str(post[0]))
                print("content: " +post[1])
                print("------------------") 
                
        elif option == "3":    
            cursor.execute("SELECT * FROM exploits  INNER JOIN hackers ON WHERE user_id != ?",[user[0],])
            print("after query")
            posts = cursor.fetchall()
            print(posts)
            for post in posts:
                print("alias:" + post[4])
                print("content: " +post[1])
                print("------------------") 
        elif option =="4":
            print("gtfo n00b")
            break
        else:
            print("invalid entry") 
            
else: 
    print("you can do better than that")               
                   
print(user)
cursor.close()
conn.close()