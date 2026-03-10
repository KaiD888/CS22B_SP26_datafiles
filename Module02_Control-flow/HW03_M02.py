### CS 22B Module 02 - Homework 3
### Name: <Your Name>

##### Homework practicing Control flow #####

#### Part I: Employee Performance Report (Contol flow exercises)
### Given a list of employees (dictionary containing emplyee's name, salary, department, and performance score),
# Your task is to:
# A. Calculate the average performance score for each employee
# B. Classify each employee based on the average performance score and print out the classification for each employee. The classification is as follows:
# - "Excellent" if the average score is 4.5 or above
# - "Good" if the average score is between 3.5 and 4.4 (inclusive)
# - "Needs Improvement" if the average score is below 3.5
# C. Find the employee with the highest salary in the "Engineering" department, and
# D. Print a dictionary where the keys are the department names and the values are lists of employee names who belong to the "Excellent" category in each department.


employees = [
    {"name": "Alice", "salary": 50000, "department": "Marketing", "performance_scores": [4.0, 4.5, 3.8, 3.2]},
    {"name": "Bob", "salary": 60000, "department": "Engineering", "performance_scores": [4.2, 4.7, 4.1, 4.3]},
    {"name": "Richard", "salary": 200000, "department": "Engineering", "performance_scores": [2.2, 2.7, 2.1, 2.3]},
    {"name": "Charlie Li", "salary": 75000, "department": "HR", "performance_scores": [3.9, 3.2, 3.5, 2.8]},
    {"name": "Diana", "salary": 55000, "department": "Marketing", "performance_scores": [4.8, 4.5, 4.2, 4.6]},
    {"name": "Mark Brown", "salary": 75000, "department": "HR", "performance_scores": [4.6, 4.8, 4.9, 4.7]},
    {"name": "Mary Lou Richard", "salary": 55000, "department": "Marketing", "performance_scores": [2.4, 2.2, 3.1, 2.7]}
]

### Part A: Calculate the average performance score for each employee

for e in employees:
        avg_score = sum(e["performance_scores"]) / len(e["performance_scores"])
        print(f"{e['name']} has an average score of {avg_score:.2f}")

### Part B: Classify each employee based on the average performance score and print out the classification for each employee
## Let's make this a function so we can reuse it in Part D
def employee_classification (employees):
	ec_list = []
	for e in employees:
		avg_score = sum(e["performance_scores"]) / len(e["performance_scores"])
		if avg_score >= 4.5:
			classification = "Excellent"
		elif avg_score >= 3.5:
			classification = "Good"
		else:
			classification = "Needs Improvement"
		e["classification"] = classification
		ec_list.append(e)
	return ec_list

ec_list = employee_classification(employees)
for e in ec_list:
        print(f"{e['name']} is classified as a(n) {e['classification']} worker.")

### Part C. Find the employee with the highest salary in the "Engineering" department, and
highest_salary = 0
for e in employees:
        if e["department"]=="Engineering":
                if e["salary"] > highest_salary:
                        highest_salary = e["salary"]
                        highest_eng = e["name"]
                print(f"The Engineering employee with the highest salary is: {highest_eng}")

### Part D. Print a dictionary where the keys are the department names and the values are lists of employee names who belong to the "Excellent" category in each department.
excellent_emp = {}
ec_list = employee_classification(employees)

for e in ec_list:
        if e["classification"] == "Excellent":
                dept = e["department"]
                excellent_emp[dept] = e["name"]
        print(excellent_emp)

