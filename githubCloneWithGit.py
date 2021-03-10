import git
import sys

URL_BASE_GIT = "https://github.com/"
EXTENSION_GIT_REPO = ".git"
PATH_LOCAL_TO_CLONE = "/Users/caiosalgado/Desktop/git_projects/{}"


def clone_repositories(list_repository_names, path_to_clone):
    print("Cloning repositories in {}".format(list_repository_names))
    for repository_name in list_repository_names:
        path_clone = "{}{}{}".format(URL_BASE_GIT, repository_name, EXTENSION_GIT_REPO)
        git_repo = git.Repo.clone_from(path_clone, path_to_clone.format(repository_name))
        print(path_clone)
        print(git_repo.branches)


list_args = sys.argv
# remove program name
list_args.pop(0)
# get function exec
# if help show how to run the command
# if exec execute de code
command = list_args.pop(0)

if command == "help":
    print("**************************************************************************************")
    print("* To run this program follow the example below")
    print("* python3 githubCloneWithGit.py [command] [path_to_clone] [... repository_names]")
    print("* command - ")
    print("* --------- help to get instructions about run the program")
    print("* --------- exec to execute the program itself")
    print("* path_to_clone - ")
    print("* --------- string with the base path to clone the repo")
    print("* --------- example: /Users/caiosalgado/Desktop/git_projects")
    print("* repository_names - ")
    print("* --------- list of repositories separate by space")
    print("* --------- CaioSalgado1995/docker-websphere-liberty-sample CaioSalgado1995/bicicletario-web")
    print("* IMPORTANT - you must have the git config authentication OK into your operation system")
    print("**************************************************************************************")
elif command == "exec":
    # get path_to_clone
    path_to_clone = list_args.pop(0)
    path_to_clone += "/{}"
    print(path_to_clone)
    list_repo = list_args
    print(list_repo)
    clone_repositories(list_repo, path_to_clone)
else:
    raise Exception("command not valid")
#clone_repositories(list_repo, PATH_LOCAL_TO_CLONE)
