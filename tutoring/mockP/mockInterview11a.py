
class MyFile():
  def __init__(self, name, parent):
    self.name = name
    self.parent = parent
  
  def __repr__(self):
    return f"'{self.name}'"
    
class MyFolder():
  def __init__(self, name, parent):
    self.name = name
    self.contents = []
    self.parent = parent
  
  def ls(self):
    # prints all files and folder names in directory (array)
    for file in self.contents:
      print(file.name)
  
  def __repr__(self):
    return f"'{self.name}'"

class DummyLinux():
  def __init__(self):
    # self.root.contents -> []
    self.root = MyFolder('root', None)
    self.working_directory = self.root
  
  def cd(self, arg):
    # traverses to folder (selects folder from array)
    if arg == "..":
      # going back one folder
      self.working_directory = self.working_directory.parent
    else:
      commands = arg.split("/")
      for command in commands: # -> unavoidable
        # if command in self.working_directory.contents:
        for data in self.working_directory.contents: 
          # -> how to remove? dictionary
          # root.contents = {
            # "sample": MyFolder(...),
              # "test_folder": ,
              # "asdf_folder": ,
          # }
          # root.contents["sample_file"]
          if command == data.name:
            self.working_directory = data
            break
        else:
          print(f"file or folder not found with name: {command}")
          return
          
# ['sample2']
    
  
    
    
mr_linus = DummyLinux()
mr_linus.root.contents.append(MyFolder('test_folder', mr_linus.root))
mr_linus.root.contents.append(MyFolder('asdf_folder', mr_linus.root))
mr_linus.root.contents.append(MyFolder('sample', mr_linus.root))
sample_folder = mr_linus.root.contents[0]
sample_folder.contents.append(MyFile('sample_file', sample_folder))
sample_folder.contents.append(MyFile('sample_file2', sample_folder))
sample_folder.contents.append(MyFile('sample_file3', sample_folder))

mr_linus.working_directory.ls()
print(mr_linus.working_directory)
mr_linus.cd('sample')
print(mr_linus.working_directory)
mr_linus.cd('..')

'''
# root
#   sample
#     test_folder
#       test_file2
#       test_file3
#     sample_file
#     sample_file2
#     sample_file3
    
  # nesting? how does this work?
  # cd sample/test_folder/abcfolder/xyzfolder
  # split + use length
  wd - > root
  ['sample']
  
  cd ..
  '''

# sample_file
# sample_file2
# sample_file3


