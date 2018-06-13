#!/usr/bin/env python
# BlackJack IRC Bot
# Developed by acidvegas in Python
# https://git.acid.vegas/blackjack
# config.py

class connection:
	server     = 'irc.silph.co'
	port       = 6697
	proxy      = None
	ipv6       = False
	ssl	       = True
	ssl_verify = False
	vhost      = None
	channel	   = '#ramen'
	key	       = None

class cert:
	file     = None
	key      = None
	password = None

class ident:
	nickname = 'BlackJack'
	username = 'blackjack'
	realname = 'https://git.supernets.org/acidvegas'

class login:
	network  = None
	nickserv = None
	operator = None

class settings:
	cmd_char = '!'
	log      = False
	modes    = None
