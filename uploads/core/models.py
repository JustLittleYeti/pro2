from __future__ import unicode_literals

from django.db import models


class Song(models.Models):

    title = models.CharField(max_length=100)
    lyrics = models.CharField(max_length=1000)

    def mytitle(self):
    print("Title of this song is:" + self.title)

    def myfunc(self):
    print("Lyrics of this song: " + self.lyrics)

Song_1= Song("21 Guns", "Do you know what's worth fighting for? When it's not worth dying for? Does it take your breath away? And you feel yourself suffocating? Does the pain weigh out the pride? And you look for place to hide? Did someone break your heart inside? You're in ruins... One, 21 guns Lay down your arms Give up the fight One, 21 guns Throw up your arms into the sky You and I When you're at the end of the road And you lost all sense of control And your thoughts have taken their toll When your mind breaks the spirit of your soul Your faith walks on broken glass And the hangover doesn't pass Nothing's ever built to last You're in ruins... One, 21 guns Lay down your arms Give up the fight One, 21 guns Throw up your arms into the sky You and I Did you try to live on your own? When you burned down the house and home? Did you stand too close to the fire? Like a liar looking for forgiveness from a stone When it's time to live and let die And you can't get another try Something inside this heart has died You're in ruins... One, 21 guns Lay down your arms Give up the fight One, 21 guns Throw up your arms into the sky One, 21 guns Lay down your arms Give up the fight One, 21 guns Throw up your arms into the sky You and I"