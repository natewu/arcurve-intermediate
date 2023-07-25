"""
Arcurve TechTips - Tech Event Intermediate Workshop
July 27th, 2023
Concept based on uAlberta database course work
"""
import sqlite3

# sets up the connection to the database so that we can interact with and manipulate it
PATH = "./database.db"
connection = sqlite3.connect(PATH)
cursor = connection.cursor()

# a function for python program to connect to the database at the given PATH
def connect(path):
    global connection, cursor

    connection = sqlite3.connect(path)
    cursor = connection.cursor()
    cursor.execute(" PRAGMA foreign_keys=ON; ")
    connection.commit()
    return


# simple menu function
def menuOptionSelect():
    print("Welcome to the program")
    while (True):
        # display menu and user options
        menuStr = (
            "\n\nMain Menu\n"
            "1. Find IDs of papers whose ratings is greater than 4.0\n"
            "2. Find titles of papers whose ratings is greater than 4.0\n"
            "3. Find papers matching a user-inputted area\n"
            "4. Find reviewers who have reviewed 2 or more different papers\n"
            "5. Find the top 5 papers that have the highest average rating ordered alphabetically and ascending\n"
            "6. Exit\n"
            "Please select an option: "
        )

        # retrieve valid user input and switch tasks
        userOption = int(input(menuStr))
        if userOption == 1:
            queryOne()

        elif userOption == 2:
            queryTwo()

        elif userOption == 3:
            queryThree()

        elif userOption == 4:
            queryFour()

        elif userOption == 5:
            queryFive()

        elif userOption == 6:
            print("Thanks! Exiting the system...")
            return

        else:
            print("\nInvalid entry")
            menuOptionSelect()

# Here is an example query being used inside a python function
def exampleQuery():
    userEmail = "example@example.com"

    cursor.execute("""
        SELECT title
        FROM Papers
        WHERE id IN (
            SELECT paper
            FROM Reviews
            WHERE Reviewer=:userEmail
        );
    """, {"userEmail": userEmail})

    rows = cursor.fetchall()

    if len(rows):
        print("\nPapers Assigned to user {email}:".format(email=userEmail))
        for row in rows:
            print(row[0])
    else:
        print("\nThere are no papers assigned to user {email}".format(email=userEmail))


# Your task in this query is to retrieve the IDs of all papers whose overall rating is greater than 4.0
# make sure there are no repetitions
def queryOne():
    # write your query here
    cursor.execute(("""

    """))

    rows = cursor.fetchall()

    if len(rows):
        print("\nIDs of Papers with High Ratings:")
        for row in rows:
            print(row[0])
    else:
        print("\nThere are no papers with high ratings.")


# Your task in this query is to retrieve the titles of all papers whose overall rating is greater than 4.0
# make sure there are no repetitions
def queryTwo():
    # write your query here
    cursor.execute(("""
        
    """))

    rows = cursor.fetchall()

    if len(rows):
        print("\nTitles of Papers with High Ratings:")
        for row in rows:
            print(row[0])
    else:
        print("\nThere are no papers with high ratings.")


# Your task in this query is to retrieve the titles and authors of all papers matching a user-inputted area
# Areas in the database include: DB, SE, AI, DM
def queryThree():
    userArea = input("\nEnter the area: ")

    # write your query here
    cursor.execute(("""
        
    """))

    rows = cursor.fetchall()

    if len(rows):
        print("\nPapers and author in Area {area}:".format(area=userArea))
        for row in rows:
            print(row[0], "by", row[1])
    else:
        print("\nThere are no papers in Area {area}:".format(area=userArea))


# Your task in this query is to retrieve the reviewers and how many papers they have reviewed, only if it is 2 or more papers
def queryFour():
    # write your query here
    cursor.execute(("""
        
    """))

    rows = cursor.fetchall()

    if len(rows):
        print("\nReviewers who have reviewed multiple papers:")
        for row in rows:
            print(row[0], "with", row[1], "papers")
    else:
        print("\nThere are no reviewers who have reviewed multiple papers.")


# Your task in this query is to retrieve the titles of the top 5 papers (highest overall average rating) ordered ascending alphabetically
def queryFive():
    # write your query here
    cursor.execute(("""
        
    """))

    rows = cursor.fetchall()

    if len(rows):
        print("\nTop 5 Papers with Highest Average Rating (Ordered Alphabetically if Tied):")
        for row in rows:
            print(row[0])
    else:
        print("\nNo papers found.")


# main function
def main():
    """
    Main function
    """
    # setup DB connection
    global connection, cursor

    # display menu
    print("Welcome to your database")
    menuOptionSelect()

    # disconnect from DB
    connection.commit()
    connection.close()
    return 0


if __name__ == "__main__":
    main()
    