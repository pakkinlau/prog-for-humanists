Reference:
1. Introduction to Modern Databases with MongoDB: https://drive.google.com/drive/folders/1U9WPFkIKBLELqHj7mfh76Bw1u5eFpwqg

Database
- Why learning database?
	- Efficient data management:
		- Our memories are fallible, and relying on them alone can lead to important information being forgotten or lost.
		- Database is a way to ensure our dataset can be effectively retrieved by indexing, querying and aggregating. 
	- Streamlined data interaction:
		- When programming script interacts with raw datasets with no indexing. The process are slow. 
		- By leveraging indexing, querying, and aggregating capabilities, individuals can extract valuable insights from large datasets.
	- Data Consistency and Integrity:
		- Maintaining data consistency and integrity is crucial for any organization. Inconsistencies and errors in data can lead to flawed analysis, decision-making, and operational inefficiencies.
		- Databases provide mechanisms such as data constraints, relationships, and transactions to ensure data accuracy and reliability. By learning about databases, individuals acquire the knowledge to enforce data integrity rules, establish relationships.

![](../../Pasted%20image%2020231217145720.png)

Why NoSQL?
- Deals with polymorphic data
	- You are able to store differently shaped data in the same collection
- Works well with rapidly changing data
	- Each shape change in the structure of the data requires to the database's corresponding schema if stored in a relational database. 

MongoDB
- Features:
	- API query or query language:
		- It allows developers interact with the database programmatically, using their preferred programming language. 
	- Distributed and resilient:
		- Higher availability and resiliency as the data lives in replica sets. 
	- Flexible schema
	- Object mapping:
		- Documents easily map to objects. And objects are the most frequently used data structure in the most popular programming languages. This allow developers to rapidly develop their app in intuitive way.
- Why choosing mongoDB?
	- Flexibility with Polymorphic Data
		- MongoDB is designed to handle polymorphic data, which means it can accommodate different data structures and formats within the same database collection. This flexibility is particularly useful in scenarios where data may vary across documents or where schema evolution is frequent.
	- Easy mapping of the data to/from programming language
		- The document-based nature of MongoDB aligns well with object-oriented programming, allowing developers to store and retrieve data in a way that feels natural and intuitive. 
	- High performance database
	- Rich Querying Capabilities

Documents
- For modeling and querying in the manner you want to perform them.

Document model:
- Similar to dictionaries in python, using key-value pairs to store information. 
- Tabular data model (in SQL)
	- Related data is split across multiple records and tables 
- Document data model
	- Related data is contained in a single, rich document
	- The main difference is that column names are appearing in each documents, allowing for greater flexibility in having document with different shapes (or, having different fields)
```
{
"_id": ObjectId(
"5f4f7fef2d4b45b7f11b6d7a"),
"user_id": "Sean",
"age": 29,
"Status": "A"
}
```

Document model constraints 
- Fields (attributes)
- Sub-documents (objects)
	- It allows one-to-one relationship
- Arrays (a chain of attributes)
	- It allows one-to-many relationship

---


CRUD operations

As a developer data platform
- Storing data
- Accessing data
- Processing data

MongoDB architecture
- Query layer
	- The first layer a request gets processed by and it adds the query shape and an index if applicable. 
	- Query analyzers determine the shape of the query, then determine what index, if any, fit the query. If it does fit, it is cached. 
- Data model layer
	- The layer where the requests receives the set of documents that it will request from the storage layer.
	- This layer has no knowledge of specifications of documents but it does understand indexes 
- Storage layer
	- The layer that deals with getting the specific documents from memory or from the disk, and passing the response back to the layer above it. 


MongoDB atlas
- Clusters:
	- It means a group of servers that stores your data
- Replica set:
	- A replica set is the basic building block for clusters. 
	- A few connected mongoDB instances (instance = single machine) that store the same data 
- Atlas:
	- A software that runs all the scaffolding to manage all of the clusters, and providing additional services/features. 
	- Atlas use Amazon/google/Microsoft cloud providers. 

---
- Atlas sample dataset:
	- Documents: https://www.mongodb.com/docs/atlas/sample-data/

Atlas data explorer
- CRUD operations on documents
- Manage indexes
- Create and run aggregations 

Atlas search
- Fuzzy search
- Autocomplete
- Filters and facets
- Multi-data type support
- Multi-language support
- Highlighting
- Custom scoring
- Rich querying language

Atlas organization / projects 
- Organizations relate to billing
- Projects are best associated to teams 


---
Querying in mongoDB
- MQL
- MongoDB aggregation framework

- Familiar with "the skill of reading documentation":
	- https://www.mongodb.com/docs/manual/tutorial/project-fields-from-query-results/


---
MQL (Lesson 11-14)


---

Aggregation framework (15-16)
- Reference: https://www.mongodb.com/docs/manual/aggregation/

- Aggregation means process multiple documents and return computed results. 
	- Group values from multiple documents
	- Perform operations on the grouped data to return a single result
	- Analyze data changes over time
- Aggregation pipeline
	- It consists of one or more stages that processes documents
	- Each stage can perform an operation, such as filter (with `$match:{}`), group (with `$group:{}`), sorting (with `$sort`), calculate values. 
	- Additional pipelines: `$out`, `$merge`, `$geoNear`
---
Data modeling

---

Index (Lesson 19)
- Single field 
- Compound index
- Multikey index
- Geospatial index
- Text index
- Hashed index
- Time-to-live index
- Hidden index
- Partial index
- Wildcard index

---
vector search
- why we need it?
	- It allow you to find related objects that have a semantic similarity. This means searching for data based on meaning rather than the keywords present in the dataset. 
	- Vector transform unstructured data into numeric representation that captures the intent and meaning of that data. 
	- Query finds related content by comparing the distance between these vector embeddings. 

- Tutorial: https://www.mongodb.com/developer/products/atlas/building-generative-ai-applications-vector-search-open-source-models/
	- Step 1: Connect your MongoDB instance 
	- Step 2: set up embedding creation function
		- `all-MiniLM-L6-v20` model from hugging face
	- Step 3: Create and store embeddings
	- Step 4: Create a vector search index
	- Step 5: Query your data

- Bonus tips in the tutorial page:
	- Hugging face inference endpoints
		- On the model page in hugging face, click on "Deploy" and in the dropdown choose "Inference Endpoints."
		- In atlas, click on "create a new endpoint" and insert a new endpoint. 
		- It would cost about 0.06$ per hour. 
		- Click on the advanced configuration and choose the task type to "sentence embeddings". This ensures the endpoint returns the response from the model that is suitable for the embedding creation task. 