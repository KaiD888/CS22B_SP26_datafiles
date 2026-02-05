### This template is for the class exercises covered in M01_L03_review-fxn-condition for CS 22B.

## root folder if applicable
# root='/path/to/folder/'

##### CL4.1: Writing a function 
### Write a function that takes two arguments; a DNA sequence and a nucleotide (ie., “A”, “T”, “C” or “G”). Return the percentage of the DNA sequence that the nucleotide makes up.

dna = "ATTGGCTATACCGGCATCGGGTAGCC"

# step 1: Write the function that takes in two argument and calculate (num of nucleotide)*100/(total nucleotide)

#def get_percent():

# step 2: modify the function above to pass in a third argument to return 2 significant figures

#def get_percent_2sig():


##### CL4.2: Using assert to test your function
### Write assertion statements to test your function, get_percent_2sig.
### Part A.: Write assertion that takes in sequence and nucleotide [“A”]

### Part B.: If you change the assertion so that the  expected result is 0.80, what is your output?


##### CL4.3: Conditional statements
### Find the accession that starts with ‘a’

accession_name = ['ab56', 'bh84', 'hg84', 'ay97', 'cd72', 'ef56']

### step 1: Write a for loop that iterates over the accession_name list 

### step 2: Use a conditional statement to ask if the accession name starts with ‘a’ and if it does, print out the name


##### CL4.4: if-elif-else 
### Write three files of accession names; one start with ‘a’, one start with ‘b’, and last one has all others accession names.

accession_name = ['ab56', 'bh84', 'hg84', 'ay97', 'cd72', 'ef56']
### step 1: Write three files

### step 2: Iterate over the list of accession names and sort them into the correct files.


##### CL4.5: Boolean operator (in this example 'or')
### Given the file, drosphila.csv, write a function called 'get_gene()' that takes in the data file. Write a loop that iterates through the rows and filter out the gene names that belong to Drosophila melanogaster or Drosophila simulans. Returns the values to a new list 'Dm_Ds'

### drosphila.csv's line is separated by ',' and consists of species, sequence, names, expression

### step 1: import library csv and read in file

### step 2: Iterate through each line and split string into different variables

### step 3: compare the variable that contains species name 
