import sys
from serp.cli import ArgumentChecker

#args = ["-c", "code/program.py"]
args = ["main.py", "-c", "a"]
# args = sys.argv

def test(targetfile: str, optional_path: str = ""):
    print(f"Targetfile: {targetfile}")
    print(f"Optional path: {optional_path}")

argChecker = ArgumentChecker(args)

argChecker.addCommand("help", "h", argChecker.checkUsage, [], [])
argChecker.addCommand("compile", "c", test, ["TARGET_FILE"], ["OPTIONAL_FILE"])

argChecker.checkUsage()

argChecker.execute()