CREATE TABLE [IF NOT EXISTS] Problem (
  problem_id VARCHAR ( 50 ) PRIMARY KEY,
  last_updated TIMESTAMP NOT NULL
  PRIMARY KEY (problem_id)
);

CREATE TABLE Result (
  result_id varchar PRIMARY KEY,
  problem_id varchar FOREIGN_KEY(Problem),
  model_id varchar FOREIGN_KEY(Model),
  dataset_id varchar FOREIGN_KEY(Dataset),
  results_metric_path varchar
);
