import argparse

from slacker import Slacker

cli = argparse.ArgumentParser()
cli.add_argument('-t',
                 '--slacktoken',
                 type=str)
cli.add_argument('-c',
                 '--channel',
                 type=str)
cli.add_argument('-m',
                 '--message',
                 type=str)
args = cli.parse_args()
slack_token = args.slacktoken
slack_channel = args.channel
message = args.message
sc = Slacker(slack_token)
sc.chat.post_message(channel=slack_channel, text=message)
