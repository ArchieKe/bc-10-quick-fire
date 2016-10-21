
###BC-10-Quick_Fire

A project done in fullfillment of the application process for Andela Cohort 10

This is a quiz console application that presents a quiz to a user and a score is generated at the end of the quiz

##The required commands for the application were:

1.When a user takes a quiz he gets a score based on the answers he got right

2.Timing can be added to quiz as a parameter in the JSON

3.As a user I can import quizzes from JSON files

4.Add in an online quiz repository using Firebase (extra credit)

5.List all the online quizzes

6.Download a quiz to your library

7.Publish a local quiz to the online library

#JSON Format for Quizzzes should contain the following keys:
1.questions - List of questions in the quiz

2.text - Question text

3.options - List of options for the question

4..is_answer - Parameter of an option that can be true or false. Indicates whether or not that option is the correct answer.

5.quiz take <quiz_name> - Start taking a new quiz

##Installation.

To be able to get this project to your local machine

1.First git clone this project at https://github.com/ArchieKe/bc-10-quick-fire/tree/master
2.Navigate to the bc-10-quick-fire folder.

3.Create a virtual environment using the virtualenv command and activate it.

4.Install the requirements via pip install -r requirements.txt

5.Run the application in your terminal via python quickfire3.py

##Bugs

A few hickups were encountered.
1.The program terminates when an unknown option is given.
2. The timer does not work perfectly

##Resources
Firebase
