
# Part 1 of 5 - Deciding the architecture 
#### Multi-layer perception (MLP)

When we build a multi-layer perception (MLP), the neural network 

- Design questions
  - How many layers?
  - Dimension of each layers?
  - How to design the output layer?
  - Fully or partially connected layers?

#### Activation function 
- Binary classification problem:
	- Choice:
		- Sigmoid
		- Hyperbolic tangent ($tanh$)
	- They have parabolic shape and the output of these function squashes to the range $(0,1)$ and $(-1,1)$. 
- Multi-class classification problem:
	- Choice:
		- Softmax function 
	- The softmax function normalizes the output of a network to a probability distribution over multiple classes. 
- Hidden layer:
	- Choice:
		- ReLU, 
		- other modifered ReLU (Lecky ReLU, Parametric ReLU, Exponential ReLU)
	- ReLU is given by $f(x) = max(0,x)$. It is outputting the input directly if it is positive; otherwise, it outputs zero. It helps with the vanishing gradient problem and is computationally efficient.
	- the discontinuity at $x=0$ introduces nonlinearity. This nonlinearity is crucial for the expressive power of neural networks, allowing them to model and learn complex relationships in data that linear functions alone would not be able to capture.

---

Model construction in python

![](../../Pasted%20image%2020231114173141.png)

---
# Part 2 of 5 - Deciding the learning process
## Learning process

- The essence of neural network learning lies in adjusting the weights and biases associated with each connection.
- Initially, the weights are randomized.
- 1. **Feedforward Propagation:**

  - The input to the k-th neuron in a layer is calculated using the activation function:
    $$
    \text{Input}_{k} = \text{Activation}\left(\sum_{i=1}^{N} (\text{Input}_{i} \times \text{Weight}_{ki}) + \text{Bias}_k\right)
    $$
![](../../Pasted%20image%2020231114154200.png)


- **Cost function:**

  - Learning in a neural network involves minimizing a cost function that measures the difference between the predicted output and the actual output. Cost function is the basis of gradient descent, which is 
  
  - **Cost function for Regression:**
    $$
    \text{Cost} = \frac{1}{2m} \sum_{i=1}^{m} (\text{Prediction}_i - \text{Actual}_i)^2
    $$
    It is a typical form of the mean squared error (MSE) cost function. 

  - **Cost function for Classification:**
  - The cost function for classification is given by:
    $$
    \text{Cost} = -\frac{1}{m} \sum_{i=1}^{m} \left[ y_i \log(\hat{y}_i) + (1 - y_i) \log(1 - \hat{y}_i) \right]
    $$
- The derivation of this expression could be referred to this video: https://www.youtube.com/watch?v=0DqnDGV_p9c 

  - For a regression problem, the hypothesis function is given by $h(\mathbf{x}) = \theta_0 + \theta_1 x$, and the corresponding cost function is the mean squared error (MSE) as defined above. So cost function becomes: $$\text{Cost} = \frac{1}{2m} \sum_{i=1}^{m} (\theta_0 + \theta_1 x_i - \text{Actual}_i)^2$$
  - The derivation of this expression could be referred to this video:  https://www.youtube.com/watch?v=x9I3eJ-Wb2s
- ---


   - **Gradient Descent:**
	- Gradient Descent finds the slope of the cost function that we discussed in the previous section to find the direction of reaching lower error rate. 
     $$
     \frac{\partial \text{Cost}}{\partial \text{Weight}_{ij}} = \frac{1}{m} \sum_{k=1}^{m} (\text{Prediction}_k - \text{Actual}_k) \times \frac{\partial \text{Output}_{k}}{\partial \text{Weight}_{ij}}
     $$
          (Here, $\frac{\partial \text{Output}_{k}}{\partial \text{Weight}_{ij}}$ is the derivative of the output signal with respect to the weight in the network.)

![](../../Pasted%20image%2020231114161249.png)
![](../../Pasted%20image%2020231114161332.png)


---

- 3. **Backpropagation:**

  - It is a supervised learning algorithm that fine-tunes the weights by propagating the error backward through the network.
  - **Backward Pass:** Error propagated backward through the network. Each weight's contribution to the error is determined, and the weights are adjusted accordingly.
    $$
    \text{Error}_{k} = \text{Activation}'(\text{Input}_{k}) \times \sum_{j=1}^{M} (\text{Error}_{j} \times \text{Weight}_{kj})
    $$
  - **Update Weights:** The weights are updated based on the calculated errors, and the process is repeated until the model converges to a state where the cost function is minimized.
    $$
    \text{Weight}_{ij} = \text{Weight}_{ij} - \text{LearningRate} \times \frac{\partial \text{Error}_{j}}{\partial \text{Weight}_{ij}} \times \text{Input}_{i}
    $$
  - The learning rate determines the size of the steps taken during each iteration.
  - This process is repeated until the model converges to a state where the cost function is minimized.

![](../../Pasted%20image%2020231114161420.png)

---
## Part 3 of 5 - Evaluating the learning outcome 

![](../../Pasted%20image%2020231114174001.png)

- In underfitting model, both training and validation errors remain high. It is because the model training from training data set already could not good classification.
- In overfitting model, the model tries to outline a complex curve to capture the pattern from training data, but when this complex boundary applies on the prediction on unseen data, it would very possibly having large error because the boundary was overfitting the nuance in training data. 
- In optimal fitting, interpretable patterns are extracted and high order terns that tries to capture nuance patterns are penalized. Low training error and validation error rate are both achieved.




---
## Part 4 of 5 - Neural network architecture 

#### recurrent neural network (RNN) (each node feeds back on itself)

![](../../Pasted%20image%2020231114182323.png)

- The nature of neurons cells within RNN connected to themselves allow RNN to feedback to itself. 
- RNNs are characterized by their ability to maintain a hidden state or memory that is updated at each time step. This hidden state serves as a form of memory, allowing the network to retain information about previous inputs and utilize it in the processing of subsequent inputs. This inherent memory capability enables RNNs to excel in scenarios where context and order matter.
- This cyclic connection allows RNNs to capture and process sequential information, making them particularly effective for tasks that involve a temporal component. 
- Such controlled states in RNN are referred to as gated state or gate memory
- Application:
	- Natural language processing
	- Time series prediction
	- Speech recognition
#### auto-encoder (AE) (contains encoder (by dimension reduction))  and decoder (by dimension addition)

![](../../Pasted%20image%2020231114182308.png)

- The dimension of input and output layer are matched. 
- This model tries to learn a representation for a set of data, for the purpose of dimensionality reduction. For example, we have an input data that has 100 dimensions and the hidden layer of AE has only 40 dimensions. AE would tries to capture the most important 40 dimension of data in order to minimize the loss and improving its prediction. 
- Application:
	- Data compression, Speech recognition

#### Generative Adversarial Network (GAN) (Generative Network, Discriminative Network)

Generative Adversarial Networks, or GANs, are a class of artificial intelligence algorithms introduced by Ian Goodfellow and his colleagues in 2014. GANs consist of two neural networks - the generative network and the discriminative network - which are trained simultaneously through adversarial training.

![](../../Pasted%20image%2020231114175848.png)

- **Generator / Generative Network:**
  - The generative network, often referred to as the generator, is responsible for creating new data instances that resemble a given dataset. It takes random noise as input and generates samples that ideally cannot be distinguished from real data by an external observer.
  - The output generated by the generator is "fake data / synthetic data". 
  - The generator continuously improves its ability to produce realistic data by learning from the feedback of the discriminative network.

- **Discriminative Network:**
  - The discriminative network, or discriminator, evaluates whether a given input is real (from the actual dataset) or fake (generated by the generator). Its objective is to correctly classify the origin of the input data.
  - The discriminator is simultaneously trained to become more adept at distinguishing between real and generated samples.

- **Adversarial Training:**
  - The training process involves a continuous back-and-forth between the generative and discriminative networks. The generative network aims to create more realistic data to fool the discriminator, while the discriminator aims to improve its ability to distinguish between real and generated data.
  - This adversarial process leads to the improvement of both networks over time.

- **Applications:**
  - GANs have found applications in various domains, including image generation, style transfer, image-to-image translation, and even the generation of synthetic data for training other machine learning models.
  - Examples include generating realistic images of faces, creating art, and transforming satellite images into maps.

---
## Part 5 of 5 - Improving performance 

- Dropout 
- Regularization
- Batch normalization
- Early stopping