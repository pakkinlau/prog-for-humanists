
Updated: Outline of the course

### Brief breakdown of the course

- Introduction (week 1, 0% in the group project)
- Accessing, handling and transformation of data (25% of the content)
- Populating and managing data with some database schemas (25% of the content)
- Machine learning (25% of the content)
- Analysis and visualization from data (25% of the content)

---
### A more detailed syllabus

- Introduction (week 1)
	- Overview of the course, Breaking down some example digital humanities projects 
	- Creation of github package
	- Writing and reading object-oriented programming with python
		- Purpose: student can get familiar with the style of programming that hiding detail
		- Briefly discuss some principles of writing effective code, such as modularity, information hiding. 
	 - Self-learning package:
			- Overview of the tools will be used throughout the course (vs code, database, Github, huggingface)
			- Discovering available solutions from github
			- Getting free github copilot with CUHK email

- Part I: Accessing, mining, handling and transformation of data
	- Historical documents: 
		- OCR tools
	- Data formats and structures in the humanities (CSV, JSON, XML)
	- Data acquisition: web scraping with scripts / scraping software, APIs, archives
	- Data cleaning and preprocessing (missing values, outliers and inconsistencies)

- Part II: Populating and managing data with some database schemas
	- Introduce the advantages of NoSQL on digital humanities projects
		- Flexibility and schema-less design
		- Ability to handle numerical metadata for data, such as location values for geo-spatial data, embedding values for data that was processed by machine learning 
	- MongoDB basics:
		- Creation and maintenance of database
		- CRUD operations in MongoDB
	- Database integration:
		- Establishing pipelines/interface of the database so that the database can be integrated to the workflow of other groupmates .

- Part III: Machine learning 
	- Introduction to machine learning concepts
		- Supervised / unsupervised learning
		- (Text / image /music) encoding / decoding
		- Types of neural networks 
		- Code exercises using popular machine learning libraries
	- Embeddings as the final product of machine learning
		- Class activities:
			- Display text, images embeddings from model
			- Calculate similarity score with embedding values 
			- Evaluate models using embeddings
	- Applying machine learning to humanities data
		- Text classification, sentiment analysis
		- Text translation with `huggingface-transformer`
		- Named entity recognition with `stanza`
		- Image data:
			- Image-to-text-caption with hugging-face "image captioning" module
		- Image recognition to categorize and tag images 
		- Topic modeling
		- Text summarization
		- Style analysis
		- KNN for clustering

- Part IV: Analysis from data
	- Exploratory data analysis:
		- Retrieving data from MongoDB and perform exploratory data analysis for uncovering patterns and insights.
	- Visualization
		- Scikit-plot:
			- creating machine learning plots, such as confusion matrices, ROC curves 
		- Streamlit:
			- Create web applications with interactive visualizations, machine learning dashboard
	- Communicating research findings through compelling visual narratives.
	- Final project presentations: Students demonstrate their skills by presenting their group projects, incorporating MongoDB data, machine learning insights, and effective data visualizations.

---
### Possible digital humanities projects that students can work on:


|            | Digitizing Historical Artifacts | Literature Text Analysis | Art History Image Classification | Cultural Heritage Text Translation |
|------------|---------------------------------|-------------------------|---------------------------------|------------------------------------|
| Part 1     | Collect historical documents, digitize them using OCR tools, and organize them in digital formats. | Scrape literary texts from public domain sources, clean and preprocess the text data. | Collect a dataset of art images from various time periods and artists. | Collect multilingual historical texts related to cultural heritage. |
| Part 2     | Create a NoSQL database to store the digitized artifacts, including metadata like date, artist, and location. | Create a NoSQL database to store the literary texts and their metadata, allowing for efficient retrieval and analysis. | Create a NoSQL database to store art images and associated metadata, such as artist, style, and location. | Create a NoSQL database to store multilingual texts and their translations. |
| Part 3     | Implement machine learning models to categorize and tag images of the artifacts based on their style and content. | Apply sentiment analysis and topic modeling to the literature texts to uncover themes and sentiments within different works. | Implement image classification using neural networks to categorize art pieces by style and artist. | Utilize transformer models (e.g., Hugging Face) to perform automated translation of historical texts between languages. |
| Part 4     | Develop interactive visualizations showcasing the historical artifacts' evolution over time and artists' styles. | Develop a web application using Streamlit to visualize the evolution of literary themes and sentiment over time. | Develop a machine learning dashboard using Streamlit to allow users to explore and classify art images interactively. | Develop a tool to visualize and compare translations, allowing users to explore the cultural context of the texts. |

This table format provides a clear overview of the different projects and their respective project parts.

---
- reference book:
	- [Book review - Introducing data science](../Book%20review%20-%20Introducing%20data%20science.md)


---

### A more detailed syllabus (Old)

- Course: Programming for humanists
	- Introduction (Lecture 1) 
	- Overview of the course
	- Writing and reading object-oriented programming (get familiar with the style of programming that hiding details)
		- Writing and reading object-oriented programming
			- Purpose: (get familiar with the style of programming that hiding details)
		- Data
			- Types of data
				- Unstructured data
					- Images
					- Articles
				- Structured Data
					- Geo-spatial data
					- Time series data
			- Source of data
				- Online databases
				- Digital archives with curated historical documents
		- Introducing components of a digital humanity project
			- "Front-end / presentations" components (most of the content in the course 1, HIST4702)
				- Websites
				- Charting, visualization
			- "Back-end / analytics"  components (The focus of this subject)
				- NoSQL Database
				- Programming scripts 
				- Machine learning tools 
					- Embeddings
					- Transformers
		- Installations and registrations of accounts
			- Github:
				- Register Github student developer pack and getting free github copilot
			- Huggingface
		- Toolkit discovery as a programmer
			- Ways of using github, huggingface, stackshare to explore suitable tools for the digital humanity project

	- Programming as a "Back-end" knowledge of a digital humanity (DH) projects 
		- 1. Getting / accessing / populating data (Should be remove old technology pipelines)
			- Introduce:
				- script packages such as beautiful-soup, selenium
				- knowing how to work with external data, such as HTML, XML, JSON
				- pre-built scraping software such as octoparse
			- REST API of websites, such as twitter
			- Understanding principles of organizing a corpus / unified dataset
			- Understanding structure of database

		- 2. Managing data with MongoDB 
			- Read: Data querying and searching
			- Write: Host and curate collections of historical documents
				- NoSQL database (mongoDB)
				- (digital archives and repositories)
			- Clean: Data cleaning packages 
			- Discuss effective task separation before start working the programming. Github copilot prompting and Coding regarding to mongoDB

		- 3. Data parsing and transformation (preprocessing, labelling)
			- Creating labels
				- NLP preprocessing with spaCy etc
				- Named-entity recognition 
			- Machine translation

		- 4. Analysis from data
			- Existing embeddings
				- OpenAI embeddings
				- Open-source embeddings from hugging-face
				- HistWords: word embeddings for historical text
					- https://nlp.stanford.edu/projects/histwords/
					- It is an open-sourced package
			- Fundamental tasks
				- Topic modeling (introducing clustering, LDA)
				- Text analysis (with established packages such as BookNLP)
				- Sentiment analysis
				- KNN for clustering 
			- Application level tasks:
				- https://huggingface.co/tasks

		- 5. (Self-teaching / part of assignment) Publishing scripts, data into the internet
			- Github, huggingface
				- Documentation, version control skills with github functionalties
				- Knowing the specifications and demands from "front-end" part of DH projects
			- Other website that hosting digital humanities data