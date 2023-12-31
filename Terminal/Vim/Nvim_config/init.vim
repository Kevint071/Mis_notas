":::instalacion de plugins:::
"::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
let g:python3_host_prog = "C:\\Users\\andre\\AppData\\Local\\Programs\\Python\\Python311\\python.exe" 

let g:loaded_python_provider = 0
"CONFIGURACIONES BASICAS 
set number 				"muestra los numeros de cada linea en la parte izquierda 
set relativenumber 			"la distribucion de los numeros en lineas de manera relativa
set mouse=a 				"permite la interaccion con el mouse
set noshowmode				"me deja de mostrar el modo en el que estamos 'normal, insert, visual, etc'
syntax enable 				"activa el coloreado de sintaxis en algunos tipos de archivos como html, c, c++
set encoding=utf-8 			"permite setear la codificación de archivos para aceptar caracteres especiales
set sw=4 				"la indentación genera 4 espacios
set nowrap				"el texto en una linea no baja a la siguiente, solo continua en la misma hasta el infinito.
"set noswapfile				"para evitar el mensaje que sale al abrir algunos archivos sobre swap.
set clipboard=unnamed			"para poder utilizar el portapapeles del sistema operativo 'esto permite poder copiar y pegar desde cualquier parte a nvim y viceversa.	
set noswapfile
syntax on
set mouse=a
set noerrorbells
set sw=2 sts=2
set number
set smartindent
set rnu
set numberwidth=1
set nowrap
set nobackup
set showmatch
set incsearch
set ignorecase
set clipboard=unnamedplus
set encoding=UTF-8
set cursorline
set relativenumber
set showcmd
set ruler
set laststatus=2
set noshowmode
set smartcase
set hlsearch
set tabstop=2
set shiftwidth=2
set expandtab
set softtabstop=2
filetype plugin indent on
set colorcolumn=80
"cuando hagamos split se acomode abajo o arriba
set splitbelow
set splitright
"Para pelgar codigo de lenguaje de programacion
set foldmethod=syntax
"set foldmethod=indent
set nofoldenable        "dont fold by default
"configuracion del tema
set termguicolors 			"activa el true color en la terminal

"----------------
" INSTALACIÓN DE PLUGINS
"----------------

call plug#begin('~/AppData/Local/nvim/plugged')

"----------------
" TEMAS  
"----------------

Plug 'joshdick/onedark.vim' "Tema oscuro
Plug 'tomasr/molokai' "Tema molokai

"----------------
" NAVEGACIÓN
"----------------

Plug 'yazgoo/vmux'
Plug 'preservim/nerdtree' "Explorador archivos
Plug 'christoomey/vim-tmux-navigator' "Navegar splits

"----------------   
" PRODUCTIVIDAD
"----------------

Plug 'mattn/emmet-vim' "Abreviaciones HTML
Plug 'jiangmiao/auto-pairs' "Autocompletar caracteres 
Plug 'terryma/vim-multiple-cursors' "Múltiples cursores
Plug 'easymotion/vim-easymotion' "Navegación rápida  
Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'osyo-manga/vim-over'
Plug 'ctrlpvim/ctrlp.vim'

"----------------
" TERMINAL
"----------------

Plug 'voldikss/vim-floaterm' "Terminal flotante
Plug 'erietz/vim-terminator' "Ejecutar código

"----------------
" BÚSQUEDA 
"----------------

Plug 'junegunn/fzf' "Búsqueda difusa 
Plug 'junegunn/fzf.vim' "Búsqueda archivos

"----------------
" FORMATO Y SINTAXIS
"----------------
 
Plug 'sbdchd/neoformat' "Formateo automático
Plug 'sheerun/vim-polyglot' "Resaltado sintaxis
Plug 'lilydjwg/colorizer' "Colores hexadecimales
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
"----------------
" OTROS
"----------------

Plug 'Yggdroot/indentLine' "Líneas indentación 
Plug 'scrooloose/nerdcommenter' "Comentar código
Plug 'ryanoasis/vim-devicons' "Iconos archivos
Plug 'valloric/matchtagalways' "Resaltado etiquetas
Plug 'tpope/vim-surround' "Delimitadores texto
Plug 'tmhedberg/simpylfold' "Plegado código
Plug 'vim-scripts/TaskList.vim' "Lista tareas
Plug 'vim-python/python-syntax' "Sintaxis Python
Plug 'KabbAmine/vCoolor.vim'
Plug 'raimon49/requirements.txt.vim'

call plug#end()

syntax on
colorscheme molokai	"activar el tema onedark

"Confioguraciones Extras
"colorscheme onedark


"MOLOKAI THEME
"let g:molokai_original = 0
"let g:rehash256 = 0 

let mapleader=","

"Colocar ; al final
"Se ejecuta con Leader ;
nnoremap <Leader>; $a;<Esc>

nnoremap <Leader>w :w<CR>
nnoremap <Leader>q :q<CR>

"Ir al siguiente buffer
"Se ejecuta con Leader k
noremap <Leader>k :bnext<CR>

"Eliminar texto seleccionado
"Se ejecuta con Leader delete
vnoremap <Leader>d "_d<CR>

noremap ñ<BS> "_ddk$
noremap ñ<Del> "_dd_
noremap <M-Down> :m+<CR>
nnoremap <BS> hxh 
" Mover línea arriba
" con alt + flecha arriba
noremap <M-Up> :m-2<CR>

" Abrir explorador de archivos
" con espacio + e
nmap <space>e <Cmd>CocCommand explorer<CR>

" Buscar archivos con FZF
" con leader + p
map <Leader>p :Files<CR>

" Abrir terminal split
" con control + t
vnoremap <c-t> :split<CR>:ter<CR>:resize 10<CR>
nnoremap <c-t> :split<CR>:ter<CR>:resize 10<CR>

nnoremap <leader><CR> o<Esc>

"siguiente buffers y anterior buffer
nnoremap <Leader>k :bnext<CR>
nnoremap <Leader>j :bprevious<CR>
nnoremap <Leader>x :bdelete<CR>

"#solo instalar el primero copiar '+y   pegar  "+p
"sudo apt install xclip
nnoremap <Leader>y "+y<CR>

"Split
nnoremap <Leader>vs :vsp<CR>
nnoremap <Leader>sp :sp<CR>


"Para q las feclas no funcionen
noremap <up> <nop>
noremap <down> <nop>
noremap <left> <nop>
noremap <right> <nop>


"split resize
nnoremap <Leader>> 10<C-w>>
nnoremap <Leader>< 10<C-w><

"Ajustar el tamano de las ventanas
nnoremap <silent> <right> :vertical resize +5<CR>
nnoremap <silent> <left> :vertical resize -5<CR>
nnoremap <silent> <up> :resize +5<CR>
nnoremap <silent> <down> :resize -5<CR>
nnoremap <Leader>e :e ~/.config/nvim/init.vim<CR>
nmap <F5> :source ~/AppData/Local/nvim/init.vim<CR>
vmap <F5> :source ~/AppData/Local/nvim/init.vim<CR>


"Buscamos con 2 letras un palabra en nuestro archivo
nmap <Leader>s <Plug>(easymotion-s2)



"##################################################################
"CONFIGURACION VIM AIRLINE
"##################################################################
let g:airline#extensions#tabline#left_sep = ' '
let g:airline#extensions#tabline#left_alt_sep = '|'
let g:airline_theme='google_dark'

"let g:airline_statusline_ontop=0

let g:airline#extensions#default#section_truncate_width = {
    \ 'b': 79,
    \ 'x': 60,
    \ 'y': 88,
    \ 'z': 45,
    \ 'warning': 80,
    \ 'error': 80,
    \ }

let g:airline#extensions#default#layout = [
    \ [ 'a', 'b' , 'c', 'x' ],
    \ [ 'z', 'error' ]
    \ ]


"#######################################
"CONFIGURACION FLOATERM TERMINAL
"#######################################
let g:floaterm_autoinsert=1
let g:floaterm_width=0.8
let g:floaterm_height=0.8
let g:floaterm_wintitle=0
let g:floaterm_autoclose=1
let g:floaterm_keymap_toggle = '<F1>'


"##################################################################
"CONFIGURACION VIM AIRLINE
"##################################################################
let g:airline#extensions#tabline#left_sep = ' '
let g:airline#extensions#tabline#left_alt_sep = '|'
let g:airline_theme='google_dark'

"#######################################
"JS FORMAT NEOFORMAT, formateador de js, ts, react
"#######################################
"link: https://hashrocket.com/blog/posts/writing-prettier-javascript-in-vim
let g:neoformat_try_formatprg = 1
augroup NeoformatAutoFormat
    autocmd!
    autocmd FileType javascript,typescript,javascript.jsx setlocal formatprg=prettier\
                                                            \--stdin\
                                                            \--print-width\ 80\
                                                            \--single-quote\
                                                            \--trailing-comma\ es5
    autocmd BufWritePre *.ts,*.js,*.jsx Neoformat
augroup END

nnoremap <silent> <F2> :CocCommand explorer<CR>

"###################################
"CONFIGURACIÓN DE EL PLUGIN CocList
"###################################
"May need for Vim (not Neovim) since coc.nvim calculates byte offset by count
" utf-8 byte sequence
set encoding=utf-8
" Some servers have issues with backup files, see #649
set nobackup
set nowritebackup

" Having longer updatetime (default is 4000 ms = 4s) leads to noticeable
" delays and poor user experience
set updatetime=300

" Always show the signcolumn, otherwise it would shift the text each time
" diagnostics appear/become resolved
set signcolumn=yes

" Use tab for trigger completion with characters ahead and navigate
" NOTE: There's always complete item selected by default, you may want to enable
" no select by `"suggest.noselect": true` in your configuration file
" NOTE: Use command ':verbose imap <tab>' to make sure tab is not mapped by
" other plugin before putting this into your config
inoremap <silent><expr> <TAB>
      \ coc#pum#visible() ? coc#pum#next(1) :
      \ CheckBackspace() ? "\<Tab>" :
      \ coc#refresh()
inoremap <expr><S-TAB> coc#pum#visible() ? coc#pum#prev(1) : "\<C-h>"

" Make <CR> to accept selected completion item or notify coc.nvim to format
" <C-g>u breaks current undo, please make your own choice
inoremap <silent><expr> <CR> coc#pum#visible() ? coc#pum#confirm()
                              \: "\<C-g>u\<CR>\<c-r>=coc#on_enter()\<CR>"

function! CheckBackspace() abort
  let col = col('.') - 1
  return !col || getline('.')[col - 1]  =~# '\s'
endfunction

" Use <c-space> to trigger completion
if has('nvim')
  inoremap <silent><expr> <c-space> coc#refresh()
else
  inoremap <silent><expr> <c-@> coc#refresh()
endif

" Use `[g` and `]g` to navigate diagnostics
" Use `:CocDiagnostics` to get all diagnostics of current buffer in location list
nmap <silent> [g <Plug>(coc-diagnostic-prev)
nmap <silent> ]g <Plug>(coc-diagnostic-next)

" GoTo code navigation
nmap <silent> gd <Plug>(coc-definition)
nmap <silent> gy <Plug>(coc-type-definition)
nmap <silent> gi <Plug>(coc-implementation)
nmap <silent> gr <Plug>(coc-references)

" Use K to show documentation in preview window
nnoremap <silent> K :call ShowDocumentation()<CR>

function! ShowDocumentation()
  if CocAction('hasProvider', 'hover')
    call CocActionAsync('doHover')
  else
    call feedkeys('K', 'in')
  endif
endfunction

" Highlight the symbol and its references when holding the cursor
autocmd CursorHold * silent call CocActionAsync('highlight')

" Symbol renaming
nmap <leader>rn <Plug>(coc-rename)

" Formatting selected code
xmap <leader>f  <Plug>(coc-format-selected)
nmap <leader>f  <Plug>(coc-format-selected)

augroup mygroup
  autocmd!
  " Setup formatexpr specified filetype(s)
  autocmd FileType typescript,json setl formatexpr=CocAction('formatSelected')
  " Update signature help on jump placeholder
  autocmd User CocJumpPlaceholder call CocActionAsync('showSignatureHelp')
augroup end

" Applying code actions to the selected code block
" Example: `<leader>aap` for current paragraph
xmap <leader>a  <Plug>(coc-codeaction-selected)
nmap <leader>a  <Plug>(coc-codeaction-selected)

" Remap keys for applying code actions at the cursor position
nmap <leader>ac  <Plug>(coc-codeaction-cursor)
" Remap keys for apply code actions affect whole buffer
nmap <leader>as  <Plug>(coc-codeaction-source)
" Apply the most preferred quickfix action to fix diagnostic on the current line
nmap <leader>qf  <Plug>(coc-fix-current)

" Remap keys for applying refactor code actions
nmap <silent> <leader>re <Plug>(coc-codeaction-refactor)
xmap <silent> <leader>r  <Plug>(coc-codeaction-refactor-selected)
nmap <silent> <leader>r  <Plug>(coc-codeaction-refactor-selected)

" Run the Code Lens action on the current line
nmap <leader>cl  <Plug>(coc-codelens-action)

" Map function and class text objects
" NOTE: Requires 'textDocument.documentSymbol' support from the language server
xmap if <Plug>(coc-funcobj-i)
omap if <Plug>(coc-funcobj-i)
xmap af <Plug>(coc-funcobj-a)
omap af <Plug>(coc-funcobj-a)
xmap ic <Plug>(coc-classobj-i)
omap ic <Plug>(coc-classobj-i)
xmap ac <Plug>(coc-classobj-a)
omap ac <Plug>(coc-classobj-a)

" Remap <C-f> and <C-b> to scroll float windows/popups
if has('nvim-0.4.0') || has('patch-8.2.0750')
  nnoremap <silent><nowait><expr> <C-f> coc#float#has_scroll() ? coc#float#scroll(1) : "\<C-f>"
  nnoremap <silent><nowait><expr> <C-b> coc#float#has_scroll() ? coc#float#scroll(0) : "\<C-b>"
  inoremap <silent><nowait><expr> <C-f> coc#float#has_scroll() ? "\<c-r>=coc#float#scroll(1)\<cr>" : "\<Right>"
  inoremap <silent><nowait><expr> <C-b> coc#float#has_scroll() ? "\<c-r>=coc#float#scroll(0)\<cr>" : "\<Left>"
  vnoremap <silent><nowait><expr> <C-f> coc#float#has_scroll() ? coc#float#scroll(1) : "\<C-f>"
  vnoremap <silent><nowait><expr> <C-b> coc#float#has_scroll() ? coc#float#scroll(0) : "\<C-b>"
endif

" Use CTRL-S for selections ranges
" Requires 'textDocument/selectionRange' support of language server
nmap <silent> <C-s> <Plug>(coc-range-select)
xmap <silent> <C-s> <Plug>(coc-range-select)

" Add `:Format` command to format current buffer
command! -nargs=0 Format :call CocActionAsync('format')

" Add `:Fold` command to fold current buffer
command! -nargs=? Fold :call     CocAction('fold', <f-args>)

" Add `:OR` command for organize imports of the current buffer
command! -nargs=0 OR   :call     CocActionAsync('runCommand', 'editor.action.organizeImport')

" Add (Neo)Vim's native statusline support
" NOTE: Please see `:h coc-status` for integrations with external plugins that
" provide custom statusline: lightline.vim, vim-airline
set statusline^=%{coc#status()}%{get(b:,'coc_current_function','')}

" Mappings for CoCList
" Show all diagnostics
nnoremap <silent><nowait> <space>a  :<C-u>CocList diagnostics<cr>
" Manage extensions
nnoremap <silent><nowait> <space>e  :<C-u>CocList extensions<cr>
" Show commands
nnoremap <silent><nowait> <space>c  :<C-u>CocList commands<cr>
" Find symbol of current document
nnoremap <silent><nowait> <space>o  :<C-u>CocList outline<cr>
" Search workspace symbols
nnoremap <silent><nowait> <space>s  :<C-u>CocList -I symbols<cr>
" Do default action for next item
nnoremap <silent><nowait> <space>j  :<C-u>CocNext<CR>
" Do default action for previous item
nnoremap <silent><nowait> <space>k  :<C-u>CocPrev<CR>
" Resume latest coc list
nnoremap <silent><nowait> <space>p  :<C-u>CocListResume<CR>
nnoremap <silent> <f2> :CocCommand explorer<CR>
