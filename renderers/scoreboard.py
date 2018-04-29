from renderers.bases import BasesRenderer
from renderers.inning import InningRenderer
from renderers.outs import OutsRenderer
from renderers.pitches import PitchesRenderer
from renderers.teams import TeamsRenderer
from data.inning import Inning

class Scoreboard:
  def __init__(self, canvas, scoreboard, config):
    self.canvas = canvas
    self.scoreboard = scoreboard
    self.config = config

  def render(self):
    TeamsRenderer(self.canvas, self.scoreboard.home_team, self.scoreboard.away_team, self.config).render()
    InningRenderer(self.canvas, self.scoreboard.inning, self.config.coords["inning"]).render()

    if self.scoreboard.inning.state == Inning.TOP or self.scoreboard.inning.state == Inning.BOTTOM:
      coords = self.config.coords
      nohitter = self.scoreboard.nohitter if self.scoreboard.inning.number > 5 else False
      PitchesRenderer(self.canvas, self.scoreboard.pitches, coords["pitches"], nohitter).render()
      OutsRenderer(self.canvas, self.scoreboard.outs, coords["outs"], nohitter).render()
      BasesRenderer(self.canvas, self.scoreboard.bases, coords["bases"]).render()
