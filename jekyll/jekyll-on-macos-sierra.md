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
## Create and serve site

```bash
jekyll new my-awesome-site
cd my-awesome-site
jekyll serve
```

## Import posts from Wordpress

http://import.jekyllrb.com/docs/wordpress/

jekyll-import를 설치하는 과정에서 nokogiri 설치 실패했다. [Stack Overflow](http://stackoverflow.com/questions/40038953/installing-nokogiri-on-mac-os-sierra-10-12)를 참조하여, 아래와 같이 nokogiri 및 jekyll-import 설치에 성공했다.

```bash
xcode-select --install
gem install nokogiri
gem install jekyll-import
```
