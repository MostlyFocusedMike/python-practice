# Python notes

pyenv is how we manage our system python versions, and to make sure it works you
need to add the following to your .zshrc

export PATH=/opt/homebrew/bin:$PATH
export PATH=/opt/homebrew/sbin:$PATH

export PATH=$(pyenv root)/shims:$PATH

Here's the stuff you need to run it

pyenv versions

pyenv install 3.5.9

pyenv global 3.8.0

pyenv local 3.5.9
// this sets it locally

https://opensource.com/article/20/4/pyenv


Virtual environments allow us to install specific versions in certain directories

cd numpy-practice
source ./venv/bin/activate

is how you get the one you wrote started in numpy. You just need to get to the venv/bin/activate executable

To exit, simply enter `deactivate` while in the virtual environment

## Running the file
just use nodemon

```bash
nodemon my-file.py
```
