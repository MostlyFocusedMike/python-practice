```text
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

# Managing environments
https://towardsdatascience.com/python-environment-101-1d68bda3094d
- `brew install pyenv` is the NVM of python
- Then run `pyenv init` which prints the following to the screen:

    ```bash
    # Load pyenv automatically by appending
    # the following to ~/.zshrc:

    eval "$(pyenv init -)"
    ```

  Which you then copy into .bash_profile (this is copied into your .zshrc already)

- `pyenv install -l` list out all versions
- `pyenv version` shows the current version in use
- `pyenv versions` shows what you have on your system (it will probably just be the system version)
- `pyenv install 3.7.7` installs a version
- `pyenv global 3.7.7` sets the global version
- `pyenv local 3.7.7` sets the local dir version with a `.python-version` which just lists the version
- There are pyenv virtual env, but honestly for now the standard way seems fine. Just switch to the version and make the venv

# Creating virtual environments
https://docs.python.org/3/tutorial/venv.html
- The main book uses anaconda, but I don't care to look that up just yet

## using builtin venv (this must use the version of python it was spawned from)
- use built in `python3 -m venv tutorial-env` (swap out tutorial-env with your own name)
- and then to activiate: `source tutorial-env/bin/activate`
- and to leave, close the shell or enter `deactivate` from the shell
- to delete, remove the `tutorial-env` file

`source dsfs/bin/activate` is the one for the book

The main environemnt is "main-python-env" so to start its: `source main-python-env/bin/activate` in the root of the project.


## Installing packages
- Package manager install with pip like: `python -m pip install novas` inside the virtual env
-` pip show` will display information about a particular package:
- `pip list` will display all of the packages installed in the virtual environment

## Package control
- `pip freeze` will produce a similar list of the installed packages, but the output uses the format that pip install expects. A common convention is to put this list in a `requirements.txt` file:

```bash
(tutorial-env) $ pip freeze > requirements.txt
(tutorial-env) $ cat requirements.txt
novas==3.1.1.3
numpy==1.9.2
requests==2.7.0
```
- The `requirements.txt` can then be committed to version control and shipped as part of an application. Users can then install all the necessary packages with `install -r`:

```bash
(tutorial-env) $ python -m pip install -r requirements.txt
Collecting novas==3.1.1.3 (from -r requirements.txt (line 1))
  ...
Collecting numpy==1.9.2 (from -r requirements.txt (line 2))
  ...
Collecting requests==2.7.0 (from -r requirements.txt (line 3))
  ...
Installing collected packages: novas, numpy, requests
  Running setup.py install for novas
Successfully installed novas-3.1.1.3 numpy-1.9.2 requests-2.7.0
```