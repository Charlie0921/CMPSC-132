def intro_message(count):
  if count > 0:
    print('I am a recursive function')
    intro_message(count-1)
  else:
    print('End of recursion')
