#判断括号的使用
def validBraces(string):
  if string.count('(') !=string.count(')') or string.count('[') != string.count(']') or string.count('{') != string.count('}') or string == "":
      return False
  if len(string) == 2:
      if (string[0] == '(' and string[1] == ')') or (string[0] == '[' and string[1] == ']') or (string[0] == '{' and string[1] == '}'):
          return True
      
  a = ' '.join(string)
  lst = a.split()
  a1 = []
  a2 = []
  
  b1 = []
  b2 = []
  
  c1 = []
  c2 = []
  
  for i in range(0,lst.count('(')):
      a1.append(lst.index('('))
      a2.append(lst.index(')'))
      lst.remove('(')
      lst.remove(')')
  
  for i in range(0,lst.count('[')):
      b1.append(lst.index('['))
      b2.append(lst.index(']'))
      lst.remove('[')
      lst.remove(']')
  
  for i in range(0,lst.count('{')):
      c1.append(lst.index('{'))
      c2.append(lst.index('}'))
      lst.remove('{')
      lst.remove('}')
      
  if a1 < a2 and b1 < b2 and c1 < c2:
      return True
      
  else:
      return False
      
      
#codewars:
def validBraces(s):
  while '{}' in s or '()' in s or '[]' in s:
      s=s.replace('{}','')
      s=s.replace('[]','')
      s=s.replace('()','')
  return s==''
#如果使用正确 必然有一组相邻！