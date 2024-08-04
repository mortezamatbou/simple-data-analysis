from pathlib import Path

import typer
from loguru import logger
from tqdm import tqdm

from simple_data_analysis.config import PROCESSED_DATA_DIR, RAW_DATA_DIR
import db as db

app = typer.Typer()


@app.command()
def main(
    # ---- REPLACE DEFAULT PATHS AS APPROPRIATE ----
    input_path: Path = RAW_DATA_DIR / "dataset.csv",
    output_path: Path = PROCESSED_DATA_DIR / "dataset.csv",
    # ----------------------------------------------
):
    # ---- REPLACE THIS WITH YOUR OWN CODE ----
    logger.info("Processing dataset...")
    for i in tqdm(range(10), total=10):
        if i == 5:
            logger.info("Something happened for iteration 5.")
    logger.success("Processing dataset complete.")
    # -----------------------------------------

@app.command()
def to_csv():
    print("Test database connectivity")

if __name__ == "__main__":
    app()
