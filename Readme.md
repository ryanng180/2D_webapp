# Pandemic Food security predictor

<!-- markdown-toc start -->

**Table of Contents**

- [Pandemic Food security predictor](#Pandemic Food security predictor)
  - [Setup](#setup)
    - [Install Git](#install-git)
    - [Downloading Repository](#downloading-repository)
    - [Create Virtual Environment](#create-virtual-environment)
    - [Using Transcrypt](#using-transcrypt)
    - [Run Flask](#run-flask)
      - [Vocareum](#vocareum)
      - [Local Computer](#local-computer)
  - [Instructions for webapp](#instructions-for-webapp)
    - [Expected Input](#expected-input)
    - [Expected Output](#expected-output)
    - [Another prediction](#another-prediction)

<!-- markdown-toc end -->

## Setup

### Install Git

You need to have Git to do the project. Download and install the software according to your OS:

- Windows: [Git for Windows](https://git-scm.com/download/win)
- Mac OS: [Git for MacOS](https://git-scm.com/download/mac)

### Downloading Repository

Clone the mini project repository from Github. On your terminal or Git Bash, type the following:

```shell
cd Downloads
git clone https://github.com/Data-Driven-World/d2w_mini_projects
```

### Create Virtual Environment

**You should open Anaconda Prompt to do the following steps.**

In the following steps, whenever there is a different between the OS commands, the **Windows** prompt will be represented by:

```shell
>
```

while the MacOS/Linux prompt will be represented by:

```shell
$
```

Go to the root folder `2D_webapp`.

Windows:

```dos
> cd %USERPROFILE%\Downloads\2D_webapp
```

Unix/MacOS:

```shell
$ cd ~/Downloads/2D_webapp
```

First make sure that you have installed `pipenv` package.

```shell
python -m pip install --user pipenv
```

**If you are running the above commands in Vocareum, you may encounter the following message at the end of the installation.**

```shell
WARNING: The script virtualenv is installed in '/voc/work/.local/bin' which is not on PATH.
Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
WARNING: The scripts pipenv and pipenv-resolver are installed in '/voc/work/.local/bin' which is not on PATH.
Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
```

It is basically saying that you need to add the newly installed `pipenv` program into the `PATH` so that you can use it from anywhere in the terminal. To do that, run the following command in the terminal.

```shell
export PATH='/voc/work/.local/bin':$PATH
```

Note: the above command works when you are running in Vocareum under Linux shell.

We will call `mp_sort` folder as the **root** folder of our application.

From the root folder, install the packages specified in the `Pipfile`.

```shell
python -m pipenv install
```

The above steps will install Flask and Transcrypt Python libraries and some other necessary packages.

To activate the virtualenv, run

```shell
python -m pipenv shell
```

Alternatively, you can choose everytime you run a command to prepend that command with the following:

```shell
python -m pipenv run
```

Ok, so let's enter into the shell by typing:

```shell
python -m pipenv shell
```

You should see the word `(2D_webapp)` in your prompt something like:

Windows:

```dos
(2D_webapp) folder >
```

Unix/MacOS:

```shell
(2D_webapp) user $
```

_To exit the virtual environment at the end of this mini project, simply type:_

```shell
exit
```

All the steps assumes you are in the virtualenv shell.

### Using Transcrypt

Javascript is the commonly used language for front-end web development. However, since this course only covers Python. We will use `Transcrypt` library which can compile and translate Python script into a Javascript file. To compile `library.py`, first we need to go into the `static` folder.

Windows:

```dos
> cd %USERPROFILE\Downloads\2D_webapp\app\static
> dir
```

Unix/MacOS:

```shell
$ cd ~/Downloads/2D_webapp/app/static
$ ls
```

The last command will list the file in that folder, and you should see:

```shell
library.py
```

Run Transcrypt on `library.py`:

```shell
python -m transcrypt -b -n library
```

The option `-b` means to build the javascript library. You can use `--help` for more options. Once it is done, you should be able to see a folder called `__target__` containing several files. To see the content of that folder:

Windows:

```dos
> dir
> dir __target__
```

Unix/MacOS:

```shell
$ ls
$ ls __target__
```

The output should be something like the following:

```shell
__target__/
  library.js
  library.project
  math.js
  org.transcrypt.__runtime__.js
  random.js
```

You should see `library.js` created inside this folder.

### Run Flask

Now you are ready to run your web app in your local computer. To do so, you need to go back to the root directory. This can be done with the following:

Windows:

```dos
> cd ..\..
```

Unix/MacOS:

```shell
$ cd ../..
```

which means go up the folder two times. Or, simply

Windows:

```dos
> cd %USERPROFILE\Downloads\2D_webapp
```

Unix/MacOS:

```shell
$ cd ~/Downloads/2D_webapp/
```

You should see `application.py` in this root folder.

Now, you can run Flask by typing:

```shell
flask run
```

You should see that some output will be thrown out, which one of them would be:

```shell
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Now you can open your browser at `http://127.0.0.1:5000/` to see the web app. You should see something like the following:

![](https://www.dropbox.com/s/a2fqx5svvyqtqf9/mp1_home.png?raw=1)

To stop the web app, type `CTRL+C`.

## Instructions for webapp

select your input Context and Predictor Variables

## Expected Input

1. Select Context: Pick a pandemic and country
2. Select Predictor Variables: Select as many Predictor Variables as you like
3. Click Calculate

## Expected Output

A Result produced.

- Moderate: Our model predicts that food security in your selected {country}, given your selected {predictor variables} is highly likely to be moderately affected in selected {pandemic}.
- Severe: Our model predicts that food security in your selected {country}, given your selected {predictor variables} is highly likely to be severly affected in selected {pandemic}.

## Another prediction

please use the Clear button then repeat steps for Expected Input. Or you can manually reconfigure the Expected Inputs directly.
