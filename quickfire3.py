import sys
import os
import json
import shutil
import time
import pyfiglet
import cmd
import click
from termcolor import *
import colorama
import pyrebase

colorama.init()

config = {
  "apiKey": "AIzaSyDg_RSaaHrUDHDV9Scu9qy4SjfQrFhB9BM",
  "authDomain": "AIzaSyDg_RSaaHrUDHDV9Scu9qy4SjfQrFhB9BM",
  "databaseURL": "https://quick-fire.firebaseio.com",
  "storageBucket": "quick-fire.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()






clear = lambda: os.system('cls')


# My Styles
def yellow(string):
    return colored(string, 'yellow')
def cyan(string):
    return colored(string, 'cyan')
def green(string):
    return colored(string, 'green')
def blue(string):
    return colored(string, 'blue')
def red(string):
    return colored(string, 'red')

online_quizzes = {}

class Quizz(cmd.Cmd):
  prompt = click.style("quickfire>>", fg='white', bg='cyan', bold=True)
  

  def do_quiz_list(self):
    """Shows all available quizzes in the global library."""

    print cyan("""\n \t\t GLOBAL LIBRARY QUIZZES\n""")
    path = "Global_library"
    quizzes = os.listdir( path )
    for file in quizzes:
      fileExt = os.path.splitext(file)[-1]
      if fileExt == '.json':
        print  "\t\t" + yellow(file[:-5])
    print "\n"


  def do_myquiz_list(self):
    """ Displays a list of quizzes that the user has imported from the global library"""

    path = "My_library"
    quizzes = os.listdir( path )
    if not any(fname.endswith('.json') for fname in os.listdir(path)):
      print '\nThere are no quizzes in your library.\nImport from the global library.'
    else:
      print cyan("""\n \t\t MY LIBRARY QUIZZES\n""")
      for file in quizzes:
        fileExt = os.path.splitext(file)[-1]
        if fileExt == '.json':
          print  "\t\t" + yellow(file[:-5])
    print "\n"
  def do_quiz_import(self, quiz_name):
    """Imports a quiz from the global library to the user's library"""

    quiz_path = 'Global_library'
    shutil.copyfile(quiz_path + "/" + quiz_name + ".json", "My_library" + "/" + quiz_name + ".json")
    print blue('\n\t\tLoading.....\n')
      
    time.sleep(4)
    print cyan("\tThe quiz has been copied to your library.\n\tHave fun with it!!")
    

  def do_quiz_take(self, quiz_name):
    """Enables the user to take a quiz of his choice from My_library. The quiz is timed and a summary is given at the end"""
    print green('\t\tQUIZ NAME: '  + quiz_name.upper()+ '\n')

    json_data = open("My_library" + "/" + quiz_name + ".json").read()

    counter = 0
    score = 0
    current_quiz =  json.loads(json_data)
    start_time = time.time()
    time_allocated = time.time() + 18

    all_questions = len(current_quiz.keys())
    done_questions = 0

    for key in current_quiz.keys():
      if time.time() > time_allocated:
          print red("\t\tTime's Up!!")
      while time.time() < time_allocated:
         
        options = current_quiz[key]['options']
        counter += 1
        print cyan('\t'+ str(counter) +"."), cyan(current_quiz[key]['q_text']) 
        
        for key2 in sorted(options.keys()):
          print   yellow("\t["+ key2.upper() +"]"), yellow(options[key2])
          
        ans = raw_input('\nEnter your answer:').lower()
        while ans not in ['a','b', 'c', 'd']:
          ans = raw_input(red('\n\twrong input. Try again:')).lower()
        done_questions += 1
        if ans == current_quiz[key]['is_answer']:
          print green('\tCorrect!\n')
          score += 5
          time.sleep(2)
        else:
          print red('\tWrong!\n')
          time.sleep(2)
        break  
          
          
    score = (score/(3.0*5))*100
    
    print cyan('\n\t SCORE:\n')
    print yellow('\tAll questions:') + green('\t\t'+str(all_questions))
    print yellow('\tAttempted questions:')  + green('\t'+str(done_questions))
    print yellow('\tYour score:') + green('\t\t'+str(round(score,2))+ '%') 
       
  def do_list_online_quizzes(self):

    """Lists the quizzes available in online in Firebase"""

    print blue('\n\t\tLoading.....\n')
    try:
      all_online_quizzes = db.child("quizzes").get()
      print cyan('\t\tONLINE QUIZZES')
      for quiz in all_online_quizzes.each():
        print "\t %s" % (quiz.key())
        online_quizzes[quiz.key()] = quiz.val()
    except:
      print red("\tThere are no quizzes in the Online Repository\n")
    quick_fire_bridge()

  def do_import_online_quiz(self):

    """Downloads a quiz of choice from the online repository to the user's My_library"""

    
    quiz_path = 'My_library'
    option = raw_input(green('\n\tWhich quiz would you like to import? '))
    online_quiz = dict(db.child("quizzes").child(option).get().val())
    try:
      with open(quiz_path + '/' + option + '.json', 'w') as our_saved_quiz:
        json.dump(online_quiz, our_saved_quiz)
      print green('\n\tThe quiz has been downloaded to your local library.\n\tHave fun with it!!')
    except:
      print red('\t No Internet Connection')
    quick_fire_bridge()  

  def do_upload_quiz(self, quiz_name):

    """Uploads a quiz of choice from the user's My_library to the online repository"""
    try:
      with open('My_library/' + quiz_name + '.json', 'r') as our_saved_quiz:
        our_saved_quiz_dict = json.loads(our_saved_quiz.read())
        data = {quiz_name: our_saved_quiz_dict}
        db.child("quizzes").child(quiz_name).update(our_saved_quiz_dict)
        print green("\tThe %s quiz has been uploaded successfuly. List online quizzes to confirm") % quiz_name
    except:
      print red('\t No Internet Connection')
    quick_fire_bridge()

  def do_EOF(self, line):
    return True



quick_fire = Quizz()

def quick_fire_bridge():

  """Allows for interaction between the program and the user"""

  option = raw_input(green('\n\n\tWhat else would you like to do? '))
  if len(option) == 0:
    print red('\tNo choice made')
  else:
    main(option)
def help():
  print green('\n\tHere are your options.')

  print(yellow(""" 

            Welcome to Quick Fire
            -----------------------
            Here are your options today

            1. quizlist - Gets a list of all quizzes in the global library
            2. quizimport - Imports a specific quiz from the library
            3. myquizlist - Displays the quizzes already imported
            4. quiztake <quiz name> - Begins the specific quiz
            5. listonlinequizzes - List all quizzes fro the Online Repository
            6. importonlinequiz <quiz name> - 
            7. uploadquizonline <quiz name> - 
            8. help - To view this menu again for a list of commands

            """))
  quick_fire_bridge()


def main(option=None):
 

  if option == None:
    pyfiglet.print_figlet("Quick Fire",'slant')

    print(yellow(""" 

            Welcome to Quick Fire
            -----------------------
            Here are your options today

            1. quizlist - Gets a list of all quizzes in the global library
            2. quizimport - Imports a specific quiz from the library
            3. myquizlist - Displays the quizzes already imported
            4. quiztake <quiz name> - Begins the specific quiz
            5. listonlinequizzes - List all quizzes fro the Online Repository
            6. importonlinequiz <quiz name> - 
            7. uploadquizonline <quiz name> - 
            8. help - To view this menu again for a list of commands

            """))

    option = raw_input(green('\tWhat would you like to do today? '))
  try:
    if len(option) == 0:
        print 'No choice made'
        sys.exit(1)
    if option == 'quizlist':
      quick_fire.do_quiz_list()
      quick_fire_bridge()
    elif option == 'myquizlist':
        quick_fire.do_myquiz_list()
        quick_fire_bridge()
    elif option == 'quizimport':
      print green("\n\tHere is a list of available quizzes from the Global Library.\n")
      quick_fire.do_quiz_list()
      option = raw_input(green('\n\tWhich quiz would you like to import?'))
      quick_fire.do_quiz_import(option)
      quick_fire_bridge()

    elif option == 'quiztake':
      quick_fire.do_myquiz_list()
      option = raw_input(green('\tPick a quiz: '))
      print blue('\n\t\tLoading.....\n')
      quick_fire.do_quiz_take(option)
      quick_fire_bridge()

    elif option == 'listonlinequizzes':
      quick_fire.do_list_online_quizzes()
    elif option == 'importonlinequiz':
      quick_fire.do_import_online_quiz()
      print blue('\n\t\tLoading.....\n')
    elif option == 'uploadquizonline':
      print green("\n\tHere is a list of available quizzes from your local Library.\n")
      quick_fire.do_myquiz_list()
      option = raw_input(green('\n\tWhich quiz would you like to upload? '))
      print blue('\n\t\tLoading.....\n')
      quick_fire.do_upload_quiz(option)
    elif option == 'help':
      help()
  except:
    print red('unknown option: \n') + option
    sys.exit(1)


clear()
main()





if __name__ == '__main__':
  Quizz().cmdloop()