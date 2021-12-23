import requests
import time

time1 = time.time()

url = "https://docs.google.com/forms/u/0/d/e/"

comments = 10 # How many comments you want to send. If you want to send multiple comments the form must allow it in its settings
form = "1FAIpQLPrcTRFeaHHKKrWTl5KJh8zmt9sos9dsFtYQJQlqvSt2QYpXDg" # That part in the URL after /0/d/e/
entries = ["entry1's number", "entry2's number"] # Press F12 to get to the networks panel. after submiting the file once it should be under 'formResponse' -> 'Payload' -> 'entry'
answers = ["Answer to entry1", "Answer to entry2"] # Answers must be valid

# Adding all entries together
_entries = ' '.join(["entry." + entries[i] + "=" + answers[i] if i == 0 else "&" + "entry." + entries[i] + "=" + answers[i] for i in range(len(entries))])

# Adding all parameters together
request = (str) (url + form + "/formResponse?" + _entries)


for i in range(0, comments):
    requests.post(request)    

print("Done!")  
print(f"{comments} Comments in {time.time() - time1} seconds")
