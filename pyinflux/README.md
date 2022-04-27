To restore an influx database from databasename.tar
`tar -xf databasename.tar`
`influxd restore -db databasename -portable databasename/`


**Query options**

`create database <databasename>` creates a new database

`use <databasename>` selects a database

`precision rfc3339` changes timestamp to datetime format 

`show measurements` lists all measurements inside a database

`select * from <measurementname>` selects all data from the measurement

`select <column> from <measurementname> where time>'<timestamp1>' and time<'<timestamp2>' and <column1>='<value>' order by desc limit <num>` selects num datapoints in descending order from a single column based on the conditions specified in the where clause

`select <column> from measurement group by <column1>` selects a column based on a column group 

`select * into <measurement_copied> from <measurement_to_copy> group by *` copies one measurement to another inside the same db.

`drop measurement <measurementname>` deletes a measurement from the database

`drop database <databasename>` deletes a database