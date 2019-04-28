itFloats(WitchWeight, DuckWeight):- WitchWeight = DuckWeight.
madeOfWood(WitchWeight, DuckWeight):- itFloats(WitchWeight, DuckWeight).
itBurns(WitchWeight, DuckWeight):- madeOfWood(WitchWeight, DuckWeight).
isAWitch(WitchWeight, DuckWeight):- itBurns(WitchWeight, DuckWeight).
