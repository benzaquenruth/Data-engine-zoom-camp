# Module 1 Homework – Docker & SQL & Terraform

This repository contains my solution for Module 1 of the Data Engineering Zoomcamp.

Learned how to:

✅ Containerize applications with Docker and Docker Compose
✅ Set up PostgreSQL databases and write SQL queries
✅ Build data pipelines to ingest NYC taxi data
✅ Provision cloud infrastructure with Terraform

## Steps performed
1. Set up Docker with PostgreSQL
2. Loaded NYC taxi data
3. Ran SQL queries
4. Created Terraform infrastructure

## Commands used
bash
docker run -it --rm 
uv init --python=3.13
uv add pandas pyarrow sqlalchemy psycopg2-binary
uv run python ingest_green.py
export GOOGLE_APPLICATION_CREDENTIALS="Path for the credential file"
terraform init
terraform apply
terraform destroy 


## Question and answers
Question 1. What's the version of pip in the image?

Answer:
pip 25.3 from /usr/local/lib/python3.13/site-packages/pip (python 3.13)

25.3


Question 2. Understanding Docker networking and docker-compose

Answer: db:5432

Question 3. Counting short trips
For the trips in November 2025 (lpep_pickup_datetime between '2025-11-01' and '2025-12-01', exclusive of the upper bound), how many trips had a trip_distance of less than or equal to 1 mile?

Answer:
8,007

```
SELECT COUNT(*) AS trips
FROM green_trips_2025_11
WHERE trip_distance <= 1
     AND (lpep_pickup_datetime BETWEEN '2025-11-01' AND '2025-12-01' ); 
```


Question 4. Longest trip for each day
Which was the pick up day with the longest trip distance? Only consider trips with trip_distance less than 100 miles (to exclude data errors).
Use the pick up time for your calculations.

Answer:
2025-11-14
```
SELECT lpep_pickup_datetime
FROM green_trips_2025_11
WHERE trip_distance <= 100
ORDER BY trip_distance DESC
LIMIT 1;
```


Question 5. Biggest pickup zone
Which was the the pickup zone with the largest total_amount (sum of all trips) on November 18th, 2025?

Answer:
East Harlem South
```
SELECT
    z."Zone",
    SUM(g.total_amount) AS sum_total_amount
FROM green_trips_2025_11 g
    JOIN taxi_zone_lookup z
    ON z."LocationID" = g."PULocationID"
WHERE DATE(g.lpep_pickup_datetime) = '2025-11-18'
GROUP BY z."Zone"
ORDER BY sum_total_amount DESC
LIMIT 5;
```
Question 6. Largest tip
For the passengers picked up in the zone named "East Harlem North" in November 2025, which was the drop off zone that had the largest tip?
Note: it's tip , not trip. We need the name of the zone, not the ID.

Answer:
| Upper East Side North | 4242.009999999995 |
```
SELECT
    z_do."Zone" AS dropoff_zone,
    SUM(g.tip_amount) AS total_tip
FROM green_trips_2025_11 g
JOIN taxi_zone_lookup z_pu
    ON z_pu."LocationID" = g."PULocationID"
JOIN taxi_zone_lookup z_do
    ON z_do."LocationID" = g."DOLocationID"
WHERE
    z_pu."Zone" = 'East Harlem North'
GROUP BY
    z_do."Zone"
ORDER BY
    total_tip DESC
LIMIT 1;
```


Question 7. Terraform Workflow
Which of the following sequences, respectively, describes the workflow for:
terraform import, terraform apply -y, terraform destroy
teraform init, terraform plan -auto-apply, terraform rm
terraform init, terraform run -auto-approve, terraform destroy
terraform init, terraform apply -auto-approve, terraform destroy
terraform import, terraform apply -y, terraform rm

Answer:
terraform init
terraform apply -auto-approve
terraform destroy



