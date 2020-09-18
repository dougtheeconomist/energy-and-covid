# energy-and-covid
# A brief look at U.S. energy consumption trends during the pandemic

 
The purpose of this exercise is to take a brief look at electricity consumption and generation trends during the beginning of the Covid-19 outbreak in the U.S. It is fairly common knowledge that gasoline consumption, and with it oil prices, have plummetted during the outbreak, and this peaked my curiosity as to what, if any, effect the pandemic is having on the electric grid. 

As a refresher for anyone who hasn’t been following the trading price of crude oil throughout the summer, see the following graph, provided by the EIA.

![eia_graph](/images/daily_oil_prices_eia.png)

My expectation prior to actually looking at any of the data is that while commercial and industrial energy use likely fell though not as much as transportation, residential use would rise due to the shift to people spending more of their time at home. Rather than looking at shifts from one month to the next, I am using the average monthly consumption for years in the near past as my benchmark, to avoid seasonal biases. Specifically I average data by month from 2008 through 2019. While I did glance at the simple comparison of 2019 to 2020 data, using a wider lens of comparison gives us a more robust idea of what we should expect to see for the months of March, April and May under more normal circumstances. The following table shows the consumption for the month in 2020, with the difference between that and the average for that month in previous years and the p-value of the t-test to determine whether or not the 2020 value fits within the same historical distribution 

This data has been slow to be released; even at the beginning of September only data through the month of May has been published, but what data is available through the U.S Energy Information Administration gives us a useful look at what was happening at the start of the pandemic in the U.S. The following graph shows the overall energy use in the U.S. since the start of 2018. 

![total_use](/images/total_use_trend.png)

As we can see from this graph, total use, which includes transportation uses such as gasoline, declined significantly in April with some bounce-back in May. To really understand the electricity use trends during Covid and how they are different from a typical year it’s useful to not only compare overall monthly consumption to previous years, but consumption by source, i.e. residential use vs commercial use, vs industrial use, etc. This gives us a better picture of what is driving any overall changes in usage trends over the first months of the year.  

![breakdown_by_source](/images/sector_trends.png)

As we see here it is predominantly the fall in industrial and transportation use that drives the change we see in the overall trend. While residential and commercial energy use are falling, they are doing so in line with the annual trends in those areas. In fact, when compared to the typical use for the months of April and May, there was actually more energy use by residencies and commercial properties during covid. The increase in residential use makes sense since people are spending more time at home, but the slight increase in commercial usage is a surprise to see, especially with many businesses having temporarily closed during that time. 

The following table shows the percentage difference between use in April 2020 and the typical use for the month of April since 2008, with a p-value generated against a null hypothesis that the 2020 numbers are actually the normal for that month, so in this case, the smaller the p-value the more confidence we can have that the difference in question is a significant one. 


## March
|Sector			               | Difference from Average | P - Value |
|------------------------------|:------------------------|:----------|
| Residential  	               | -9.85% 		         | 0.0351    |
| Commercial	               | -4.57%  		         | 0.2429    |
| Industrial	               | 6.44%   		         | 0.0030    |
| Transportation               | -10.41%  		         | 0.0000    |
| Energy Generation            | -8.83%  		         | 0.0000    |
| Total                        | -5.87%                  | 0.0002    |


## April
|Sector			               | Difference from Average | P - Value |
|------------------------------|:------------------------|:----------|
| Residential  	               | 11.84% 	             | 0.0076    |
| Commercial	               | 3.03% 		             | 0.3617    |
| Industrial	               | -2.99%  		         | 0.0959    |
| Transportation               | -29.9% 		         | 0.0000    |
| Energy Generation            | -11.61%  		         | 0.0000    |
| Total                        | -13.03%                 | 0.0000    |


## May
|Sector			               | Difference from Average | P - Value |
|------------------------------|:------------------------|:----------|
| Residential  	               | 23.64% 	             | 0.0000    |
| Commercial	               | 6.79%  	             | 0.0209    |
| Industrial	               | -1.83%  		         | 0.3447    |
| Transportation               | -22.64%  		         | 0.0000    |
| Energy Generation            | -10.96%  		         | 0.0000    |
| Total                        | -10.52%                 | 0.0000    |

While there are some values here that fall within the normal range of consumption for the time of year such as the commercial use in March and industrial use in May, by and large the level of energy utilization for most sectors is significantly different from what we typically see. It is safe to conclude that while transportation may be one of the biggest drivers, it is not the only industry who has broken from its normal energy use patterns. 

The follow up question that this bring us to is then, how is this change in demand effecting the supply side of the energy equation? We have already seen that it has wreaked havoc on the prices of crude oil, but how have different types of generation i.e. different fossil fuel and clean energy sources changed their production levels? 

Prior to looking at any of the data it is my intuitive assumption that energy sources such as solar, wind and hydroelectric would be least effected by the drop in demand. The reasoning for making this assumption is that because of a lower marginal operating cost due to cheaper inputs (sunlight and wind are cheaper than oil or coal) it makes sense from a cost efficiency standpoint to cut production from fossil fuel sources when needed.

![gen_comparison](/images/f_v_r.png)

When graphing generation breakdown between proportion of energy from fossil fuel and renewable generation, it seems that not only has fossil fuel generation decreased, but renewable generation has increased its share of overall generation, though this is likely more due to the fact that there is a large decrease in fossil fuel output rather than a jump in output from renewable sources. This can be verified in the next graph which displays the actual output levels for fossil fuels, renewables and the production total.  

![production_graph](/images/production.png)

## April
|Production Source			   | Difference from Average | P - Value |
|------------------------------|:------------------------|:----------|
| Coal    	                   | -51.69% 		         | 0.0000    |
| Crude Oil	                   | 30.84%  		         | 0.0036    |
| Natural Gas	               | 31.96%  		         | 0.0000    |
| Nat. Gas Liquids	           | 65.18%  		         | 0.0000    |
| Nuclear	                   | 10.75%   		         | 0.0000    |
| Hydro-Electric               | 11.06%  		         | 0.0099    |
| Solar                        | 268.65%  		         | 0.0000    |
| Wind                         | 61.31%                  | 0.0005    |
| Biomass                      | -4.3%                   | 0.1642    |
| Geothermal                   | 6.63%                   | 0.0001    |

## May 
|Production Source			   | Difference from Average | P - Value |
|------------------------------|:------------------------|:----------|
| Coal    	                   | -51.98% 		         | 0.0000    |
| Crude Oil	                   | 26.55%  		         | 0.0082    |
| Natural Gas	               | 27.93%  		         | 0.0001    |
| Nat. Gas Liquids	           | 57.75%  		         | 0.0001    |
| Nuclear	                   | 0.25%   		         | 0.8603    |
| Hydro-Electric               | 0.96%  		         | 0.7953    |
| Solar                        | 230.63%  		         | 0.0000    |
| Wind                         | 77.29%                  | 0.0001    |
| Biomass                      | -8.05%                  | 0.0188    |
| Geothermal                   | 1.74%                   | 0.1094    |
