# Training for Generatively Pretrained Transformer (GPT)

<div id="top"></div>
<div align="center">
  
  

![](https://img.shields.io/badge/Language-Python-blue)



  
</div>



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/mstatt/NLP-training-for-Generatively-Pretrained-Transformer-GPT-">
    <img src="assets/falcons-logo2.png" alt="Logo" >
  </a>
</div>

  <p align="center">
    A basic project to derrived from "Let's build GPT: from scratch, in code, spelled out." by Andrej Karpathy: (https://www.youtube.com/watch?v=kCc8FmEb1nY).
    <br />
</p>
  <p align="center">

Generative pre-trained transformer (GPT) is a family of language models generally trained on a large corpus of text data to generate human-like text. They are built using several blocks of the transformer architecture. They can be fine-tuned for various natural language processing tasks such as text generation, language translation, and text classification. The "pre-training" in its name refers to the initial training process on a large text corpus where the model learns to predict the next word in a passage, which provides a solid foundation for the model to perform well on downstream tasks with limited amounts of task-specific data.
  
       <br />
  </p>








<!-- Notes -->
## Some Notes
<p>
Below are some notes on execution times and feature edits to update performance and accuracy of the model. </br>
 I replaced the tiny shakespeare dataset with the currated Big Bang Theory season 1-8 transcript dataset.

</br>
Here are the local machine GPU (NVIDIA GeForce RTX 2080 Super) training time in ( HH:MM:SS ) format:</br>
<ol>
<li>Execution time: 00:02:20  for  100  iterations.</li>
<li>Execution time: 00:04:37  for  500  iterations</li>
<li>Execution time: 00:07:42  for  1000  iterations</li>
<li>Execution time: 00:38:34  for  5000  iterations</li>
<li>Execution time: 01:17:35  for  10000  iterations</li>
</ol>
</p>
</br>
Some features to manipulate for performance testing are as follows. For in depth explanation see Mr. Karpathy's video on the effects of these values. </br></br>
<ol>
<li>** More text training data **</li>
<li>batch_size</li>
<li>block_size</li>
<li>max_iters</li>
<li>learning_rate</li>
<li>n_head</li>
<li>n_layer</li>
</ol>




<p align="right">(<a href="#top">back to top</a>)</p>



<!-- Enhancements -->
## Enhancements
<p align="center">
Below are some basic enhancements that could be done to make this better.
</p>
<ol>
<li>Functionality to Save the model.</li>
<li>Functionality to Reload the saved model.</li>
<li>Additional data added to the training text. <br/> I got the original text from (https://bigbangtrans.wordpress.com/) and included the (remove-line-that-begins-with.py) file to assist with data clean-up.</li>
</ol>




<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you want, feel free to fork this repository. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/YourFeature`)
3. Commit your Changes (`git commit -m 'Add some YourFeature'`)
4. Push to the Branch (`git push origin feature/YourFeature`)
5. Open a Pull Request
<br />
See the https://github.com/mstatt/NLP-training-for-Generatively-Pretrained-Transformer-GPT-/issues for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

![](https://img.shields.io/badge/License-MIT-blue)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Project Link: [https://github.com/mstatt/NLP-training-for-Generatively-Pretrained-Transformer-GPT-]


<p align="right">(<a href="#top">back to top</a>)</p>

