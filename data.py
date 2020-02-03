import discord

def  init():
    global bot_token
    global self_bot_token
    global message
    global embed
    global output_channel
    global input_channels
    global command_channel

    global game_in_session
    global counter_public_1
    global counter_public_2
    global counter_public_3
    global counter_private_1
    global counter_private_2
    global counter_private_3
    global counter1
    global counter2
    global counter3
    global weight
    global weight_time
    global seconds_elapsed

bot_token = 'NTk5OTY4NDE3MjQzNTk0NzUz.XStcmg.K9TSLK9MYdonsd8YYAKYzSH-Hi4'
self_bot_token = 'NDkwODkzNjYyMzU2NzY2NzI2.XL9GrA.D4zTKrSmg8GLLn76-g8b8SlruKc'

message = None
embed = None
embed_best = None

#trivia-answers
output_channel = discord.Object(id= '600006755568713729')

input_hq_private  = [
    "569420198717816852",
    "459842150323060736",
    "523359669280833536",
	"535628205139296256",
	"525131707410677761",
	"513818250652680213",
	"544381529829146645",
    "569843705654149130",
    "566979656083963918", # answers1
    "559442345674670082", #answers2
    '559357612068700183' #trivia-answers
]
input_hq_public = ['600006755568713729']
command_channel = '600006755568713729' #trivia-answers
admin_chat = '600006755568713729' # answers2

game_in_session = False
counter_public_1 = 0
counter_public_2 = 0
counter_public_3 = 0
counter_private_1 = 0
counter_private_2 = 0
counter_private_3 = 0
counter1 = 0
counter2 = 0
counter3 = 0
weight = 5
weight_time = 1
wronggone1 = 0
wronggone2 = 0
wronggone3 = 0

seconds_elapsed = 0
