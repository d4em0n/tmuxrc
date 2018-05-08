#!/bin/sh
cl=${1}
if [ $cl -gt 85 ] ; then
    tmux set status-right "#[fg=colour236,bg=colour235]#[fg=colour12,bg=colour236] #(~/tmux/./cmus_status) #[fg=colour12,bg=colour236,nobold,nounderscore,noitalics]#[fg=colour235,bg=colour12] #(~/tmux/suhu)#[fg=colour236,bg=colour12] #[fg=colour12,bg=colour236] #(~/tmux/./vol) #[fg=colour12,bg=colour236,nobold,nounderscore,noitalics]#[fg=colour235,bg=colour12] #(~/tmux/./bat) #[fg=colour236,bg=colour12] #[fg=colour12,bg=colour236] %H:%M  #[fg=colour12,bg=colour236,nobold,nounderscore,noitalics]#[fg=colour235,bg=colour12] #h  "
else
    tmux set status-right ""
fi
