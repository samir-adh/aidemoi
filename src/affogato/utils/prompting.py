system_prompt = """
You are a LLM embedded in a program that helps user using commands.
You are will be given user command and you should anwser by writing a summary on how to use the command with the arguments used by the user.
You response should be tailored to this specific command and argument combination.
The user's command might be incorrect, in such case you should propose some fixes.
You should respond to this query with a short answer in the from of common unix help messages.
Your answer needs to be concise and relevant to the context.
You should only answer with the help message, nothing else.
Make sure that you are not inventing any command or option when answering.
If you are given the man page of the command, base yourself on it to generate your anwser.
Do not wrap your answer in backticks, quotes or double quotes, respond directly with text.
"""

# Here is an example of such a message if the command you received was only "ls":
# <<<
#   ls
#   List directory contents.  More information: https://www.gnu.org/software/coreutils/manual/html_node/ls-invocation.html.
#   - List files one per line:    ls -1
#   - List all files, including hidden files:    ls --all
#   - List files with a trailing symbol to indicate file type (directory/, symbolic_link@, executable*, ...):    ls --classify
#   - List all files in [l]ong format (permissions, ownership, size, and modification date):    ls -l --all
#   - List files in [l]ong format with size displayed using human-readable units (KiB, MiB, GiB):    ls -l --human-readable
#   - List files in [l]ong format, sorted by [S]ize (descending) recursively:    ls -lS --recursive
#   - List files in [l]ong format, sorted by [t]ime the file was modified and in reverse order (oldest first):    ls -lt --reverse
#   - Only list directories:    ls --directory */
# >>>


def make_prompt(command_as_str: str, manual: str | None = None):
    full_prompt = system_prompt
    full_prompt += "Here is the actual command typed by the user : "
    full_prompt += command_as_str
    if manual is not None:
        full_prompt += "For reference here is the man page of the command : \n"
        full_prompt += manual
    return full_prompt
