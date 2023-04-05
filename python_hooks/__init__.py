import re
import sys
from subprocess import check_output

red_color = "\033[1;31m"
commit_msg_filepath = sys.argv[1]
branch = (check_output(["git", "symbolic-ref", "--short", "HEAD"]).decode("utf-8").strip())

regex = r"^[a-zA-Z]{1,5}-[0-9]{1,9}"


def perepare_commit_msg():
    if re.search(regex, branch):
        try:
            found_obj = re.match(regex, branch)
            prefix = found_obj.group(0)
            with open(file=commit_msg_filepath, mode="rw", encoding="utf-8", errors="ignore") as file:
                commit_msg = file.read()
                if commit_msg.find(prefix) == -1:
                    file.seek(0, 0)
                    file.write(f"[{prefix}] {commit_msg}")
        except Exception as e:
            print(f"{e}")
    else:
        print("Branch name does not contain ticket number")
        sys.exit(1)
