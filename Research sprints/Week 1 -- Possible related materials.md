- Reference:
	- Introduction to cultural analytics and python 
		- https://melaniewalsh.github.io/Intro-Cultural-Analytics/06-Network-Analysis/00-Network-Analysis.html
	- Simple machine learning
		- ![[Pasted image 20230915162522.png|100]]
		- source: scikit-learn algorithm cheat-sheet
		- ![[Pasted image 20230915162556.png|100]]
		- source: a complete chart of neural network (2016 medium post)
	- [[../Concepts/Spark]]
	- [[../Concepts/MongoDB]]

- Skill-set:
	- How to host a dataset with github?
	- 1. Push the data into one of the repository
	- 2. Generate "raw" link from the webpage
	- ![[Pasted image 20230915162814.png]]
	- 3. Test the "raw" link in the browser
	- ![[Pasted image 20230915162853.png]]
	- 4. Writing the code that loads the online dataset
```python
# Turn off scientific notation
np.set_printoptions(suppress=True)  

# Import data from csv file url
path = 'https://raw.githubusercontent.com/selva86/datasets/master/Auto.csv'
data = np.genfromtxt(path, delimiter=',', skip_header=1, filling_values=-999, dtype='float')
data[:3]  # see first 3 rows
```
![[Pasted image 20230915162930.png]]


