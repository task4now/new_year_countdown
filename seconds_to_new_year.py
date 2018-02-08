#! Seconds to New Year program
import bottle
import datetime

app = application = bottle.Bottle()


def seconds_to_new_year():
    """Creates message of remaining seconds until 2019 Year"""
    now = datetime.datetime.now()
    new_year = datetime.datetime(2019, 1, 1)
    period = new_year - now
    return "Seconds before the New Year: {} seconds!".format(
        int(round(period.total_seconds(), 0)), align='^')
