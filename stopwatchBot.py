#!/usr/bin/python

from datetime import datetime
from errbot import botcmd, BotPlugin

__author__ = 'taoistmath'

class StopwatchBot(BotPlugin):

    stopwatchDict = {}

    date_format = '%a %b %d %H:%M:%S %Y'

    @botcmd
    def timer_start(self, mess, args):
        """ Starts timer
        Example: !timer start Regression Testing
        """

        if not args:
            return 'Please enter a title for your timer.'

        timer_title = args.title()

        if (timer_title in self.stopwatchDict):
            return "{0} is already running, started at: {1}".format(timer_title, self.stopwatchDict.get(timer_title, 2))
        else:
            start_time = datetime.strftime(datetime.now(), self.date_format)
            self.stopwatchDict[timer_title] = start_time

            return "{0} was started at: {1}".format(timer_title, start_time)

    @botcmd
    def timer_list(self, mess, args):
        """ Tells you what is being timed
        Example: !timer list
        """

        stopwatchList = ''

        if not self.stopwatchDict:
            return "Nothing is being timed. Use !timer start <something_or_other> to start timing."

        for key, value in self.stopwatchDict.items() :
            stopwatchList = stopwatchList + "{0} - Started at: {1} \n".format(key, value)

        return stopwatchList

    @botcmd
    def timer_stop(self, mess, args):
        """ Stops timer, tells how much time elapsed
        Example: !timer stop Regression Testing
        """

        if not args:
            return 'Please enter the title of the timer you would like to stop.'

        timer_title = args.title()

        if (timer_title not in self.stopwatchDict):
            return "You have to start {0} before you can stop it".format(timer_title)
        else:
            start_time = self.stopwatchDict.get(timer_title, 2)
            end_time = datetime.strftime(datetime.now(), self.date_format)
            elapsed_time = datetime.strptime(end_time, self.date_format) - datetime.strptime(start_time, self.date_format)
            del self.stopwatchDict[timer_title]

            return "{0} was finished at: {1}".format(timer_title, end_time) + '\n' + "{0} took: {1}".format(timer_title, elapsed_time)
