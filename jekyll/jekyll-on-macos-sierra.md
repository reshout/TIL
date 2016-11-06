# Jekyll on macOS Sierra

https://jekyllrb-ko.github.io

## Install Ruby

https://gorails.com/setup/osx/10.12-sierra

```bash
brew install rbenv ruby-build

# Add rbenv to bash so that it loads every time you open a terminal
echo 'if which rbenv > /dev/null; then eval "$(rbenv init -)"; fi' >> ~/.bash_profile
source ~/.bash_profile

# Install Ruby
rbenv install 2.3.1
rbenv global 2.3.1
ruby -v
```

## Install Jekyll and Bundle

```bash
gem install jekyll
gem install bundle
bundle install
```
## Create and Serve Site

```bash
jekyll new my-awesome-site
cd my-awesome-site
jekyll serve
```
