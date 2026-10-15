#!/usr/bin/env zsh

# MIT License
#
# Copyright (c) 2017 Sergei Kolesnikov
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

#======================================================================#
#    _        _                _ _ _         _____ _                   #
#   /_\  _ __| |_  _ _ ___  __| (_) |_ ___  |_   _| |_  ___ _ __  ___  #
#  / _ \| '_ \ ' \| '_/ _ \/ _` | |  _/ -_)   | | | ' \/ -_) '  \/ -_) #
# /_/ \_\ .__/_||_|_| \___/\__,_|_|\__\___|   |_| |_||_\___|_|_|_\___| #
#       |_|                                                            #
#                                                                      #
#                       Aphrodite Terminal Theme                       #
#                 by Sergei Kolesnikov a.k.a. win0err                  #
#                                                                      #
#                        https://kolesnikov.se                         #
#                                                                      #
#======================================================================#


export VIRTUAL_ENV_DISABLE_PROMPT=true
setopt PROMPT_SUBST

precmd() {
	if [[ -z "$FIRST_PROMPT_DRAWN" ]]; then
		FIRST_PROMPT_DRAWN=1
	else
		print ""
	fi
}

aphrodite_get_prompt() {
	if (( ${+VIRTUAL_ENV} )); then
		echo -n "%F{7}["$(basename "$VIRTUAL_ENV")"]%f "
	fi

	echo -n "%F{15}%n"
	echo -n "%F{15}@"
	echo -n "%F{11}%m"
	echo -n "%F{15}:"
	echo -n "%f%~"
	echo -n " "

	local git_branch
	git_branch=$(git --no-optional-locks rev-parse --abbrev-ref HEAD 2> /dev/null)
	if [[ -n "$git_branch" ]]; then
		local git_status
		git_status=$(git --no-optional-locks status --porcelain 2> /dev/null | tail -n 1)
		[[ -n "$git_status" ]] && echo -n "%F{11}" || echo -n "%F{10}"
		echo -n "‹${git_branch}›%f"
	fi

	if (( ${+APHRODITE_THEME_SHOW_TIME} )); then
		echo -n "%F{8} [%D{%H:%M:%S}]%f"
	fi

	echo  # new line

	echo -n "%(?.%f.%F{1})"  # if retcode == 0 ? reset : red
	echo -n "%(!.#.$)%f "  # if is_root_user ? # : $
}

export PROMPT='$(aphrodite_get_prompt)'
