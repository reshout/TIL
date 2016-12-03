# Markdown support for Vim Editor

## vim-markdown

https://github.com/plasticboy/vim-markdown

### Install Vundle

https://github.com/VundleVim/Vundle.vim

```bash
$ git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
```

`~/.vimrc` 파일의 가장 위에 아래 내용을 추가

```
set nocompatible
filetype off

set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
Plugin 'VundleVim/Vundle.vim'
call vundle#end()
filetype plugin indent on
```

### Install vim-markdown

`~/.vimrc` 파일에 아래 내용을 추가

```
Plugin 'godlygeek/tabular'
Plugin 'plasticboy/vim-markdown'
```

Vim에서 아래 커맨드 실행

```
:so ~/.vimrc
:PluginInstall
```

`~/.vimrc`에 추가 설정

```
let g:vim_markdown_folding_disabled = 1
let g:vim_markdown_fenced_languages = ['python', 'java', 'bash=sh']
let g:vim_markdown_new_list_item_indent = 2
```
