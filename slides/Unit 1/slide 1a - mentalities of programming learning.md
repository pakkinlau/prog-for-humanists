

Reference / Readings:
- Python for beginners: https://learn.microsoft.com/en-us/training/paths/beginner-python/
- Python for data analysis: https://wesmckinney.com/book/numpy-basics


---
# Course - Programming for humanist

#### Knowledge 1: Read as little documentation as possible
- The Book Reading Paradigm:
	- Traditionally, we approach books with the expectation of a linear progression—from the beginning to the end—to fully grasp the concepts and vocabulary presented.
- The Programmers' Paradigm:
	- Programming documentation and learning do not necessarily follow a linear path. Unlike traditional reading, understanding programming can often be a more recursive process.
	- This non-linear approach allows programmers to dive into any part of the code or documentation and understand components in isolation before seeing how they integrate into the larger picture.
	- **Advantage**: Programmers can often infer the meaning and functionality of code segments without needing to comprehend the entire codebase first.
	- When you feel being overwhelmed, try to draw some mind maps or diagrams to help you identify relationships between keywords, objects or methods 
#### Knowledge 2: Leading your mind with what you want to do, not by what is given from the package/book
- High-order thinking:
	- Drawing flowcharts, mind maps, status, 
	- UML sequence / activity diagram: Flowcharts
	- UML Class / component diagram: Blueprint charts
- Pareto principles in programming
	- In most cases, you just need to learn 20% of keywords, methods from a package to utilize / solve 80% of the problems you need to solve. 
#### Knowledge 3: Tree Structure in Programming Languages
- While there is no need to read the entire documentation to learn one package, we need to learn some important "grammar" and "models" to know how things work. 
- Learning a programming language, such as Python, is like how we learn grammar when learning a new language to help us understanding the entire script. 
- Python
	- Tree structure: It often use a hierarchical tree structure to organize code. Understanding this can help navigate and comprehend programming concepts:

    - **Classes**: 
        - They encapsulate data and behavior. Think of classes as blueprints for creating objects.
        - For example, a `Car` class might contain information about car properties (like color, make, model) and behaviors (like drive, stop, honk).

    - **Methods**: 
        - These are functions defined within a class that describe the behaviors the objects can perform.
        - In our `Car` class example, a method might be `accelerate`, which increases the car's speed.

    - **Attributes**: 
        - Attributes are the properties or data stored within an object.
        - Continuing with the `Car` example, attributes could include `color`, `make`, `year`, etc.

#### Knowledge 4: An ability to capture new patterns from script
- Certainly there would be new patterns in the script you did not know it before. We don't need to feel panic on it. Instead, there are general ways to deal with it: 
	- Step 1. Recognizing keywords, symbols and structures:
		- Possible keywords: `with`, `**`, indentations
	- Step 2. Research their meaning
	- Step 3. Coining and conceptualize and name these structures for easier reference.

#### Knowledge 5: How to comprehend -- Embedded Documentation
- Many programming languages and libraries come with embedded documentation, which can be immensely helpful for learning and troubleshooting:

    - **Tool Tips**: 
        - Modern Integrated Development Environments (IDEs) often allow you to hover over keywords and functions to reveal documentation or definitions in tooltips.
        - This instant access to information helps coders understand the functionality and usage of different components without needing to search through external documentation.

    - **Contextual Help**:
        - IDEs and text editors may also provide contextual help or links to more detailed documentation for the item under the cursor.
        - This feature can guide programmers to use the methods and attributes correctly within their code.

#### Knowledge 6: Separating the learning of models and methods
- When having "model" in between speaker and receiver in the conversation, you can express yourself in a more concise way. 
	- Such as you want to be familiar with what is "dataframe" if you want to perform data analytics with pandas

#### Knowledge 7: Familiar with finding suitable tools from a pool of resources
- Reinventing the wheel for every project is inefficient. Instead, learn to find and utilize existing solutions:
- There are some pathways programmers can look for pre-built solutions:
	- 1. Look for any packages that focus on the area we concern
	- 2. Look for any of these packages that are providing functionalities that we want to use
	- 3. Test out whether the methods provided by this package are working as we expect. 
- Example questions you might find it useful:
	- Q1: What are the task I am going to do?
	- Q2: Can I find some sample script that is doing such thing?
	- Q3: Is there any lines I cannot comprehend?
	- Q4: Is there any important models that package is using?