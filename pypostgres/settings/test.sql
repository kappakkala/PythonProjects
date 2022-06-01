/*scp_data15_full */
DROP TABLE IF EXISTS sde_team_data."HFT_8_04_scp_data15_full";
CREATE TABLE if not exists sde_team_data."HFT_8_04_scp_data15_full" AS (
SELECT time_bucket('15 min', time) AS bucket, percentile_cont(0.5) WITHIN GROUP (ORDER BY refrigeration) as refrigeration, percentile_cont(0.5) WITHIN GROUP (ORDER BY freezing) as freezing
FROM sde_team_data."HFT_8_03_calc_data"
GROUP BY bucket
ORDER BY bucket ASC
);
ALTER TABLE sde_team_data."HFT_8_04_scp_data15_full" RENAME bucket TO time;

/*scp_data15 */

DROP TABLE IF EXISTS sde_team_data."HFT_8_05_scp_data15";
CREATE TABLE if not exists sde_team_data."HFT_8_05_scp_data15" AS (
SELECT * FROM sde_team_data."HFT_8_04_scp_data15_full" where
	time >= (select start_time from sde_settings."times" where time_type='competition') and 
	time < (select stop_time from sde_settings."times" where time_type='competition')
);
ALTER TABLE sde_team_data."HFT_8_05_scp_data15" ADD COLUMN "8_1_scoring" BOOLEAN DEFAULT FALSE;
ALTER TABLE sde_team_data."HFT_8_05_scp_data15" ADD COLUMN "8_2_scoring" BOOLEAN DEFAULT FALSE;
UPDATE sde_team_data."HFT_8_05_scp_data15" SET "8_1_scoring" = true WHERE 
	time >= (select start_time from sde_settings."times" where subcontest='8_1') and 
	time < (select stop_time from sde_settings."times" where subcontest='8_1');
UPDATE sde_team_data."HFT_8_05_scp_data15" SET "8_2_scoring" = true WHERE 
	time >= (select start_time from sde_settings."times" where subcontest='8_2') and 
	time < (select stop_time from sde_settings."times" where subcontest='8_2');


/* merging both 8_1 and 8_2 data */
/* The columns of joining tables may be different in JOIN but in UNION the number of columns and order of columns of all queries must be same */

DROP TABLE IF EXISTS sde_team_data."temp1";
CREATE TABLE if not exists sde_team_data."temp1" AS (
	SELECT time,refrigeration as data,"8_1_scoring" FROM sde_team_data."HFT_8_05_scp_data15" 
);
ALTER TABLE sde_team_data."temp1" ADD COLUMN "contest" character varying DEFAULT NULL;
UPDATE sde_team_data."temp1" SET "contest" = '8_1';

DROP TABLE IF EXISTS sde_team_data."temp2";
CREATE TABLE if not exists sde_team_data."temp2" AS (
	SELECT time,freezing as data,"8_2_scoring" FROM sde_team_data."HFT_8_05_scp_data15" 
);
ALTER TABLE sde_team_data."temp2" ADD COLUMN "contest" character varying DEFAULT NULL;
UPDATE sde_team_data."temp2" SET "contest" = '8_2';

DROP TABLE IF EXISTS sde_team_data."HFT_8_05_scp_data15_merge";
CREATE TABLE if not exists sde_team_data."HFT_8_05_scp_data15_merge" AS (
/* union of common table columns*/
select time,data,contest from sde_team_data."temp1" union all select time,data,contest from sde_team_data."temp2" order by time asc); 
/* adding unique columns to both tables*/
ALTER TABLE sde_team_data."HFT_8_05_scp_data15_merge" ADD COLUMN "8_1_scoring" boolean DEFAULT NULL;
ALTER TABLE sde_team_data."HFT_8_05_scp_data15_merge" ADD COLUMN "8_2_scoring" boolean DEFAULT NULL;
/* updating new columns based on condition */
UPDATE sde_team_data."HFT_8_05_scp_data15_merge" set "8_1_scoring" = sde_team_data."temp1"."8_1_scoring" from sde_team_data."temp1" where sde_team_data."HFT_8_05_scp_data15_merge".contest='8_1';
UPDATE sde_team_data."HFT_8_05_scp_data15_merge" set "8_2_scoring" = sde_team_data."temp2"."8_2_scoring" from sde_team_data."temp2" where sde_team_data."HFT_8_05_scp_data15_merge".contest='8_2';

DROP TABLE IF EXISTS sde_team_data."temp1";
DROP TABLE IF EXISTS sde_team_data."temp2";
select * from sde_team_data."HFT_8_05_scp_data15_merge" t1 order by time asc;


/*prescoring */

DROP TABLE IF EXISTS sde_team_data."temp1";
CREATE TABLE if not exists sde_team_data."temp1" AS (
SELECT time, data,contest,"8_1_scoring", 
	CASE WHEN data between 2 and 6 THEN 100.0::float
		 WHEN data between 0 and 2 THEN 50*data::float
		 WHEN data between 6 and 8 THEN 50*(8-data)::float
	ELSE 0.0::float
  END 
  AS perc_points_per_scp 
	FROM sde_team_data."HFT_8_05_scp_data15_merge" where "contest"='8_1' and "8_1_scoring"=true
	);
DROP TABLE IF EXISTS sde_team_data."temp2";
CREATE TABLE if not exists sde_team_data."temp2" AS (
SELECT time, data,contest,"8_2_scoring", 
	CASE WHEN data between -28 and -18 THEN 100.0::float
		 WHEN data between -34 and -28 THEN (100*data+3400)/6::float
		 WHEN data between -18 and -12 THEN -100*(2+data/6)::float
	ELSE 0.0::float
  END 
  AS perc_points_per_scp 
	FROM sde_team_data."HFT_8_05_scp_data15_merge" where "contest"='8_2' and "8_2_scoring"=true
	);
	
DROP TABLE IF EXISTS sde_team_data."HFT_8_06_prescoring15_merge";
CREATE TABLE if not exists sde_team_data."HFT_8_06_prescoring15_merge" AS (
/* union of common table columns*/	
select time,data,contest,perc_points_per_scp from sde_team_data."temp1" union all select time,data,contest,perc_points_per_scp from sde_team_data."temp2" order by time asc); 
/* adding unique columns to both tables*/
ALTER TABLE sde_team_data."HFT_8_06_prescoring15_merge" ADD COLUMN "8_1_scoring" boolean DEFAULT NULL;
ALTER TABLE sde_team_data."HFT_8_06_prescoring15_merge" ADD COLUMN "8_2_scoring" boolean DEFAULT NULL;
/* updating new columns based on condition */
UPDATE sde_team_data."HFT_8_06_prescoring15_merge" set "8_1_scoring" = sde_team_data."temp1"."8_1_scoring" from sde_team_data."temp1" where sde_team_data."HFT_8_06_prescoring15_merge".contest='8_1';
UPDATE sde_team_data."HFT_8_06_prescoring15_merge" set "8_2_scoring" = sde_team_data."temp2"."8_2_scoring" from sde_team_data."temp2" where sde_team_data."HFT_8_06_prescoring15_merge".contest='8_2';

DROP TABLE IF EXISTS sde_team_data."temp1";
DROP TABLE IF EXISTS sde_team_data."temp2";

ALTER TABLE sde_team_data."HFT_8_06_prescoring15_merge" ADD COLUMN "points_per_scp" float DEFAULT 0.0;
ALTER TABLE sde_team_data."HFT_8_06_prescoring15_merge" ADD COLUMN "max_perc_points_per_scp" float DEFAULT 100.0;
ALTER TABLE sde_team_data."HFT_8_06_prescoring15_merge" ADD COLUMN "max_points_per_scp" float DEFAULT 5.0/880.0;
UPDATE sde_team_data."HFT_8_06_prescoring15_merge" SET "points_per_scp" = "perc_points_per_scp"*5/(880*100) where contest='8_1';
UPDATE sde_team_data."HFT_8_06_prescoring15_merge" SET "points_per_scp" = "perc_points_per_scp"*5/(880*100) where contest='8_2';
select * from sde_team_data."HFT_8_06_prescoring15_merge" t1 order by time asc;


/*scoring*/

select contest,sum("points_per_scp") as cum_sum_points from sde_team_data."HFT_8_06_prescoring15_merge" group by contest;