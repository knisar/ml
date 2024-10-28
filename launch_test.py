import wandb
import numpy as np

with wandb.init(project="launch-example", entity="wandb-smle", config={"learning_rate": 0.001,
 "epochs": 100, "batch_size": 128}, job_type="PreProcessing1") as run:
  wandb.run.log_code()
  for i in range(1000):
    wandb.log({
      "metric1":    np.random.uniform()*i,
      "metric2": np.sin(i)*np.random.normal()*i
    })