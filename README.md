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
    Keep in mind this is a substantially smaller version that the popular model deployed by OpenAI.
</p>
  <p align="center">

Generative pre-trained transformer (GPT) is a family of language models generally trained on a large corpus of text data to generate human-like text. They are built using several blocks of the transformer architecture. They can be fine-tuned for various natural language processing tasks such as text generation, language translation, and text classification. The "pre-training" in its name refers to the initial training process on a large text corpus where the model learns to predict the next word in a passage, which provides a solid foundation for the model to perform well on downstream tasks with limited amounts of task-specific data.

  </p>








<!-- Notes -->
## Some Notes
<p>
Below are some notes on execution times and feature edits to update performance and accuracy of the model. </br>
 I replaced the tiny shakespeare dataset with the Coca dataset. Located here( https://www.corpusdata.org/formats.asp )
</br>
</p>
Here are the local machine GPU (NVIDIA GeForce RTX 2080 Super) training times for >19 Million parameters, (training data set size and system specs could alter this substantially):</br>
<ol>
<li>Execution time: 00:09:39 for 1,000  iterations.</li>
<li>Execution time: 01:22:11 for 5,000  iterations</li>
<li>Execution time: 02:21:46 for 10,000  iterations</li>
<li>Execution time: 03:33:02 for 15,000  iterations</li>


</ol>

</br></br></br>
Some features to manipulate for performance testing are as follows. For in depth explanation see Mr. Karpathy's video on the effects of these values. </br>
<ol>
<li>** More text training data **</li>
<li>batch_size</li>
<li>block_size</li>
<li>max_iters</li>
<li>learning_rate</li>
<li>n_head</li>
<li>n_layer</li>
</ol>
</br></br></br>
If you want to run a reloaded model. Please see the process below: </br>
<ol>
<li>Run the imports Cell to ensure all of the libraries are loaded</li>
<li>Execute Steps 1-5 prior to loading the model or testing the output.</li>
<li>Ensure that the same data file used for training the model is loaded.</li>
<li>Specifically the same text training data file with the same sentence length as the one used for training.</li>
<li>Load the specific model you want from the directory.</li>
<li>Run the Generate text from the (GPT) model cell.</li>
<li>**** All of the models provided here were trained with the same params and data file, </br>the only thing I changed was the number of iterations. ****</li>
</ol>
</br></br>
|:-------------------------
Model flow diagram.
 -------------------------:|


![A1]


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- Enhancements -->
## Enhancements
<p align="center">
Below are some basic enhancements that could be done to make this better.
</p>
<ol>
<li>Additional data added to the training text. <br/> Great text data resource (https://www.corpusdata.org/formats.asp) and I have included the (clean-training-text.py) file to assist with data clean-up and formatting.</li>
<li>The script cleans up stray chars and formates the files, then merges both the soap and the news text for a single clean larger corpus. With adjustable line length for better results when tuning the model.</li>
<li>If you run the notebook and script (as is) or use the included (merged-final-training-text-formatted.txt  --unchanged) that will give you 19.03 Million parameters to start.</li>

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



<!-- MARKDOWN LINKS & IMAGES -->
[A1]: assets/model.png