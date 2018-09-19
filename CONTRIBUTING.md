Contributing to sv-tools.

One should always check with owner of project before starting your work to ensure one does not duplicate work.

Coding style.
  PyCharm default coding style is preffered, that is:
    class names start with capital letter, e.g. class FruitsAndVegetables()
    functions are named in lower_case_underscore_separation,
    shadowing should be avoided with single underscore, e.g. _shadowing_variable,
    at least one new line after function/class definition,
    space around operators like '=', '+', ..., e.g. fruits = apples + peaches.

Naming convention.
  Name variables and function from general description to more specific.
  
  text_input_white <- it is text, which is user's input and happens to be white-colored.
  copy_object_overwrite() <- function does copy on object and overwrites if object exists.

Stages of code completion:
  no compile, no implemented tests - working progress
  compiles, tests do not pass - code ready
  compiles, tests pass - production ready
  compiles, tests pass on multiple platforms, user tested - release ready
  
Working progress is more than welcome in commits, we can git for synchs in between machines. Do not commit .pdf files
from documentation unless in release. Always try to improve .gitignore and testing scheme. Branching is encouraged
for adding features that are independent of other features.

Note. Gerrit review will be added when project is out of rapid development stage (that should be close to first release).
