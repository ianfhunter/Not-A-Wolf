import botlib,sys,scrapemark,linecache,random
import os
import unicodedata
             
##
# command arguments must be:
#	@BotName
#	@Server
#	@Channel to join (no #)
##
 
#Param Stuff
if len(sys.argv) < 4:
	sys.exit("You do not have the correct amount of Parameters - name,server,channel(no \'#\')")

bot_name = sys.argv[1]
server = sys.argv[2]
start_channel = '#' + sys.argv[3]

#Game Variables
active_players = 0









#Printing
def one_liner(self,string):
    if self.get_channel()[0] == "#":
        self.protocol.privmsg(self.get_channel(), string)
    else:
        self.protocol.privmsg(self.get_username(), string)


#1 - Anywhere in String
def trigger_word(self,trigger,result,option):
    if option == 1:
        if botlib.check_found(self.data, trigger):
            one_liner(self,result)
    else:
        if botlib.check_on_own(self.data, trigger):
            one_liner(self,result)
            

# Create a new class for our bot, extending the Bot class from botlib
class WolfBot(botlib.Bot):
	
    def __init__(self, server, channel, nick, password=None):
        botlib.Bot.__init__(self, server, 6667, channel, nick) 
	
    def __actions__(self):

        botlib.Bot.__actions__(self)
        print self.data

        if botlib.check_on_own(self.data, "!join ") or botlib.check_found(self.data, "!j "):
            active_players[self.get_username()] = True

        if botlib.check_on_own(self.data, "!quit ") or botlib.check_found(self.data, "!q "):
            active_players[self.get_username()] = False

        if botlib.check_on_own(self.data, "!channel ") or botlib.check_found(self.data, "!c"):
            channel = self.get_args();
            if len(channel) == 0:
                one_liner(self,"Please tell me a channel to go in. I'm not psychic you know!")
            elif channel[0][0] != '#':
                one_liner(self,"# plz")
            else:
                one_liner(self,"Alrighty")
                self.protocol.join(channel[0])
                self.protocol.privmsg(channel[0], "Sup? please blame %s for the proceeding spam!" % self.get_username())

        elif botlib.check_on_own(self.data, "!lynch"):
            one_liner(self, "!v brendan")
        elif botlib.check_on_own(self.data,"You are a seer"):
            oneliner(self, "I'm Seer")
	    else:
		pass
			
if __name__ == "__main__":
    # Create new instance of our bot and run it
    HelloWorldBot(server,start_channel, bot_name).run()