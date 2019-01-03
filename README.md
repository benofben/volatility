# Volatility

I'm playing around with volatility in the stock market.  I first did something like this with Mathematica and MATLAB on a Christmas vacation in 2005.  It seems fitting that I'm starting a new version on Christmas vacation 2018.

## Data

I'm going to use some data from [Intrinio](https://intrinio.com/bulk-financial-data-downloads/us-fundamentals-financials-metrics-ratios-stock-prices).  I think I'll start with the 10 years of stock prices.  The fundamentals look interesting too, but maybe I'll try that later.  Similar work I've done in the past has also incorporated SEC EDGAR to look at insider trading filings.  That was based on comments Peter Lynch made in [One Up on Wall Street](https://www.amazon.com/One-Up-Wall-Street-Already/dp/0743200403).

I stuffed the data in a Google Drive [here](https://drive.google.com/open?id=1RIeXtYd2s2WG7zLQul_3uY1W64jAWgFO).

That data is going to need a ton of preprocessing including normalization.  I'm going to try some methods I used in 2008-2010.  The model worked then and I think the macro conditions might be about the same now.  preprocess.py will consolidate the data, normalize it and then break it into various data sets to ensure proper withholding.

Some of the data is sparse (missing high and low but has a close, etc) even though it shouldn't be.  I have a ticket open with Intrinio about that.

## Modeling

I'm fiddling around with H2O.ai DAI.
