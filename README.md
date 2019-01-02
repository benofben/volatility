# Volatility

I'm playing around with volatility in the stock market.  I first did something like this with Mathematica and MATLAB on a Christmas vacation in 2005.  It seems fitting that I'm starting a new version on Christmas vacation 2018.

# Data

I'm going to use some data from [Intrinio](https://intrinio.com/bulk-financial-data-downloads/us-fundamentals-financials-metrics-ratios-stock-prices).  I think I'll start with the 10 years of stock prices.  The fundamentals look interesting too, but maybe I'll try that later.  Similar work I've done in the past has also incorporated SEC EDGAR to look at insider trading filings.  That was based on comments Peter Lynch made in [One Up on Wall Street](https://www.amazon.com/One-Up-Wall-Street-Already/dp/0743200403).

That data is going to need a ton of preprocessing including normalization.  I'm going to try some methods I used in 2008-2010.  The model worked then and I think the macro conditions might be about the same now.