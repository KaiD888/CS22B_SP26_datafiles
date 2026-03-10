### CS 22B Module 02 - Homework 2
### Name: <Your Name>

##### Homework practicing Control flow and Regular expression #####

## Import library
import re

##### Problem 1 - if/elif/else
## You are given a list of log lines. Classify each line into one of these buckets:
## - "ERROR": contains ERROR and an error code like E1234
## - "WARN": contains WARN and a module tag in brackets like [auth]
## - "INFO": contains INFO and a user id like user=ab_12
## - "SKIP": anything else
## Return a dictionary with counts per bucket.

lines = [
    "2026-02-11 10:00:01 ERROR E1042 [db] user=ab_12 msg=timeout",
    "2026-02-11 10:00:02 WARN [auth] user=xy_77 msg=bad password",
    "2026-02-11 10:00:03 INFO user=ab_12 msg=login ok",
    "2026-02-11 10:00:04 ERROR [api] msg=missing code",
    "garbage line"
]

### step 1: Define the count variables
error_count = re.compile(r"\bERROR\b.*\b(E\d{4})\b")
warn_count = re.compile(r"\bWARN\b.*\[[a-zA-Z_]+\]") 
info_count = re.compile(r"\bINFO\b.*\buser=([a-z]{2}_[0-9]{2})\b")

### step 2: Initialize the count dictionary 
counts = {"ERROR": 0, "WARN": 0, "INFO": 0, "SKIP": 0}

### step 3: Loop throught the dictionary with if-elif-else
for line in lines:
    if error_count.search(line):
       counts["ERROR"] += 1
    elif warn_count.search(line):
       counts["WARN"] += 1
    else:
       counts ["SKIP"] += 1

print(counts)


##### Problem 2 - Check passwords with boolean logic and regex
## Write a function check_password(pw) that returns one of:
# "STRONG" if:
# - length ≥ 10
# - contains at least 1 lowercase, 1 uppercase, 1 digit, 1 symbol from !@#$%^&*
# - does not contain whitespace
# otherwise "WEAK" 
## Test the function on a list of passwords using a loop

test_pw = ["Short7!", "LongerPass7!", "GoodPassw0rd!", "Bad Passw0rd!", "N0SymbolHereAAA"]

### step 1: Define variables
import re

lower = re.compile(r"[a-z]")
upper = re.compile(r"[A-Z]") 
digit = re.compile(r"\d")
symbol = re.compile(r"[!@#$%^&*]")
space = re.compile(r"\s")

### step 2: Write a function that check password (str) to test cases
def check_password(pw: str) -> str:
    strong = (
	len(pw) >= 10
	and lower.search(pw) is not None
	and upper.search(pw) is not None
	and digit.search(pw) is not None
	and symbol.search(pw) is not None
	and space.search(pw) is None
)

    return "STRONG" if strong else "WEAK"

### step 3: Use case. Test list test_pw
for t in test_pw:
	print(t, "password is ", check_password(t))

