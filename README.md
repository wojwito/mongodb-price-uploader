# mongodb-price-uploader
A simple Python script used to upload prices from a <i>csv</i> file into a MongoDB timeseries collection. 
 
Please generate an input file with your test prices, rename it to <i>Prices.csv</i> and use the following format:<br>
 <pre>
 timestamp,time_in_milliseconds,price,volume
 2020-06-27 16:52,1593276720000,4.4972,4328.29</pre>

A new price gets uploaded every 60 seconds so input data *should* contain prices published once a minute.
