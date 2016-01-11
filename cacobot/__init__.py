# As bad a practice this is, we use __init__ to import the commands we
# need. If there's a command you don't want to add, omit it from this
# file. This way, all main.py needs to do is import cacobot.

#base
import cacobot.base as base
import cacobot.help as dochelp # help is reserved.

#recall/database
import cacobot.quote as quote
import cacobot.tags as tags
import cacobot.changes as changes

#useful funcs
import cacobot.log as log
import cacobot.define as define
import cacobot.moderation as moderation
import cacobot.youtube as youtube

#novelties
import cacobot.dice as dice
import cacobot.stats as stats

#server-specific
import cacobot.doom as doom
import cacobot.undertale as undertale
import cacobot.utau as utau

# If you're taking the senic tour of the code, you should check out
# cacobot/base.py next.
