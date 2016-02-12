set nocompatible              " be iMproved, required

colorscheme darkblue 

set guifont=Courier\ New:h16

" history存储长度。
set history=1000       

"检测文件类型
filetype on
" 针对不同的文件类型采用不同的缩进格式  
filetype indent on               
"允许插件  
filetype plugin on
"启动自动补全
filetype plugin indent on

" 非兼容vi模式。去掉讨厌的有关vi一致性模式，避免以前版本的一些bug和局限
set nocompatible      
set autoread          	" 文件修改之后自动载入。
set shortmess=atI       " 启动的时候不显示那个援助索马里儿童的提示

" 取消备份。
" Turn backup off, since most stuff is in SVN, git et.c anyway...
set nobackup
set nowb
set noswapfile

" No annoying sound on errors
" 去掉输入错误的提示声音
set noerrorbells
set novisualbell
set t_vb=
set tm=500

"显示行号：
set number
set nowrap                    " 取消换行。

"括号配对情况
set showmatch
" How many tenths of a second to blink when matching brackets
set mat=2

"设置文内智能搜索提示
" 高亮search命中的文本。
set hlsearch          
" 搜索时忽略大小写
set ignorecase
" 随着键入即时搜索
set incsearch
" 有一个或以上大写字母时仍大小写敏感
set smartcase

" 代码折叠
set foldenable
" 折叠方法
" manual    手工折叠
" indent    使用缩进表示折叠
" expr      使用表达式定义折叠
" syntax    使用语法定义折叠
" diff      对没有更改的文本进行折叠
" marker    使用标记进行折叠, 默认标记是 {{{ 和 }}}
set foldmethod=syntax
" 在左侧显示折叠的层次
"set foldcolumn=4

set tabstop=4                " 设置Tab键的宽度        [等同的空格个数]
set shiftwidth=4
set expandtab                " 将Tab自动转化成空格    [需要输入真正的Tab键时，使用 Ctrl+V + Tab]
" 按退格键时可以一次删掉 4 个空格
set softtabstop=4

set ai "Auto indent
set si "Smart indent


"==========================================
" status
"==========================================
"显示当前的行号列号：
set ruler
""在状态栏显示正在输入的命令
set showcmd


" Set 7 lines to the cursor - when moving vertically using j/k 上下滚动,始终在中间
set so=7


"==========================================
"colors and fonts
"==========================================
"开启语法高亮
syntax enable
syntax on

"==========================================
" file encode
"==========================================
" 设置新文件的编码为 UTF-8
set fileencoding=utf8
"set enc=2byte-gb18030
" 自动判断编码时，依次尝试以下编码：
set fileencodings=ucs-bom,utf-8,gb18030,default
" gb18030 最好在 UTF-8 前面，否则其它编码的文件极可能被误识为 UTF-8

" Use Unix as the standard file type
set ffs=unix,dos,mac

" 如遇Unicode值大于255的文本，不必等到空格再折行。
set formatoptions+=m
" 合并两行中文时，不在中间加空格：
set formatoptions+=B

filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')

" let Vundle manage Vundle, required
Plugin 'VundleVim/Vundle.vim'

" The following are examples of different formats supported.
" Keep Plugin commands between vundle#begin/end.
" plugin on GitHub repo
Plugin 'tpope/vim-fugitive'
" plugin from http://vim-scripts.org/vim/scripts.html
Plugin 'L9'
" Git plugin not hosted on GitHub
Plugin 'git://git.wincent.com/command-t.git'
" git repos on your local machine (i.e. when working on your own plugin)
Plugin 'file:///home/gmarik/path/to/plugin'
" The sparkup vim script is in a subdirectory of this repo called vim.
" Pass the path to set the runtimepath properly.
Plugin 'rstacruz/sparkup', {'rtp': 'vim/'}
" Avoid a name conflict with L9
Plugin 'user/L9', {'name': 'newL9'}

" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required