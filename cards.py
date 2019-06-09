'''
in here is going to be all of the cards and card classes made.
I'm going to start with the deck of many things

TODO
- make class that holds a card 
- make embed that holds the class
- images for every card
- descriptions / effects for every card
- https://imgur.com/a/8wneGfK images
- The sender could be either Nozomi or Avdol

- https://imgur.com/gallery/l3EGo Rider Tarot Deck complete


cardEmbed = discord.Embed(title="This is where the title goes", colour=discord.Colour(0xffaa48), description="The description goes here")

cardEmbed.set_image(url="https://cdn.discordapp.com/embed/avatars/0.png")
cardEmbed.set_author(name="author name", icon_url="https://cdn.discordapp.com/embed/avatars/0.png")
cardEmbed.set_footer(text="Message @fops#1969 if you have any questions")

'''

import discord
import random

#base class that holds the cards
class card:
    def __init__(self, title, desc , url):
        self.title = title
        self.description = desc
        self.imgURL = url

#all of the cards
Rogue = card("Rogue","A nonplayer character of the DM's choice becomes hostile toward you. The identity of your new enemy isn't known until the NPC or someone else reveals it. Nothing less than a wish spell or Divine Intervention can end the NPC's hostility toward you.","https://i.imgur.com/voPBc64.png")
Flame = card("Flames","A powerful devil becomes your enemy. The devil seeks your ruin and plagues your life, savoring your suffering before attempting to slay you. This enmity lasts until either you or the devil dies.","https://i.imgur.com/j7kEK96.png")
Idiot = card("Idiot","Permanently reduce your Intelligence by 1d4 + 1 (to a minimum score of 1). You can draw one additional card beyond your declared draws.","https://i.imgur.com/4NtUg2g.png")
Donjon = card("Donjon","You disappear and become entombed in a state of suspended animation in an extradimensional Sphere. Everything you were wearing and carrying stays behind in the space you occupied when you disappeared. You remain imprisoned until you are found and removed from the Sphere. You can't be located by any Divination magic, but a wish spell can reveal the location of your prison. You draw no more cards.","https://i.imgur.com/Y7zITG4.png")
Void = card("Void","This black card Spells Disaster. Your soul is drawn from your body and contained in an object in a place of the DM's choice. One or more powerful beings guard the place. While your soul is trapped in this way, your body is Incapacitated. A wish spell can't restore your soul, but the spell reveals the location of the object that holds it. You draw no more cards.","https://i.imgur.com/45aIClQ.png")
Star = card("Star","Increase one of your Ability Scores by 2. The score can exceed 20 but can't exceed 24.","https://i.imgur.com/zgGikPc.png")
Throne = card("Throne","You gain proficiency in the Persuasion skill, and you double your Proficiency Bonus on checks made with that skill. In addition, you gain rightful ownership of a small keep somewhere in the world. However, the keep is currently in the hands of Monsters, which you must clear out before you can claim the keep as. yours.","https://i.imgur.com/ihUkfzo.png")
Jester = card("Jester","You gain 10,000 XP, or you can draw two additional cards beyond your declared draws.","https://i.imgur.com/9h9mMaR.png")
Visier = card("Visier","At any time you choose within one year of drawing this card, you can ask a question in meditation and mentally receive a truthful answer to that question. Besides information, the answer helps you solve a puzzling problem or other dilemma. In other words, the knowledge comes with Wisdom on how to apply it.","https://i.imgur.com/8CB1NbW.png")
Gem = card("Gem","Twenty-five pieces of jewelry worth 2,000 gp each or fifty gems worth 1,000 gp each appear at your feet.","https://i.imgur.com/8TBp17r.png")
Fool = card("Fool","You lose 10,000 XP, discard this card, and draw from the deck again, counting both draws as one of your declared draws. If losing that much XP would cause you to lose a level, you instead lose an amount that leaves you with just enough XP to keep your level.","https://i.imgur.com/m7ych8E.png")
Talons = card("Talons","Every magic item you wear or carry disintegrates. Artifacts in your possession aren't destroyed but do Vanish.","https://i.imgur.com/gGStBpn.png")
Skull = card("Skull","You summon an avatar of death-a ghostly humanoid Skeleton clad in a tattered black robe and carrying a spectral scythe. It appears in a space of the DM's choice within 10 feet of you and attacks you, warning all others that you must win the battle alone. The avatar fights until you die or it drops to 0 Hit Points, whereupon it disappears. If anyone tries to help you, the helper summons its own Avatar of Death. A creature slain by an Avatar of Death can't be restored to life.","https://i.imgur.com/bIJZZAR.png")
Moon = card("Moon","You are granted the ability to cast the wish spell 1d3 times.","https://i.imgur.com/Bcti8iW.png")
Key = card("Key","A rare or rarer Magic Weapon with which you are proficient appears in your hands. The DM chooses the weapon.","https://i.imgur.com/bAfjOyA.png")
Fates = card("Fates","Reality's fabric unravels and spins anew, allowing you to avoid or erase one event as if it never happened. You can use the card's magic as soon as you draw the card or at any other time before you die.","https://i.imgur.com/L4ag0fK.png")
Sun = card("Sun","You gain 50,000 XP, and a wondrous item (which the DM determines randomly) appears in your hands.","https://i.imgur.com/zYyIMoe.png")
Euryale = card("Euryale","The card's medusa-like visage curses you. You take a -2 penalty on Saving Throws while cursed in this way. Only a god or the magic of The Fates card can end this curse.","https://i.imgur.com/DxgQ9o1.png")
Knight = card("Knight"," You gain the service of a 4th-level Fighter who appears in a space you choose within 30 feet of you. The Fighter is of the same race as you and serves you loyally until death, believing the fates have drawn him or her to you. You control this character.","https://i.imgur.com/ZALdmca.png")
Ruin = card("Ruin","All forms of Wealth that you carry or own, other than Magic Items, are lost to you. Portable property vanishes. Businesses, buildings, and land you own are lost in a way that alters reality the least. Any documentation that proves you should own something lost to this card also disappears.","https://i.imgur.com/pvMSQTZ.png")
Comet = card("Comet","If you single-handedly defeat the next hostile monster or group of Monsters you encounter, you gain Experience Points enough to gain one level. Otherwise, this card has no effect.","https://i.imgur.com/tLWgYA5.png")
Balance = card("Balance","Your mind suffers a wrenching alteration, causing your Alignment to change. Lawful becomes chaotic, good becomes evil, and vice versa. If you are true neutral or unaligned, this card has no effect on you.","https://i.imgur.com/dlHlMSJ.png")

#a list containing all of the card classes made
cardList = [Rogue,Flame,Idiot,Donjon,Void,Star,Throne,Jester,Visier,Gem,Fool,Talons,Skull,Moon,Key,Fates,Sun,Euryale,Knight,Ruin,Comet,Balance]

#change the card to be a randomly chosen one & create the embed
def drawCard():
    chosenCard = random.choice(cardList)

    cardEmbed = discord.Embed(title=chosenCard.title, colour=discord.Colour(0xffaa48), description=chosenCard.description)
    cardEmbed.set_image(url=chosenCard.imgURL)
    cardEmbed.set_author(name="Avdol", url="https://en.wikipedia.org/wiki/Deck_of_many_things", icon_url="attachment://avdol.jpg")
    cardEmbed.set_footer(text="Message @fops#1969 if you have any questions")
    return cardEmbed
