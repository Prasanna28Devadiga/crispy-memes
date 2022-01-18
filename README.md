<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->




<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/logo.png" alt="Logo" >
  </a>

  <h3 align="center">Meme Generation using GPT-3</h3>

  
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project


This project has been an attempt at using SOTA Language models to create Memes.
The entire process is carried out in 6 steps
1. We scrape memes from particular templates
2. we then pass these memes into an OCR, which we built using the easyocr library, to extract the text and write these into documents based on the template used. These documents form the dataset for our model to perform generation on. It is important to note that GPT-3 uses few shot learning , which is why it works well even with tiny datasets. Models of this size cant be possibly fine tuned by the masses which is why we use "prompt engineering" to teach it to perform tasks.
3. We next pass on the documents to our model to perform text generation. It is incredibly difficult to write good prompts, and hence this stage requires plenty of handcrafting.
4. This step involves removing noise from the output. As our prompts can’t be a 100% representative of our task (in our case that would be generating meme text) , there is an addition of unnecessary text in our outputs. 
5. In the fifth step we pass the clean outputs to the Imgflip api to generate the memes. 
6. In the sixth step we download these memes to a folder which we then serves as a database for our twitter bot. Our twitter bot continues to post these in random intervals for users to enjoy.

Stats:
1. We generated enough meme text for about 20,000 memes.
2. We were able to create ~1000 memes before hitting the api limit for the day.


### Built With

This section should list any major frameworks that you built your project using. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.
* [Python](https://www.python.org/)
* [GPT-3](https://beta.openai.com/)

## Twitter Bot Handle

This is the [link](https://twitter.com/JennyTa06647874) to the twitter bot handle which is automated to post the memes generated


<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a list of proposed features (and known issues).



