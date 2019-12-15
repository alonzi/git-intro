Annamalai's version
# git-intro
uva library workshop on introduction to git and github

# https://github.com/alonzi/git-intro

## Who am I?
* [Senior Research Data Scientist with the Data Science Institute and UVA Library](https://dsi.virginia.edu/people/peter-alonzi)
* I like to be interrupted with questions! Please jump right in.

## Welcome to the UVA Library
* [Research Data Services](https://data.library.virginia.edu/)
* [Workshop Series](https://data.library.virginia.edu/training/)
  * Data Storage Best Practices (Bill Corey)	Tuesday, 11/6	14:00 – 15:30	Brown 133

## First, some terms

* git - version control software
* github - a for profit company owned by microsoft
* repository - a record of all changes to specified files (aka repo)
* fork - a repo and a pointer to the repo it deviates from

* [visual](https://github.com/UVA-DSI/2018-bootcamp/blob/master/intro-general-tools/github_terms.png)

## Second, our goals

1. Everyone has git on their computer in working order
2. Become comfortable with git/github workflows
3. Know how to get help

## Getting Git
* to play along you will need a github account --> https://github.com/

* if on mac/linux you probably already have git
  * go to the terminal and type git
  * if it says: *-bash: git: No such file or directory* (or something similar)
  * goto https://git-scm.com/ and download
  
* if on windows you probably need to get git
  * goto https://git-scm.com/ and download

## Outline
0. Some background
1. Work through the GitHub browser interface
2. Quick show of terminal interface
3. Tips on getting help

### Cartoons
* http://phdcomics.com/comics.php?f=1531
* https://swcarpentry.github.io/2014-06-24-wise-penn/lessons/nelle-git/git.html
* https://xkcd.com/1597/

### A brief history (according to wiki)
* Designed by [Linus Torvalds](https://en.wikipedia.org/wiki/Linus_Torvalds)
* initial release: 7 April 2005
* official repo: https://github.com/git/git
* most recent release (as of writing) 2.19.0 / 10 September 2018; 19 days ago

### Step 1 - inspect this repo
* goto: https://github.com/alonzi/git-intro
* we are in the github interface, nb:
  1. upper left corner: notebook icon next to alonzi/git-intro  (a repo)
  2. big green button on the right hand side (down a little) says "Clone or Download" (how to get the files)
  3. list of files (how to browse the files)
  4. readme.md is shown in all its glory (github automatically shows the readme file, very handy)
  
### Step 2 - create a repo
* hard to find, upper right hand corner '+' button, pull down: select 'new repository'
  1. name
  2. description
  3. public v private
  4. initialize with readme (alway say yes)
  5. license
  
### Step 3 - edit a file
* click on readme.md in the list and then click the pencil
  1. now type in the editor
  2. when done click green button at bottom 'commit changes'
    * commits should be done early and often
    * no change is too small to commit
    * leave a message that is maybe *5* words long and includes a verb
    
### Step 4 - collaboration
* Direct Collaboration - collaborator
  * add a collaborator to your repo
  * setting tab (top of repo page) --> collaborators menu (LHS of settings page)
  * search users to add by username/email
  * **This gives the collaborator power to commit directly**
* Indirect Collaboration - pull requests
  * click fork button (upper right of repo page)
  * look at upper left corner and note the new symbol and pointer
  * **This is a completely functional independent repo**
  * You may reccomend changes to the remote by initiating a pull request
    * click the pull request button
    * this is a little tricky so let's walk slowly
  * Demo, someone please pull request me and I'll show on screen what it looks like  


### Step 5 - local v cloud
  * downloading your code
  * syncing your repositories [sync to upstream](https://help.github.com/articles/syncing-a-fork/)
  * Command Line Interface - [cheat sheet](https://services.github.com/on-demand/downloads/github-git-cheat-sheet.pdf)

### Additional Items
  * Command Line Interface (CLI)
  * Organizations
  * [Webpages](https://pages.github.com/)
  * Branches

## Getting Help (most important part so we end on it)
* How to compose a google search
* What sources are reputable
* Then email: datascientist@virginia.edu

## Helpful Links - https://github.com/alonzi/git-intro/blob/master/helpful_links.md

## How to compare revisions
* use the following URL with two commit hashes
* https://github.com/$USER/$REPO/compare/$REV_A...$REV_B
* eg: https://github.com/alonzi/feynman/compare/b08a2a61bb96ccfea3127a92a8c356df3f3b6f0e...master

# Ways to Practice
1. Write some code
2. Do the version control in github
3. Ask a friend to review it
