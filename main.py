import sys
from serp.cli import ArgumentChecker
from serp.lexer import Lexer

from serp.utils.FilePath import FilePath

args = ["main.py", "-c", "code/program.py"]
#args = ["main.py", "-c", "a"]
# args = sys.argv

def compile(targetfile: str, outputpath: str = ""):
    targetfile = FilePath(targetfile)
    outputpath = FilePath(outputpath + targetfile.getPureFilename() + ".o" if outputpath == "" else outputpath)

    print(f"targetfile: {targetfile.getPath()}")
    print(f"outputpath: {outputpath.getPath()}")
    print("-"*32)



    Lexer(filePath=targetfile)

argChecker = ArgumentChecker(args)

argChecker.addCommand("help", "h", argChecker.checkUsage, [], [])
argChecker.addCommand("compile", "c", compile, ["TARGET_FILE"], ["OUTPUT_PATH"])

argChecker.checkUsage()

argChecker.execute()