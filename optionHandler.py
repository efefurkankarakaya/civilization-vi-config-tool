params = { 'uiUpscaling': 'UIUpscale' }

def readOptionsFile(source):
  content = ""
  with open(source, 'r', encoding="utf-8") as txt:
      content = txt.readlines()
  return content

def updateOption(content, key, value):
  updatedOne = ""
  for index, line in enumerate(content):
      if key in line:
          [currentKey, currentValue] = line.split(' ') # TODO: No longer necessary
          print(f'{currentKey=} {currentValue=}')
          content[index] = f"{key} {value}\n"
          updatedOne = content[index]
  return updatedOne

def saveOptions(content, destination):
   merged = "".join(content)
   with open(destination, 'w', encoding="utf-8") as txt:
      txt.write(merged)

# content = readOptionsFile()
# updatedOne = updateOption(content, params['enableSubtitle'], 13)
# saveOptions(content)

# print(updatedOne)
# print(content)