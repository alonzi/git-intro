# git-intro
dfsdfdsfsd UVA Library Workshop on Introduction to Git and GitHub/GitLab. 

This file exists here: https://github.com/rjp0i/git-intro (or visit [here](https://rjp0i.github.io/intro.Fall2019.html) for a prettified view)

## About Me
* Ricky Patterson: I am the [Associate Director, Research Data Services, UVA Library](http://people.virginia.edu/~rjp0i)
* I was a research astronomer for 20+ years here at UVA

## Data Resources in the UVA Library
* [Research Data Services](https://data.library.virginia.edu/)
* [Workshop Series](https://data.library.virginia.edu/training/)

## First, our goals

1. Everyone has a GitHub and GitLab account, and has GitHub Desktop running on their computer
2. Create a repository and fork it
3. Feel comfortable with git/github workflows
4. Know how to get help

## Second, some terms

* git - version control software.
* GitHub - a for profit company recently purchased by Microsoft. It provides cloud-based hosting of repositories.
* GitLab - an alternative to GitHub, not owned by Microsoft ([why you might want to switch](https://about.gitlab.com/2017/07/19/git-wars-switching-to-gitlab/)). "Free software deserves free tools."
* repository (repo) - Basic unit in git: a record of all changes to specified files.
* fork - personal copy of another users repo.
* branch - a parallel version of a repo (main branch is called "master").

[Git Glossary](https://help.github.com/en/articles/github-glossary)

You can look at GitHub's [Git Handbook](https://guides.github.com/introduction/git-handbook/)

## Getting Git
* To play along you will need a [GitHub](https://github.com) account --> https://github.com/

* If on mac/linux you probably already have git, but we also want GitHub Desktop
  * goto [http://desktop.github.com](http://desktop.github.com) and download
  
* If on windows, the latest version of GitHub desktop [http://desktop.github.com](http://desktop.github.com) is fine for today, but it won't include the git "command line tools."  They are available:
  * Go to [https://gitforwindows.org/](https://gitforwindows.org/) and download

## Outline
0. Some background
1. Work on the GitHub browser interface
2. Look at the GitHub Desktop interface
3. Tips on getting help

## Reference for Git
The book <em>Computing Skills for Biologists: A Toolbox</em> contains a very useful introduction to Git, with practice data and code. Members of the UVA community can access the book [online](http://proxy01.its.virginia.edu/login?url=http://www.degruyter.com/isbn/9780691183961). 
The examples, data, code and solutions are hosted on a [github repo](https://github.com/CSB-book/CSB]https://github.com/CSB-book/CSB)

### A brief history of Version Control
* CVS (1990s) Centralized (client-server)
* SVN (2000s) Centralized (client-server)
* git (2005) Distributed. Developed by [Linus Torvalds](https://en.wikipedia.org/wiki/Linus_Torvalds) for Linux development.

### Getting Started: Hello World
* Let's walk through GitHub's [Hello World Guide](https://guides.github.com/activities/hello-world/)

### Using Github
### Step 0 - inspect this current repo
* In a web browser, visit this repo: [https://github.com/rjp0i/git-intro](https://github.com/rjp0i/git-intro)
* We are in the github interface:
  1. upper left corner: notebook icon next to rjp0i/git-intro  (a repo)
  2. big green button on the right hand side (down a little) says "Clone or Download" (how to get the files)
  3. list of files (how to browse the files)
  4. readme.md is rendered as Markdown (github automatically shows the readme file, very handy)
  
### Step 1 - create your own repo 
[https://guides.github.com/activities/hello-world/#repository](https://guides.github.com/activities/hello-world/#repository)
* Not so obvious, but in the upper right hand corner, click the '+' button, pull down: select 'new repository'
  1. name (this will be the address of the repo...)
  2. description
  3. public v private
  4. initialize with readme (alway say yes)
  5. license
  
### Step 2 - create a branch (Direct Collaborators)
[https://guides.github.com/activities/hello-world/#branch](https://guides.github.com/activities/hello-world/#branch)
* Let's leave the master branch alone and create a new branch
 1. Click the drop down at the top of the file list that says branch: master.
 2. Type a branch name, readme-edits, into the new branch text box.
 3. Select the blue Create branch box or just hit “Enter” on your keyboard.

Now we have two branches: master and readme-edits

### Step 3 - edit a file and commit changes
[https://guides.github.com/activities/hello-world/#commit](https://guides.github.com/activities/hello-world/#commit)
* You should now be in the readme-edits branch.
* Click on README.md in the list and then click the pencil to edit the file
  1. now type in the editor
  2. when done click green button at bottom 'commit changes'
    * commits can/should(?) be done early and often
    * no change is too small to commit, but you'll get a feel for how often you should commit after some time
    * but always write a commit message that describes your changes
    
* Now the master and readme-edits branches differ
    
### Step 4 - Pull requests
[https://guides.github.com/activities/hello-world/#pr](https://guides.github.com/activities/hello-world/#pr)
* Indirect Collaboration - pull requests
  1. Click the "Pull Request" tab, then "New pull request" ![alt text](https://guides.github.com/activities/hello-world/pr-tab.gif "Step 1")
  2. In the Example Comparisons box, select the branch you made, readme-edits, to compare with master (the original).![alt text](https://guides.github.com/activities/hello-world/pick-branch.png "Step 2")
  3. Proofread your changes in the diffs on the Compare page ![alt text](https://guides.github.com/activities/hello-world/diff.png "Step 3")
  4. When ready to submit, click the Create Pull Request Button ![alt text](https://guides.github.com/activities/hello-world/create-pr.png "Step 4")
  5. Write a title and a brief description of your changes ![alt text](https://guides.github.com/activities/hello-world/pr-form.png "Step 5")
  6. Click Create Pull Request
  
  ### Step 4.5 - Merging Pull Requests
  [https://guides.github.com/activities/hello-world/#merge](https://guides.github.com/activities/hello-world/#merge)
  * Now, let's merge the Pull Request, to bring the changes from readme-edits into the master branch.
  1. Click the green Merge pull request button to merge the changes into master.
    ![alt text](https://guides.github.com/activities/hello-world/merge-button.png "step 4.5")
  2. Click Confirm merge.
  3. Now we can delete the readme-edits branch, since its changes have been incorporated into master. You'll be prompted to do so inside the purple box. 
  ![alt text](https://guides.github.com/activities/hello-world/delete-button.png "delete branch")



### GitHub Flow
[https://guides.github.com/introduction/flow/](https://guides.github.com/introduction/flow/)


### Forks - Indirect Collaboration
  If you aren't a collaborator in a repo, you can't branch that repo. However, you can "fork" it, which is just creates a clone of the repo on the GitHub server.
  1. You can't push changes directly back to the original repo.
  2. You'll want to work on keeping your fork in sync with the project
    * add it to the original project as a remote, or
    * fetching regularly from the original repo
    
  Try forking from my repo, and make changes to the resulting fork, and then submit a pull request to me!
  
 
### Additional Items
  * Command Line Interface (CLI) [cheat sheet](https://education.github.com/git-cheat-sheet-education.pdf)
  * Organizations (such as https://github.com/UVA-RDS)
  * [Webpages](https://pages.github.com/) (such as https://rjp0i.github.io/intro.html)
  * Branches

## Getting Help

* Please, feel free to email me: ricky@virginia.edu
* The book <em>Computing Skills for Biologists: A Toolbox</em> contains a very useful introduction to Git, with practice data and code. Members of the UVA community can access the book [online](http://proxy01.its.virginia.edu/login?url=http://www.degruyter.com/isbn/9780691183961)
  * The examples, data, code and solutions are hosted on a [github repo](https://github.com/CSB-book/CSB]https://github.com/CSB-book/CSB)
* Lots of [git](https://git-scm.com/)/[GitHub](https://guides.github.com/)/[GitLab](https://gitlab.com/help?nav_source=navbar) resources from the source, as well as free training through a number of github sites
* StackOverflow is another good resource (e.g., for questions concerning git (or GitHub/GitLab): [https://stackoverflow.com/questions/tagged/git]https://stackoverflow.com/questions/tagged/git)

## How to compare revisions
* use the following style of URL with two commit hashes (Rev A and Rev B)
 * https://github.com/$USER/$REPO/compare/$REV_A...$REV_B
* $REV_A and B are the commit hashes for the versions you want to compare. You can get these by examining the Commit history of a file on Github

# Ways to Practice
1. Write some code, or some text
2. Do the version control in github
3. Edit it yourself
4. Have a friend do some edits as well

# This is an additional edit for practice.
Hopefully this works 
