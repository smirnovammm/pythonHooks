import re
import sys
from subprocess import check_output

red_color = "\033[1;31m"


def perepare_commit_msg():
    commit_msg_filepath = sys.argv[1]
    branch = (check_output(["git", "symbolic-ref", "--short", "HEAD"]).decode("utf-8").strip())

    regex = r"^[A-Z]{1,3}-[0-9]{1,9}"

    with open(commit_msg_filepath, "r+") as file:
        commit_msg = file.read()
        if re.search(regex, branch):
            found_obj = re.match(regex, branch)
            prefix = found_obj.group(0)
            if commit_msg.find(prefix) == -1:
                file.seek(0, 0)
                file.write(f"[{prefix}] {commit_msg}")
        else:
            print(red_color + "Branch name does not contain ticket number")
            print("commit-msg hook failed")
            sys.exit(1)


