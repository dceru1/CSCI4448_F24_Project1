# CSCI4448_F24_Project1

Some git tips i've learned (by myself or during my Co-Op)

1. !!!ALWAYS DO `git pull` BEFORE EDITING YOUR FILES!!!
This more applies to a repository w/ alot of forks/merges, but it's good practice. If you don't update your repository then try to commit, git will yell at you saying that your head is behind release

2. If you want to push files, do the following:
   - Do git add <file1> <file2> ... <filen>
   - Next, git commit -m "(a useful message)"
      Eg: git commit -m "Added tree.hpp to implement a binary tree"
   - Finnaly, git push
