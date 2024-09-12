# Strikeout Spinrate correlation
This is a personal project in which I use python pandas and matplotlib libraries to statistically analyze pitches.
I look at a variety of individual pitch metrics to see which are most closely correlated to a pitcher's strikeout rate.

My initial hypothesis was that spinrate of a pitcher's breaking pitch spinrate (usually the curveball or slider) would have the highest correlation, hence the repo name. But, it's actually Fastball Speed that's most associated with striking out the competition. One metric with a low correlation to strikeouts is Fastball Break (Why would you need a fastball to move? It's a *fast*ball.).

To run it for yourself:
```
python read_from_excel.py
```

The dataset is from MLB https://baseballsavant.mlb.com/