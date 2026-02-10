### This template is for Homework #01 reviewing the material we covered in Module 01 Essentials for CS 22B.

## root folder if applicable
# root='/path/to/folder/'

##### Problem 1: Trim adapter reads and validate bases
### Write a script that reads in adapter_reads.txt line by line and remove the first 14 base pair (characters) that are the adapter. Validate if the read is valid by ensuring that all the characters are in {A,T,C,G}. Write the valid trimmed reads to clean_reads.txt and invalid reads in bad_reads.txt. Print the number of valid and invalid reads.


##### Problem 2: List comprehension statistic
### Using the valid trimmed reads, create a list comprehension that returns the length of each valid read. Create a second list comprehension that returns the GC% of each valid read (GC.count/length). Print the minimum length, max length, and average length. Print the average GC% rounded to 3 decimals.


##### Problem 3: Dictionary
### Using the valid trimmed reads, build a dictionary base_counts with total counts of A, T, C, G across all valid reads. Use a loop over the dictionary and compute and print the product of the four counts (A*C*T*G).


#### Problem 4: Function and asserts
### Write a function that returns the percentage of any nt (A,T,C,G) in a sequence, rounded to 2 significant figure. Add 3 asserts including a known case (eg "AATT" with "A" returning 50.00), case with 0%

sequence = TTATAAGCCGATTATAAGCCCGTAACCGGTTAG

