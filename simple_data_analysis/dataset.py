from pathlib import Path

import typer
from loguru import logger
from tqdm import tqdm

from simple_data_analysis.config import PROCESSED_DATA_DIR, RAW_DATA_DIR

import db as db
import pandas as pd
import shutil

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
def to_csv(vr: int = 1):
    if vr < 0:
        raise Exception("version value must be >= 0")

    dir = RAW_DATA_DIR / str(vr)

    if dir.is_dir():
        # delete version folder
        shutil.rmtree(dir)

    # make new one
    dir.mkdir()
    
    """
    Read tables, store in csv file
    
    List of tables:
    +---------------+
    | Tables_in_db  |
    +---------------+
    | Album         |
    | Artist        |
    | Customer      |
    | Employee      |
    | Genre         |
    | Invoice       |
    | InvoiceLine   |
    | MediaType     |
    | Playlist      |
    | PlaylistTrack |
    | Track         |
    +---------------+
    """

    tables = [
        "Album",
        "Artist",
        "Customer",
        "Employee",
        "Genre",
        "Invoice",
        "InvoiceLine",
        "MediaType",
        "Playlist",
        "PlaylistTrack",
        "Track"
    ]
    
    for table in tables:
        sql = f'SELECT * FROM {table}'
        db.db.execute(sql)
        result = db.db.fetchall()
        df = pd.DataFrame(result)
        df.to_csv(dir / f"{table}.csv")
    
    print("Tables loaded successfully in ", dir)

if __name__ == "__main__":
    app()
