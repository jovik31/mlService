
CREATE USER docker_postgres;
GRANT ALL PRIVILEGES ON DATABASE ml_service_db TO docker_postgres;



CREATE TABLE IF NOT EXISTS Problem (
  problem_id VARCHAR ( 50 ) PRIMARY KEY NOT NULL,
  last_updated TIMESTAMP NOT NULL,
  description VARCHAR ( 200 ) NOT NULL
);

CREATE TABLE IF NOT EXISTS Dataset (
  dataset_id VARCHAR ( 50 ) PRIMARY KEY NOT NULL,
  dataset_file_path VARCHAR ( 100 ) NOT NULL,
  dataset_info_path VARCHAR ( 100 ) NOT NULL
);

CREATE TABLE IF NOT EXISTS Models (
  model_id VARCHAR ( 50 ) PRIMARY KEY NOT NULL,
  saved_model_path VARCHAR ( 100 ) NOT NULL,
  hyperparameter_path VARCHAR ( 100 ) NOT NULL
);


CREATE TABLE IF NOT EXISTS Result (
  result_id varchar ( 50 ) PRIMARY KEY NOT NULL,
  problem_id varchar ( 50 ) NOT NULL,
  model_id varchar ( 50) NOT NULL,
  dataset_id varchar ( 50 ) NOT NULL,
  results_metric_path varchar ( 100)
);

ALTER TABLE Result ADD CONSTRAINT problem_id_constraint FOREIGN KEY (problem_id) REFERENCES Problem(problem_id);
ALTER TABLE Result ADD CONSTRAINT dataset_id_constraint FOREIGN KEY (dataset_id) REFERENCES Dataset(dataset_id);
ALTER TABLE Result ADD CONSTRAINT model_id_constraint FOREIGN KEY (model_id) REFERENCES Models(model_id);


