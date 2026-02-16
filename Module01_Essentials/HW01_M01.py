### CS 22B Module 01 - Homework 1
### Name: <Your Name>

### This template is for Homework #01 reviewing the material we covered in Module 01 Essentials for CS 22B.

### root folder if applicable
# root='/path/to/folder/'

##### Problem 1: Trim adapter reads and validate bases
## 1. Write a script that reads in adapter_reads.txt line by line and remove the first 14 base pair (characters) that are the adapters. 
## 2. Validate if the read is valid by ensuring that all the characters are in {A,T,C,G}. ie., Not another character eg N.
## 3. Write the valid trimmed reads to a new file, clean_reads.txt, and the invalid reads in another new file,  bad_reads.txt. 
## 4. Print as output, the number of valid and invalid reads. 

valid = 0
invalid = 0

infile = open("adapter_reads.txt", "r")
clean_file = open("clean_reads.txt", "w")
bad_file = open("bad_reads.txt", "w")

for line in infile:
	read = line.strip()
	trimmed_read = read[14:]

	is_valid = True

	for base in trimmed_read:
		if base not in "ATCG":
			is_valid = False
			break
	
	if is_valid:
		clean_file.write(trimmed_read + "\n")
		valid += 1
	else:
		bad_file.write(trimmed_read + "\n")
		invalid += 1

infile.close()
clean_file.close()
bad_file.close()

print("Valid reads:", valid)
print("Invalid reads:", invalid)


##### Problem 2: List comprehension statistic
## 1. Using the valid trimmed reads from problem 1, create a list comprehension command that returns the length of each valid read. 
## 2. Create a second list comprehension command that returns the GC% of each valid read (ie., GC.count/length). 
## 3. Print as output, the minimum length, max length, and average length of your valid trimmed reads. Additionally, print the average GC% rounded to 3 decimals.

clean_file = open("clean_reads.txt", "r")

valid_reads = []

for line in clean_file:
	read = line.strip()
	valid_reads.append(read)

clean_file.close()

lengths_valid = [len(read) for read in valid_reads]

GC_percentages = [
	(read.count("G") + read.count("C")) / len(read)
	for read in valid_reads
]

min = min(lengths_valid)
max = max(lengths_valid)
average = sum(lengths_valid) / len(lengths_valid)
average_GC = sum(GC_percentages) / len(GC_percentages)

print("\nMin length:", min)
print("Max length:", max)
print("Average length:", average)
print("Average GC:", round(average_GC, 3))


##### Problem 3: Dictionary
## 1. Using the valid trimmed reads from problem 1, build a dictionary called 'base_counts' that has the total counts of A, T, C, G across all valid reads. 
## 2. Use a loop that iterates over the dictionary and compute and print the product of the four counts (A*C*T*G).

base_counts = {"A": 0, "T": 0, "C": 0, "G": 0}

for read in valid_reads:
	for base in read:
		base_counts[base] += 1

print("\nBase counts:", base_counts)

product = 1

for base in base_counts:
	product *= base_counts[base]

print("Product of ACTG:", product)


#### Problem 4: Function and asserts
## 1. Write a function that returns the percentage of any nt (A,T,C,G) in a sequence, rounded to 2 significant figure. 
## 2. Include 3 asserts to test your code including a known case (eg "AATT" with "A" returning 50.00) and a case with 0%.

## Use this sequence as your test sequence
## sequence = TTATAAGCCGATTATAAGCCCGTAACCGGTTAG

def sequence_percent(sequence, seq):

	count = sequence.count(seq)
	percent = (count / len(sequence)) * 100
	return round(percent, 2)

sequence = "TTATAAGCCGATTATAAGCCCGTAACCGGTTAG"

assert sequence_percent("AATT", "A") == 50.00
assert sequence_percent("AATT", "G") == 0.00

Test = round((sequence.count("T") / len(sequence)) * 100, 2)
assert sequence_percent(sequence, "T") == Test

print("\nTests passed")

