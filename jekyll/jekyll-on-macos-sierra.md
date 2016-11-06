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
gem update
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

Wordpress에서 import 하려면 sequel, mysql2, unidecode가 필요하다.

```bash
gem install sequel
gem install mysql2
gem install unidecode
```

아래와 같이 import에는 성공했지만,

```bash
ruby -rubygems -e 'require "jekyll-import";
JekyllImport::Importers::WordPress.run({
"dbname"   => "wordpress",
"user" => "root",
"password" => "xxxxxxxx",
"host" => "reshout.com",
"socket" => "",
"table_prefix" => "wp_",
"site_prefix" => "",
"clean_entities" => false,
"comments" => false,
"categories" => true,
"tags" => true,
"more_excerpt" => true,
"more_anchor" => true,
"extensions" => "html",
"status" => ["publish"]
})'
```

다음과 같은 파일 이름 때문에 관리가 어려워 보인다.

```
2014-02-05-mac-os-x-%ed%84%b0%eb%af%b8%eb%84%90%ec%97%90%ec%84%9c-git-%eb%b8%8c%eb%9e%9c%ec%b9%98%ea%b0%80-%eb%b3%b4%ec%9d%b4%eb%8a%94-%ed%94%84%eb%a1%ac%ed%94%84%ed%8a%b8-%ec%84%a4%ec%a0%95.html
```
