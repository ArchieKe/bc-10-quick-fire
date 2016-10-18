import sys
import os
import json
import shutil

def quiz_list():
  """Shows all available quizzes in the global library."""
  path = "Global_library"
  quizzes = os.listdir( path )

# This would print all the files and directories
  for file in quizzes:
    fileExt = os.path.splitext(file)[-1]
    if fileExt == '.json':
      print file[:-5]

def myquiz_list():
  """ Displays a list of quizzes that the user has imported from the global library"""
  path = "My_library"
  quizzes = os.listdir( path )

# This would print all the files and directories
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
  current_quiz =  json.loads(json_data)
 
  for key in current_quiz.keys():
    options = current_quiz[key]['options']
    counter += 1
    print str(counter) +".", current_quiz[key]['q_text']
    for key2 in sorted(options.keys()):
      print   "["+ key2.upper() +"]", options[key2]
    ans = raw_input('\nEnter your answer:')
    print

            

    

    



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
    # quiz_name = option
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