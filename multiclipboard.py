import sys
import clipboard
import json

# paste the data from cliboard into the data variable
data = clipboard.paste()
clipboard.copy("abc")
print(data)

