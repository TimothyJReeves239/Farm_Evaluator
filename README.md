# Goal:
	Model farm prices v. their respective distances to major urban areas to find the most cost-effective regions to combat food deserts. 

  File Explanations:

	FarmEvaluationDownloader.py - A web scraping script which pulls farm pricing, acreage, and zip code data from www.landandfarm.com. (for this case only farms in New York were considered).

	Data1.csv - The data exported from the FarmEvaluationDownloader. Was only ran once.

	Data_Analysis - Preliminary data analysis. 
		A/P added to dataframe, where A/P = Price/Acres (not a great name, I know)
		Dist2City added to dataframe, where Dist2City = Each Farm's distance to New York City (Farm Zipcodes were very general, only one zipcode was used for New York City, constructed using pgeocode).



