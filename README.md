# User Guide for CSS NLP Lab Notebooks

## Contents
0. [Getting the Code and Data](#download)
1. [Enviornment Setup](#setup)
2. [Using Lab Exercises](use)
    - [Short Summaries of each Lab](#summary)
    - [Lab 0: Intro to python & text](#zero)
    - [Lab 1: Data munging](#one)
    - [Lab 2: Word frequencies](#two)
    - [Lab 3: Topic modeling](#three)
3. [Suggested Readings](#readings)
4. [License](#license)    

## 0. Getting the Code and Data <a name="download"></a>
To use these labs, you will need to download the code and the data. These are available for free online in a GitHub repository with steps below: 

- Go to this page on a web browser: https://github.com/UM-CSS/CSSLabs-NLP
- If you are familiar with `git`, we recommend you clone the repo.
- If you are unfamiliar with `git`, the easiest option is to follow these steps:
    - Press the ![Clone or download](images/clone_or_download.png "Clone or download") button on the right side of each repository.
    - Choose `Download ZIP` and save the file somewhere memorable.
    - Go to where the file is saved and unzip it.

## 1. Environment Setup <a name="setup"></a>

You will need some software to be able to run this code. Advanced users may view the required libraries in the [README](README.md) file. For all users, we recommend the following:
1. Install [Docker Desktop](https://docs.docker.com/desktop/) on the laptop or desktop computer.  Here are direct links for various operating systems: [Mac OS](https://docs.docker.com/desktop/install/mac-install/), [Windows](https://docs.docker.com/desktop/install/windows-install/), [Linux](https://docs.docker.com/desktop/install/linux-install/). 
2. We are using [Jupyter notebook on Docker Stack](https://jupyter-docker-stacks.readthedocs.io/en/latest/) to avoid steps to install various components. With the Docker Desktop installed in above step, now we can load a docker container directly by:
    - Open a terminal on Mac OS or the Commandline Prompt on Windows, and navigate to the folder where you downloaded the notebook in step 0 above.

        - If you are a Mac user, run the following command:
        ```bash
        docker run -v $(pwd):/home/jovyan/CSSLabs-NLP -p 8888:8888 quay.io/jupyter/scipy-notebook:2024-01-05
        ```

        - If you are a Windows Command shell user, use this command:
        ```bash
        docker run -v %cd%:/home/jovyan/CSSLabs-NLP -p 8888:8888 quay.io/jupyter/scipy-notebook:2024-01-05
        ```

        - If you are a Windows PowerShell user, use the following command:
        ```bash
        docker run -v ${PWD}:/home/jovyan/CSSLabs-NLP -p 8888:8888 quay.io/jupyter/scipy-notebook:2024-01-05
        ```
           
    - The above step will first pulling the docker container from the remote repository.  You should see a list of layers of this container being pulled off the remote repo. Notice, the image pulling steps only happens when this is done for the first time.  Once the pulling is completed, it will run the container on your local operating system, and expose a port 8888 on your local host, with a token, i.e. ```b045...61e4``` in the following case.  

    ```
    ...
    aef40af6dc3e: Pull complete 
    3c01e088ac39: Pull complete 
    Digest: sha256:162744a05b15a0bcad1064238af48b0e4e6bcb56f1e4cc607f34343ee3a0f728
    Status: Downloaded newer image for quay.io/jupyter/scipy-notebook:2024-01-05
    Entered start.sh with args: jupyter lab
    Running hooks in: /usr/local/bin/start-notebook.d as uid: 1000 gid: 100

    ...

    [I 2024-01-05 21:07:36.315 ServerApp] Serving notebooks from local directory: /home/jovyan
    [I 2024-01-05 21:07:36.315 ServerApp] Jupyter Server 2.12.2 is running at:
    [I 2024-01-05 21:07:36.315 ServerApp] http://bda4c6f01885:8888/lab?token=b045793e8e725f79808eb241136cf80294ba94d86c8f61e4
    [I 2024-01-05 21:07:36.315 ServerApp]     http://127.0.0.1:8888/lab?token=b045793e8e725f79808eb241136cf80294ba94d86c8f61e4
    [I 2024-01-05 21:07:36.315 ServerApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
    [C 2024-01-05 21:07:36.317 ServerApp] 
        
        To access the server, open this file in a browser:
            file:///home/jovyan/.local/share/jupyter/runtime/jpserver-7-open.html
        Or copy and paste one of these URLs:
            http://bda4c6f01885:8888/lab?token=b045793e8e725f79808eb241136cf80294ba94d86c8f61e4
            http://127.0.0.1:8888/lab?token=b045793e8e725f79808eb241136cf80294ba94d86c8f61e4
    ```

3. If you see the above terminal completed with above output and waiting for input, congratulations! you have successfully installed docker container that  you need. If not, there is something wrong with your installation, and please ask one of the instructors for help.  Use a web browser to access the above URL with the token from your local machine, i.e. you have to copy the similar string from your output with your TOKEN string and replace following one. If not, you might be given a prompt to copy/paste the token on the first webpage. 
    ```
    http://127.0.0.1:8888/lab?token=xxx
    ```

4. In the jupyter lab environment we have created above, you should see a list of files and folders on the left of the webpage, and Notebook, Console, and Others to the right side of the page. Navigate through the left file browser to the `CSSLabs-NLP` folder.  In this folder is a list of lab files ending in `.ipynb`, stands for Interactive (i) Python (py) Notebook (nb). Click on any of these and they should open in a new Notebook tab with the lab code and instructions.
    - **Note** if you get an error or the top of the new page does not look like this 
        - ![notebook top](images/notebook_top.png "notebook top"), 
        - Then you have probably made a mistake in downloading the files. Go back to the "[Getting the Code and Data](#download)" instructions. 
5. If you are new to Jupyter Notebooks, everything you need for these labs is in the great [introduction to their basic use](http://nbviewer.jupyter.org/github/jupyter/notebook/blob/master/docs/source/examples/Notebook/Notebook%20Basics.ipynb).

6. **Optional notebook extensions**: The labs were designed to work with the `collapsible headings` extension. They work fine without it, but look a little nicer if you have it installed. Full installation instructions are [at the bottom of this link](https://github.com/ipython-contrib/jupyter_contrib_nbextensions). Here's the short version:
    1. In `anaconda prompt` or your terminal, run this command: `conda install -c conda-forge jupyter_contrib_nbextensions`
    2. In the same prompt, run `jupyter nbextensions_configurator enable`
    3. In the same prompt, run `jupyter nbextension enable collapsible_headings/main`
    2. Restart Jupyter Notebook.


## 2. Using Lab Exercises <a name="use"></a>
**Note** Labs 2 and 3 require you to first run the code in Lab 1. You may simply run the code in Lab 1 without looking at it and skip to labs 2 or 3 if you like. (Be sure to check for errors when you run Lab 1: if there is something wrong with your setup, it will show up here. Lab 1 has detailed instructions for common errors.)

### Short Summaries of each Lab <a name="summary"></a>
- Lab 0 introduces both the python programming language and how computers think about text. It assumes no prior knowledge of programming. It is not a comprehensive course in either programming or text processing, but rather a quick, gentile start designed to help new users up and running with the basics.
- Lab 1 walks students through cleaning the OKC profile data. Data are often messy when researchers first get them; indeed munging is usually the largest component of any data science project.
- Lab 2 gets students thinking about text as data. By the end, students compare word frequencies across different social groups to see what aspects of their language use are distinctive.
- Lab 3 introduces students to topic modeling. They construct topic models, interpret the topics, evaluate their quality, and explore the relative popularity of topics across social groups. 

### Lab 0: Intro to python & text <a name="zero"></a>
- This lab sets out to teach people who have never seen programming before two things:
    1. Enough python to use and understand the other labs
    2. Enough about how computers understand text to make sense of the other labs
- As such, it focuses heavily on developing intuition rather than explaining full technical details or rationals. Further, it leaves out a lot of what normally would be covered in an intro to programming or intro to python course. 

### Lab 1: Data munging <a name="one"></a>
#### Data reminder
- For this lab to work, you'll need to follow the instructions above for "getting the code and data."

#### As a prerequisite for other labs
- If you are only running this lab in order to get the clean profiles data for one of the other labs:
    - You can click `cell` -> `Run All` at the top of the notebook.
    - Be sure to scroll through the whole notebook to make sure that it finishes running all the way to the bottom without errors. If there are errors or the notebook does not finish, you will not be able to do the next labs. 
    - The most common errors, and how to fix them, are explained in the notebook.


### Lab 2: Word frequencies <a name="two"></a>
#### Initial Setup
- This lab uses the `clean_profiles.tsv` file produced by `Lab 1`. You will need to run that code first, or get a copy of the file it creates from someone who has. 
    - If you get an error that says something like `FileNotFoundError: File b'data/clean_profiles.tsv' does not exist` at the bottom, if means that you need to run the code in Lab 1. If you already ran this code and still get this error, then check for error messages in Lab 1. 
- If you have run this lab or used `nltk` before, you should comment out the `nltk.download()` line in the imports code.
- If you are running this code on a personal computer or laptop:
    - Run the code under the header "For laptop and personal computer users." 
    - This takes a smaller sample of the data. Otherwise, the data is too big for most personal computers and causes them to crash. 

#### Helper functions
- This lab, like the others, has code labeled "helper functions." 
- This code is not explained in the notebook because it is not a central part of the lesson.
- Students should run these code cells and scroll past them without worrying about how they work. 

#### Stop words
- This lab changes the standard English set of stop words so that pronouns are not removed from the text. This decision was informed by the work of James Pennebaker and others, which shows that pronoun frequency can be very informative.
- It turns out that pronoun frequencies aren't very distinctive of different groups within this data set. We would see similar results if we used the default list of stop words and excluded pronouns. 
- The lab still does not use the default set of stop words in order to show students more about what stop words are and that they should not be used uncritically. 

#### Cleaning text
- There is a list of `bad_words` in the text cleaning function. This is a bit of a hack solution to the fact that `beautifulsoup`, although it is a great HTML parsing library, does not quite remove all links from our text. Without this, the words `http` and `www` clutter the results. `\nnan` is removed also, because every empty text box leaves that artifact.

#### Sex/gender 
- The OKC data has a column `sex` with categories `m` and `f`. There is no column or category to indicate gender identity or intersex identity. 
- The lab generally refers to these groups as "men" and "women." This is likely how most people interacted with the site when making their profiles. It is also how most students will interpret the sex data. It is not perfect. 
- If students raise the problems with this data, it is a great opportunity to pose to them research questions: 
    - Given that OkCupid has constraining options, how might trans, genderqueer, and enby people interact with it?
    - Do words like `transgender` appear in the profile text? (yes)
        - What sex do those individuals pick, and how does it relate to what they write in their profiles? (it depends)

#### "4. Your turn to try it with another trait"
- Suggestions of traits that work out well:
    - Age_group
    - Education
    - Orientation (sexuality)
    - Sex
- Other notable things
    - In the race/ethnicity variable, there really aren't strong differences between groups. This could be the starting point for an interesting discussion, especially since research shows strong racial discrimination and assortativiy in online dating.


### Lab 3: Topic modeling <a name="three"></a>
#### Initial Setup
- This lab uses the `clean_profiles.tsv` file produced by `Lab 1`. You will need to run that code first, or get a copy of the file it creates from someone who has. 
    - If you get an error that says something like `FileNotFoundError: File b'data/clean_profiles.tsv' does not exist` at the bottom, if means that you need to run the code in Lab 1. If you already ran this code and still get this error, then check for error messages in Lab 1. 

#### Choosing a profile section
- OKC has 10 open ended text boxes in their user profiles. Students should pick one to analyze the text in. Alternatively, they may choose to analyze the combined text from all of the boxes. 
- Recommended:
    - `text`: looking at all of the profile text tends to produce interesting topics. Often, one can tell which part of the profile a topic comes from (e.g. favorite books and movies). 
    - `essay0`: the "About me" section of profiles also tends to produce interesting topics. 
    - `essay8`: the "most private thing I'm willing to admit" section of the profile often excites students, although the quality of topic models for this section is not as good. 
    
#### Helper functions
- This lab, like the others, has code labeled "helper functions." 
- This code is not explained in the notebook because it is not a central part of the lesson.
- Students should run these code cells and scroll past them without worrying about how they work. 

#### Interpreting topics
- Students will need to do some thinking to interpret the output of the topic models. 
    - The notebook contains guidance for this.
    - Ultimately, however, students should probably write out their thoughts on paper or in a separate word document. 
    - Students will need to refer to these topics throughout the rest of the lab, so having their interpretations of them handy is essential. 

#### Picking examples
- In many parts of the code, it does things like get examples of topic number 4 or look at the topic distribution for user number 3452. 
- The topics LDA produces aren't deterministic, however, and they will also vary depending on which profile text students choose to use. 
- Thus, we cannot pick good examples of topic number or profile number in advance for the notebook. 
- Students should pick topic and profile numbers that they are interested in, and substitute these into the code wherever they see specific topics or profiles listed. 

#### "Who is a topic most popular with?"
- Suggestions of traits that work out well:
    - Age_group
    - Education
    - Orientation (sexuality)
    - Sex

## Suggested Readings <a name="readings"></a>

#### Popular and short writing
- Ng, Fiona. 2016. “[Tinder Has an In-House Sociologist and Her Job Is to Figure Out What You Want](http://www.lamag.com/longform/tinder-sociologist).” *Los Angeles Magazine*, May 25. 
- Pepin, Joanna. 2015. “[Online Dating Choices, Constrained](https://contexts.org/articles/online-dating-choices-constrained).” *Contexts* 14(4):7.
- Page, Letta and Seyed Ali. 2016. “[Romancing the Data](http://journals.sagepub.com/doi/abs/10.1177/1536504216648161?journalCode=ctxa).” *Contexts* 15(2):68–69.
- Zimmer, Michael. 2016. "[OKCupid Study Reveals the Perils of Big-Data Science](https://www.wired.com/2016/05/okcupid-study-reveals-perils-big-data-science/)." *Wired* May 14.
- . 2009. "[Exactly what to say in a first message](https://theblog.okcupid.com/exactly-what-to-say-in-a-first-message-2bf680806c72)." OKCupid Data Blog, September 13. 
- . 2010. "[The REAL 'stuff white people like'](https://theblog.okcupid.com/the-real-stuff-white-people-like-66b131aa3ac8)." OKCupid Data Blog, September 7. 

#### Academic publications
- Danescu-Niculescu-Mizil, Cristian, Robert West, Dan Jurafsky, Jure Leskovec, and Christopher Potts. 2013. “[No Country for Old Members: User Lifecycle and Linguistic Change in Online Communities](https://nlp.stanford.edu/pubs/linguistic_change_lifecycle.pdf).” Pp. 307–18 in *Proceedings of the 22nd international conference on World Wide Web*. ACM.
- Sumter, Sindy R., Laura Vandenbosch, and Loes Ligtenberg. 2017. “[Love Me Tinder: Untangling Emerging Adults’ Motivations for Using the Dating Application Tinder](http://www.sciencedirect.com/science/article/pii/S0736585316301216).” *Telematics and Informatics* 34(1):67–78.
- Mason, Corinne Lysandra. 2016. “[Tinder and Humanitarian Hook-Ups: The Erotics of Social Media Racism](http://www.tandfonline.com/doi/abs/10.1080/14680777.2015.1137339?journalCode=rfms20).” *Feminist Media Studies* 16(5):822–37.
- Evans, James A. and Pedro Aceves. 2016. “[Machine Translation: Mining Text for Social Theory](http://www.annualreviews.org/doi/abs/10.1146/annurev-soc-081715-074206).” *Annual Review of Sociology* 42(May):1–30.
- Bonilla, Tabitha and Justin Grimmer. 2013. “[Elevated Threat Levels and Decreased Expectations: How Democracy Handles Terrorist Threats](https://stanford.edu/~jgrimmer/terror.pdf).” *Poetics* 41(6):650–69.


## License <a name="license"></a> 
[![Creative Commons License](https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png)](http://creativecommons.org/licenses/by-nc-nd/4.0/)  
This work is licensed under a [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License](http://creativecommons.org/licenses/by-nc-nd/4.0/).
