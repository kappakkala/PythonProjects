**Settings module for all the postgres related projects**

Create a file `settings.yaml` using the following template.


```yaml
postgres :
  drivername : postgresql
  username : 
  password : 
  host : localhost
  port : 5432

influx :
  host : ''
  port : 8086
  username : ''
  password : ''
  db : ''
  measurement_read : ''
```