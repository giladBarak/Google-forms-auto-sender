import requests
import time
import math

time1 = time.time()

url = "https://docs.google.com/forms/u/0/d/e/"

comments = 100 # How many comments you want to send. If you want to send multiple comments the form must allow it in its settings
form = "1FAIpQLScnTRFeaHHKKrWTl5KJh8zmt9sos9dsFtYQJQlqvSt2QYpYwd" # That part in the URL after /0/d/e/
entries = ["902735262", "581532641"] # Press F12 to get to the networks panel. after submiting the file once it should be under 'formResponse' -> 'Payload' -> 'entry'
answers = ["Answer to 902735262", "Answer to 581532641"] # Answers must be valid

# Adding all parameters together
request = (str) (url + form + "/formResponse?" + ["entry." + entries[i] + "=" + answers[i] if i == 0 else "&" + "entry." + entries[i] + "=" + answers[i] for i in range(len(entries))])

for i in range(0, comments):
    requests.post(request)    

print("Done!")  
print(f"{comments} Comments in {time.time() - time1} seconds")
