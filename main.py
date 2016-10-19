import sys
import os
import json
import shutil
import time

def quiz_list():
  """Shows all available quizzes in the global library."""
  path = "Global_library"
  quizzes = os.listdir( path )
  for file in quizzes:
    fileExt = os.path.splitext(file)[-1]
    if fileExt == '.json':
      print file[:-5]


def myquiz_list():
  """ Displays a list of quizzes that the user has imported from the global library"""
  path = "My_library"
  quizzes = os.listdir( path )
  for file in quizzes:
    fileExt = os.path.splitext(file)[-1]
    if fileExt == '.json':
      print file[:-5]


def quiz_import(quiz_name):
  quiz_path = 'Global_library'
  shutil.copyfile(quiz_path + "/" + quiz_name + ".json", "My_library" + "/" + quiz_name + ".json")
  print """
    Loading.....
    The quiz has been copied to your library. 
    Have fun with it!!"""
  

def quiz_take(quiz_name):
  json_data = open("My_library" + "/" + quiz_name + ".json").read()

  counter = 0
  score = 0
  current_quiz =  json.loads(json_data)
  start_time = time.time()
  time_allocated = time.time() + 15

  all_questions = len(current_quiz.keys())
  done_questions = 0

  for key in current_quiz.keys():
    while time.time() < time_allocated:
      options = current_quiz[key]['options']
      counter += 1
      print str(counter) +".", current_quiz[key]['q_text']
      for key2 in sorted(options.keys()):
        print   "["+ key2.upper() +"]", options[key2]
      ans = raw_input('\nEnter your answer:').lower()
      while ans not in ['a','b', 'c', 'd']:
        ans = raw_input('\nwrong input. Try again:').lower()
      if ans == current_quiz[key]['is_answer']:
        print'Correct!'
        score += 5
        done_questions += 1
      else:
        print 'Wrong!'
      break  
          # elif ans != current_quiz[key]['is_answer']:
        
      
      
  final_score = score
  print "Time's Up!!"
  time.sleep(5)
  print 'All questions:' + str(all_questions)
  print 'Attempted questions:' + str(done_questions)
  print 'You scored: {0}'.format(score)
 
            


def main():
  print""" 

          Welcome to Quick Fire
          -----------------------
          Here are your options today

          1.quizlist - Gets a list of all quizzes in the global library
          2.quizimport - Imports a specific quiz from the library
          3.myquizlist - Displays the quizzes already imported
          4.quiztake <quiz name> - Begins the specific quiz 


          """


  option = raw_input('What would you like to do today?   ')

  if len(option) == 0:
    print 'No choice made'
    sys.exit(1)

  if option == 'quizlist':
    print """
    Here are the categories of quizzes available:

  """
    quiz_list()
  elif option == 'myquizlist':
    print """Here are the ready quizzes: 
----------------------------
            """
    myquiz_list()

  elif option == 'quizimport':
    option = raw_input('What category would you like to import?   ')
    quiz_import(option)

  elif option == 'quiztake':
    option = raw_input('Pick a category:')
    print """

    Loading....

    """
    quiz_take(option)
  else:
    print 'unknown option: ' + option
    sys.exit(1)

if __name__ == '__main__':
  main()