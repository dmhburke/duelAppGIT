from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.db.models import Sum, Count
from django.views import generic

#CHOICES
YES_NO = (
    ("YES", "Yes"),
    ("NO", "No"),
    )

EVENT_CATEGORY = (
    ("Round1Golf", "Round1Golf"),
    ("Round1CTPLD", "Round1CTPLD"),
    ("Round1_Bonus", "Round1_Bonus"),
    ("Round2Golf", "Round2Golf"),
    ("Round2CTPLD", "Round2CTPLD"),
    ("Round2_Bonus", "Round2_Bonus"),
    ("Round3Golf", "Round3Golf"),
    ("Round3CTPLD", "Round3CTPLD"),
    ("Round3_Bonus", "Round3_Bonus"),
    ("Social", "Social"),
    ("Best_dressed", "Best_dressed"),
    ("Tipping", "Tipping"),
)

DAYS = (
    ("FRIDAY", "Friday"),
    ("SATURDAY", "Saturday"),
    ("SUNDAY", "Sunday"),
    )

#TIPPING INPUT
GAME_1 = (
    ("", "Select result"),
    ("NETS", "Nets"),
    ("NETS", "Rockets"),
    )

GAME_2 = (
    ("", "Select result"),
    ("LIGHTNING", "Lightning"),
    ("ISLANDERS", "Islanders"),
    )

GAME_3 = (
    ("", "Select result"),
    ("OILERS", "Oilers"),
    ("PENGUINS", "Penguins"),
    )

GAME_4 = (
    ("", "Select result"),
    ("RAPTORS", "Raptors"),
    ("BUCKS", "Bucks"),
    )

GAME_5 = (
    ("", "Select result"),
    ("CRYSTAL_PALACE", "Crystal Palace"),
    ("LEICESTER_CITY", "Leicester City"),
    ("DRAW", "Draw"),
    )

GAME_6 = (
    ("", "Select result"),
    ("ARSENAL", "Arsenal"),
    ("WOLVERHAMPTON", "Wolverhampton"),
    ("DRAW", "Draw"),
    )

GAME_7 = (
    ("", "Select result"),
    ("ENGLAND", "England"),
    ("SOUTH AFRICA", "South Africa"),
    )


GAME_8 = (
    ("", "Select result"),
    ("OLE_MISS", "Ole Miss"),
    ("AUBURN", "Auburn"),
    )

GAME_9 = (
    ("", "Select result"),
    ("OREGON", "Oregon"),
    ("USC", "USC"),
    )

GAME_10 = (
    ("", "Select result"),
    ("MIAMI", "Miami"),
    ("FLORIDA_STATE", "Florida State"),
    )

#RESULTS CHECK - change empty result value
GAME_1R = (
    ("NOT_COMPLETE", "No result"),
    ("ROCKETS", "Rockets"),
    ("NETS", "Nets"),
    )

GAME_2R = (
    ("NOT_COMPLETE", "No result"),
    ("LIGHTNING", "Lightning"),
    ("ISLANDERS", "Islanders"),
    )

GAME_3R = (
    ("NOT_COMPLETE", "No result"),
    ("OILERS", "Oilers"),
    ("PENGUINS", "Penguins"),
    )

GAME_4R = (
    ("NOT_COMPLETE", "No result"),
    ("RAPTORS", "Raptors"),
    ("BUCKS", "Bucks"),
    )

GAME_5R = (
    ("NOT_COMPLETE", "No result"),
    ("CRYSTAL_PALACE", "Crystal Palace"),
    ("LEICESTER_CITY", "Leicester City"),
    ("DRAW", "Draw"),
    )

GAME_6R = (
    ("NOT_COMPLETE", "No result"),
    ("ENGLAND", "England"),
    ("SOUTH_AFRICA", "South Africa"),
    )

GAME_6R = (
    ("NOT_COMPLETE", "No result"),
    ("ARSENAL", "Arsenal"),
    ("WOLVERHAMPTON", "Wolverhampton"),
    ("DRAW", "Draw"),
    )

GAME_8R = (
    ("NOT_COMPLETE", "No result"),
    ("OLE_MISS", "Ole Miss"),
    ("AUBURN", "Auburn"),
    )

GAME_9R = (
    ("NOT_COMPLETE", "No result"),
    ("OREGON", "Oregon"),
    ("USC", "USC"),
    )

GAME_10R = (
    ("NOT_COMPLETE", "No result"),
    ("MIAMI", "Miami"),
    ("FLORIDA_STATE", "Florida State"),
    )
