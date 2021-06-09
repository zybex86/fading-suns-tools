COLOR_LIST='black red green yellow blue magenta cyan white'

COLOR_BLACK=0
COLOR_RED=1
COLOR_GREEN=2
COLOR_YELLOW=3
COLOR_BLUE=4
COLOR_MAGENTA=5
COLOR_CYAN=6
COLOR_WHITE=7

FG_BLACK="\033[30m"
FG_RED="\033[31m"
FG_GREEN="\033[32m"
FG_YELLOW="\033[33m"
FG_BLUE="\033[34m"
FG_MAGENTA="\033[35m"
FG_CYAN="\033[36m"
FG_WHITE="\033[37m"

FG_LTBLACK="\033[30;1m"
FG_LTRED="\033[31;1m"
FG_LTGREEN="\033[32;1m"
FG_LTYELLOW="\033[33;1m"
FG_LTBLUE="\033[34;1m"
FG_LTMAGENTA="\033[35;1m"
FG_LTCYAN="\033[36;1m"
FG_LTWHITE="\033[37;1m"

FG_DEFAULT="\033[39m"
FG_256_="\033[38;5;"
FG_TRUE_="\033[38;2;"

BG_BLACK="\033[40m"
BG_RED="\033[41m"
BG_GREEN="\033[42m"
BG_YELLOW="\033[43m"
BG_BLUE="\033[44m"
BG_MAGENTA="\033[45m"
BG_CYAN="\033[46m"
BG_WHITE="\033[47m"

BG_DEFAULT="\033[49m"
BG_256_="\033[48;5;"
BG_TRUE_="\033[48;2;"

ST_BOLD="\033[1m"
ST_UNDERLINE="\033[4m"
ST_REVERSE="\033[7m"

ST_RST="\033[0m"

set_style() {
    code="\033[$((30+$1+$3*60));$((40+$2+$4*60))"
    [ $5 -eq 1 ] && code=$code";1"
    [ $6 -eq 1 ] && code=$code";4"
    printf $code"m"
}

reset_style() {
    printf "$ST_RST"
}

_hex2rgb() {
    r="0x$(echo $1 | cut -c 1-2)"
    g="0x$(echo $1 | cut -c 3-4)"
    b="0x$(echo $1 | cut -c 5-6)"
    printf "%d;%d;%d" $f $g $b
}

fg_256() {
    printf "$FG_256_$1m"
}

bg_256() {
    printf "$BG_256_$1m"
}

fg_hex() {
    printf "$FG_TRUE_$(_hex2rgb $1)m"
}

bg_256() {
    printf "$BG_TRUE_$(_hex2rgb $1)m"
}

[ $(echo -e) ] && ECHO_NO_E=true
echo_e() {
    [ $ECHO_NO_E ] && echo "$@" || echo -e "$@"
}

echo_black() {
    echo_e "$FG_BLACK""$@""$ST_RST"
}
echo_red() {
    echo_e "$FG_RED""$@""$ST_RST"
}
echo_green() {
    echo_e "$FG_GREEN""$@""$ST_RST"
}
echo_yellow() {
    echo_e "$FG_YELLOW""$@""$ST_RST"
}
echo_blue() {
    echo_e "$FG_BLUE""$@""$ST_RST"
}
echo_magenta() {
    echo_e "$FG_MAGENTA""$@""$ST_RST"
}
echo_cyan() {
    echo_e "$FG_CYAN""$@""$ST_RST"
}
echo_white() {
    echo_e "$FG_WHITE""$@""$ST_RST"
}

echo_ltblack() {
    echo_e "$FG_LTBLACK""$@""$ST_RST"
}
echo_ltred() {
    echo_e "$FG_LTRED""$@""$ST_RST"
}
echo_ltgreen() {
    echo_e "$FG_LTGREEN""$@""$ST_RST"
}
echo_ltyellow() {
    echo_e "$FG_LTYELLOW""$@""$ST_RST"
}
echo_ltblue() {
    echo_e "$FG_LTBLUE""$@""$ST_RST"
}
echo_ltmagenta() {
    echo_e "$FG_LTMAGENTA""$@""$ST_RST"
}
echo_ltcyan() {
    echo_e "$FG_LTCYAN""$@""$ST_RST"
}
echo_ltwhite() {
    echo_e "$FG_LTWHITE""$@""$ST_RST"
}

echo_black_bg() {
    echo_e "$BG_BLACK""$@""$ST_RST"
}
echo_red_bg() {
    echo_e "$BG_RED""$@""$ST_RST"
}
echo_green_bg() {
    echo_e "$BG_GREEN""$@""$ST_RST"
}
echo_yellow_bg() {
    echo_e "$BG_YELLOW""$@""$ST_RST"
}
echo_blue_bg() {
    echo_e "$BG_BLUE""$@""$ST_RST"
}
echo_magenta_bg() {
    echo_e "$BG_MAGENTA""$@""$ST_RST"
}
echo_cyan_bg() {
    echo_e "$BG_CYAN""$@""$ST_RST"
}
echo_white_bg() {
    echo_e "$BG_WHITE""$@""$ST_RST"
}

echo_bold() {
    echo_e "$ST_BOLD""$@""$ST_RST"
}
echo_underline() {
    echo_e "$ST_UNDERLINE""$@""$ST_RST"
}
echo_reverse() {
    echo_e "$ST_REVERSE""$@""$ST_RST"
}

echo_critical() {
    echo_e "$FG_LTWHITE""$BG_RED""$@""$ST_RST"
}
echo_error() {
    echo_e "$FG_LTRED""$BG_BLACK""$@""$ST_RST"
}
echo_warning() {
    echo_e "$FG_LTYELLOW""$BG_BLACK""$@""$ST_RST"
}
echo_info() {
    echo_e "$FG_LTBLUE""$BG_BLACK""$@""$ST_RST"
}
echo_debug() {
    echo_e "$ST_BOLD""$@""$ST_RST"
}
alias echo_crit=echo_critical
alias echo_warn=echo_warning
