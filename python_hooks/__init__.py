import re
import sys
from subprocess import check_output

red_color = "\033[1;31m"
commit_msg_filepath = sys.argv[1]
branch = (check_output(["git", "symbolic-ref", "--short", "HEAD"]).decode("utf-8").strip())

regex = r"^[a-zA-Z]{1,5}-[0-9]{1,9}"


def perepare_commit_msg():
    if re.search(regex, branch):
        found_obj = re.match(regex, branch)
        prefix = found_obj.group(0)
        with open(commit_msg_filepath, "r+") as file:
            commit_msg = file.read()
            if commit_msg.find(prefix) == -1:
                file.seek(0, 0)
                file.write(f"[{prefix}] {commit_msg}")
    else:
        print(red_color + "Branch name does not contain ticket number")
        print("prepare-commit-msg hook failed")
        sys.exit(1)
