# longest-absolute-file-path
# https://leetcode.com/problems/longest-absolute-file-path/

# // Suppose we abstract our file system by a string in the following manner:
# // The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

# // dir
# //     subdir1
# //     subdir2
# //         file.ext
# // The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.
# // The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:
# // dir
# //     subdir1
# //         file1.ext
# //         subsubdir1
# //     subdir2
# //         subsubdir2
# //             file2.ext
# // "dir/subdir2/subsubdir2/file2.ext"

# // The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty 
# second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.

# // We are interested in finding the longest (number of characters) absolute path to a file within our file system. 
# For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", 
# and its length is 32 (not including the double quotes).
# Given a string representing the file system in the above format, return the length of the longest absolute path to file in the abstracted file system. 
# If there is no file in the system, return 0.

# // Note:
# // The name of a file contains at least a . and an extension.
# // The name of a directory or sub-directory will not contain a ..
# // Time complexity required: O(n) where n is the size of the input string.

# // Notice that a/aa/aaa/file1.txt is not the longest file path, if there is another path aaaaaaaaaaaaaaaaaaaaa/sth.png.

# // [dir,\tsubdir1,\t\tfile1.ext,\t\tsubsubdir1,\tsubdir2,\t\tsubsubdir2,\t\t\tfile2.ext]
#     dir
# //     subdir1
# //         file1.ext
# //         subsubdir1
# //     subdir2
# //         subsubdir2
# //             file2.ext
        # subsubsubdir3
# // "dir/subdir2/subsubdir2/file2.ext"

# class Node:
#   def __init__(self, val):
#     self.children = []
#     self.val = val

# def lengthLongestPath(input: str):
#   window = []
#   pathlist = input.split('\n')
#   prevtab = -1
#   maxpath = 0
#   for e in pathlist:      
#     element = e.split('\t')
#     curtabs = len(element) -  1
#     if curtabs > prevtab:
#       window.append(element[-1])
#     else:
#       # print(maxpath)
#       if '.' in window[-1]:
#         abspath = '/'.join(window)
#         maxpath = max(maxpath, len(abspath))
#       for _ in range(prevtab - curtabs + 1):
#         window.pop()
#       window.append(element[-1])
#     prevtab = curtabs
#   if '.' in window[-1]:
#       maxpath = max(maxpath, len('/'.join(window)))
#   return maxpath
    
# print(lengthLongestPath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"))

# Success Details 
# Runtime: 24 ms, faster than 90.94% of Python3 online submissions for Longest Absolute File Path.
# Memory Usage: 13.9 MB, less than 54.82% of Python3 online submissions for Longest Absolute File Path.      
      
