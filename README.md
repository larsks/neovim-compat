I'm using [Neovim][], but I like to type `vim`. I could create an alias, but that only works in the shell. I could just drop a shell script into `~/bin/vim`, but that will cause problems if I were to replace Neovim with regular Vim.

This package, which conflicts with regular Vim, provides the best solution: install it along with Neovim and you get `vim`. If at some point you try to install regular Vim, this package will get removed.

[neovim]: https://neovim.io/
