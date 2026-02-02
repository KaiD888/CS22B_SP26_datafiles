### This template is for the class exercises covered in M01_L02_review-files for CS 22B.

## root folder if applicable
# root='/path/to/folder/'

##### CL1.1: Count the number of T in the sequence. 
sequence = "ATTGGCTATACCGG"
# ** your code **
number_T = ("T")
number_T = sequence.count("T")
print(number_T)

##### CL1.2: For the sequence above, convert the sequence from the 4th character to the 9 character to lower case
# ** your code **
sequence = "ATTGGCTATACCGG"
new_sequence = sequence[:3] + sequence[3:9].lower() + sequence[9:]
print(new_sequence)

##### CL1.3: Find the noncoding(4th to 9th character) and coding regions(all other characters)
## step 1: open the seq.txt file
# ** your code **
seq_file = open("seq.txt", "r")
seq = seq_file.read().strip()
seq_file.close()

## step 2: create 2 new files for coding and noncoding
# ** your code **
coding_file = open("coding.txt", "w")
noncoding_file = open("noncoding.txt", "w")

## write to new files sequence 4-9 as lowercase to noncode file and all other sequence as uppercase to code file. Don't forget to close() to save the files.
# ** your code **
noncoding = seq[3:9].lower()

coding = (seq[:3] + seq[9:]).upper()

noncoding_file.write(noncoding)
coding_file.write(coding)

coding_file.close()
noncoding_file.close()

##### CL1.4: Trim the adapter sequence (14 bp seq at front of each line “ATTCGATTATAAGC”)
## step 1: open the adapter_input.txt file
# ** your code **

adapter_input = open("adapter_input.txt", "r")

## step 2: create an output file
# ** your code **

adapter_output = open("adapter_output.txt", "w")

## step 3: read in each line in the adapter_input file and trim the first 14 characters. Write the remaining sequence to the output file. Do this for each line. Don't forget to close() to save the file. 

for line in adapter_input:
    trimmed = line.strip()[14:]
    adapter_output.write(trimmed + "\n")

adapter_input.close()
adapter_output.close()
